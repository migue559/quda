from .schemaBase import *
from .models import *
from .forms import *

import graphql_jwt

############################################################
class SiteNode(DjangoObjectType):
    class Meta:
        model = Site

############################################################
class ModuleNode(DjangoObjectType):
    class Meta:
        model = Module

############################################################
class OrganizationNode(DjangoObjectType):
    class Meta:
        model = Organization

############################################################
class UserNode(BaseNode):
    get_all_permissions = graphene.String(source='get_all_permissions')
    getProfiles = graphene.String(source='getProfiles')
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'username': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'visibleUsername': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )
        connection_class = ConnectionBase
    @classmethod
    def get_queryset(cls, queryset, info):
        return cls.sortBy(queryset, info)

class UserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserNode)
    class Meta:
        form_class = UserForm

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    coreuser = graphene.Field(UserNode)
    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(coreuser=info.context.user)

############################################################
######### QUERY & MUTATION & SUBSCRIPTION
############################################################
class Query(object):
    verify_token = graphql_jwt.Verify.Field()
    modelVar = graphene.Field(ModelVar, resolver=resolve_modelVar)
    coreuser = graphene.relay.Node.Field(UserNode)
    coreuserQuery = DjangoFilterConnectionField(UserNode, sort=graphene.String())

class Mutation(object):
    token_auth = ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    coreuserForm = UserMutation.Field()

class Subscription(graphene.ObjectType):
    pass

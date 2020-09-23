from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

    name = "core"
    verbose_name = _("core")
    def ready(self):
        import .signals

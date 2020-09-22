from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

    name = "quda.core"
    verbose_name = _("QUDA")
    def ready(self):
        import quda.core.signals

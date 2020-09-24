from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CoreConfig(AppConfig):
    name = "quda.core"
    verbose_name = _("QUDA")
    def ready(self):
        try:
            import quda.core.signals
        except ImportError:
            pass

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MeasurementsConfig(AppConfig):
    name = 'measurements'
    verbose_name = _('Measurements module')

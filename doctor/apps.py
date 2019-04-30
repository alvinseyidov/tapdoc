from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

class DoctorConfig(AppConfig):
    name = 'doctor'

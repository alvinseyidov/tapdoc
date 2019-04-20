from modeltranslation.translator import translator, TranslationOptions
from .models import Clinic

class ClinicTranslationOptions(TranslationOptions):
    fields = ('name', 'address','description','descriptionmeta','metro1','metro1distance','metro2','metro2distance')

translator.register(Clinic, ClinicTranslationOptions)

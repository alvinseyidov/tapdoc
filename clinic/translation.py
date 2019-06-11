
from modeltranslation.translator import translator, TranslationOptions
from .models import Clinic, City

class ClinicTranslationOptions(TranslationOptions):
    fields = ('name', 'address','description','descriptionmeta','descriptionmetadiaqnostika','metro1','metro1distance','metro2','metro2distance')

translator.register(Clinic, ClinicTranslationOptions)

class CityTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(City, CityTranslationOptions)

from modeltranslation.translator import translator, TranslationOptions
from .models import Company

class CompanyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Company, CompanyTranslationOptions)

from modeltranslation.translator import translator, TranslationOptions
from .models import Doctor, Profession

class DoctorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name','title','description',)

translator.register(Doctor, DoctorTranslationOptions)

class ProfessionTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

translator.register(Profession, ProfessionTranslationOptions)

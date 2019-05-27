from modeltranslation.translator import translator, TranslationOptions
from .models import XidmatlarGroup, Xidmatlar, DiaqnostikalarGroup, Diaqnostikalar, Xidmat, Diaqnostika

class XidmatlarGroupTranslationOptions(TranslationOptions):
    fields = ('group_name',)

translator.register(XidmatlarGroup, XidmatlarGroupTranslationOptions)

class XidmatlarTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Xidmatlar, XidmatlarTranslationOptions)

class XidmatTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Xidmat, XidmatlarTranslationOptions)

class DiaqnostikaTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Diaqnostika, XidmatlarTranslationOptions)

class DiaqnostikalarGroupTranslationOptions(TranslationOptions):
    fields = ('group_name',)

translator.register(DiaqnostikalarGroup, DiaqnostikalarGroupTranslationOptions)


class DiaqnostikalarTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Diaqnostikalar, DiaqnostikalarTranslationOptions)

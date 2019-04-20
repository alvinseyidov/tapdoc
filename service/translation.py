from modeltranslation.translator import translator, TranslationOptions
from .models import XidmatlarGroup, Xidmatlar, DiaqnostikalarGroup, Diaqnostikalar

class XidmatlarGroupTranslationOptions(TranslationOptions):
    fields = ('group_name',)

translator.register(XidmatlarGroup, XidmatlarGroupTranslationOptions)

class XidmatlarTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(Xidmatlar, XidmatlarTranslationOptions)

class DiaqnostikalarGroupTranslationOptions(TranslationOptions):
    fields = ('group_name',)

translator.register(DiaqnostikalarGroup, DiaqnostikalarGroupTranslationOptions)


class DiaqnostikalarTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Diaqnostikalar, DiaqnostikalarTranslationOptions)

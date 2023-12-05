from modeltranslation.translator import translator, TranslationOptions
from .models import Site, Direction, SiteType


class SitesTranslationOptions(TranslationOptions):
    fields = ('title', 'about',)


class DirectionsTranslationOptions(TranslationOptions):
    fields = ('title',)


class SiteTypeTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Site, SitesTranslationOptions)
translator.register(SiteType, SiteTypeTranslationOptions)
translator.register(Direction, DirectionsTranslationOptions)

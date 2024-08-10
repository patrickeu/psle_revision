from django.contrib import admin
from .models import word,wordMeaning,sampleSentence

class wordMeaningAdmin(admin.ModelAdmin):
    list_display = ["word","description"]
    list_per_page = 20

class sampleAdmin(admin.ModelAdmin):
    # fields = ["word","meaning","sentence"]
    list_display = ["word","sentence"]
    list_per_page = 20
# Register your models here.
admin.site.register(word)
admin.site.register(wordMeaning, wordMeaningAdmin)
admin.site.register(sampleSentence, sampleAdmin)
from django.contrib import admin
from .models import idiom, idiomSample
# Register your models here.
class idiomAdmin(admin.ModelAdmin):
    list_display = ["word","chinese"]
    list_per_page = 300

class idiomSampleAdmin(admin.ModelAdmin):
    list_display = ["idiom","sampleSentence"]
    list_per_page = 300
    
admin.site.register(idiom,idiomAdmin)
admin.site.register(idiomSample, idiomSampleAdmin)
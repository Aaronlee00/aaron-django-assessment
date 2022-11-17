from django.contrib import admin
from .models import Data


class HeaderAdmin(admin.ModelAdmin):
    #list_display= ('user_ID','input',Data.score)
    list_display= ('user_ID','keyin','input','score',Data.keyin_total_score)
    list_filter = ['user_ID','keyin']
    search_fields = ['user_ID','keyin']

admin.site.register(Data, HeaderAdmin)

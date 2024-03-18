from django.contrib import admin
from .models import News, Email, Users

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'body', 'email', 'sent']
    raw_id_fields = ['email']

admin.site.register(Email)

admin.site.register(Users)

from django.contrib import admin
from .models import Comment, News, Event




# Register your models here.
admin.site.register(Comment)
admin.site.register(Event)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author' )


from django.contrib import admin
from .models import Category, Recruitment, Video, Comment, UploadFile, Notes
from django.utils.html import format_html

admin.site.register(Recruitment)
# Register your models here.

admin.site.register(Category)


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin): 
    list_display = ('title', 'discription', 'created_on')
    list_filter = ('title', 'created_on')
    search_fields = ("title__startswith", )
    date_hierarchy = 'created_on'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')
    
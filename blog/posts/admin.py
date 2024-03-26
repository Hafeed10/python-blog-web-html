from django.contrib import admin

# Register your models here.
from posts.models import *

admin.site.register(Author)

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'published_date', 'is_draft', 'is_deleted')

admin.site.register(Post, PostAdmin)
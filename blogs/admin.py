from django.contrib import admin

from blogs.models import Blog,Comment

class BookInline(admin.TabularInline):
    model = Comment
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Blog, AuthorAdmin)
admin.site.register(Comment)
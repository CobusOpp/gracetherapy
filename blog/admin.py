from django.contrib import admin

from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)


admin.site.site_header = "Grace Therapy Admin"
admin.site.site_header = 'Grace Therapy'
admin.site.site_title = 'Grace Therapy'

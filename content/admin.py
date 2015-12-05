from django.contrib import admin

from .models import Post, Comment, UserProfile

###
#Admin actions
###
def activate(modeladmin, request, queryset):
    queryset.update(active=True)
    activate.short_description = "Activate selected entries"

def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)
    deactivate.short_description = "Deactivate selected entries"

###
#Admin classes
###
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'date_published',  'like_count', 'comment_count', 'active' ]
    prepopulated_fields = {'slug': ('title',)}
    actions = [activate, deactivate]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'display_author', 'content', 'timestamp', 'parent_post', 'active']
    actions = [activate, deactivate]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['age','birthday','color']

# class WYSIWYGAdmin(admin.ModelAdmin):
#     form = WYSYWIGForm

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile)
# admin.site.register(WYSIWYG, WYSIWYGAdmin)



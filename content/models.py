from django.db import models
from django.contrib.auth.models import User
#from ckeditor_uploader.fields import RichTextUploadingField

#Blog Post Class
class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    # rich_content = RichTextUploadingField(config_name='toolbar_Eric', blank=True)
    author = models.ForeignKey(User, related_name='post_author')
    date_published = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date_published"]

    def get_absolute_url(self):
        return "/%s" % self.slug

    def get_like_count(self):
        return self.like_count

#Comment Class
class Comment(models.Model):
    display_author = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='comment_author')
    timestamp = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    content = models.TextField()
    parent_post = models.ForeignKey('Post', related_name='parent_post')
    active = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    like_count = models.IntegerField(default=0)

    def get_like_count(self):
        return self.like_count

#####
# #WYSIWYG Editor class
# #Do we need both fields?
# #Lets keep this out for now. Get the initial site working before adding 3rd parties
#####
# class WYSIWYG(models.Model):
#     content = RichTextField(config_name='toolbar_Eric')
#     upload = RichTextUploadingField(config_name='toolbar_Eric')

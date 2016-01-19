from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField

import random
##Third Party
from ckeditor_uploader.fields import RichTextUploadingField
from colorful.fields import RGBColorField


#Blog Post Class
class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    rich_content = RichTextUploadingField(config_name='toolbar_Eric', blank=True)
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

    def get_comment_count(self):
        return self.post_comments.filter(active=True).count()

#Comment Class
class Comment(models.Model):
    display_author = models.CharField(max_length=200, default="anonymous coward")
    author = models.ForeignKey(User, related_name='comment_author')
    timestamp = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    content = models.TextField()
    parent_post = models.ForeignKey('Post', related_name='post_comments')
    active = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    like_count = models.IntegerField(default=0)

    def get_like_count(self):
        return self.like_count

#helper funcitons
def generate_image_path(instance, filename):
        ext = filename.split('.')[-1]
        return 'users/%s/profile.%s' % (instance.user.username, ext)

def random_color():
    return "#%06x".upper() % random.randint(0, 0xFFFFFF)

#User Profile Class
class UserProfile(models.Model):

    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User)
    age = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    addr_street = models.CharField(max_length=500, null=True, blank=True, default='None')
    addr_city = models.CharField(max_length=200, null=True, blank=True, default='None')
    addr_state = models.CharField(max_length=2, null=True, blank=True, default='NA')
    addr_zip = models.IntegerField(null=True, blank=True)
    prof_pic = models.ImageField(upload_to=generate_image_path, height_field='prof_h', width_field='prof_w', blank=True, null=True)
    prof_h = models.IntegerField(null=True, blank=True, default=200)
    prof_w = models.IntegerField(null=True, blank=True, default=200)
    color = RGBColorField(default=random_color(), null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def get_letter(self):
        return self.user.username[0].upper()

#Bug Report Class
class BugReport(models.Model):
    OS_CHOICES = (
        ('OSX', 'Mac OSX'),
        ('WINDOWS', 'Windows'),
        ('LINUX', 'Linux'),
        ('OTHER', 'Something Else')
        )
    os = models.CharField(max_length=200, choices=OS_CHOICES)
    BROWSER_CHOICES = (
        ('CHROME', 'Google Chrome'),
        ('FIREFOX', 'Mozilla Firefox'),
        ('SAFARI', 'Apple Safari'),
        ('IE', 'Internet Explorer'),
        ('EDGE', 'Microsoft Edge'),
        ('OTHER', 'Something Else')
        )
    browser = models.CharField(max_length=200, choices=BROWSER_CHOICES)
    bug = models.TextField()
    steps = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    feature = models.BooleanField(default=False)


#Xmas gifts class never got used
class Xmas(models.Model):
    giftee = models.OneToOneField(User)
    snitch_on = models.OneToOneField(User, related_name='snitch', default=False)
    age = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    addr_street = models.CharField(max_length=500, null=True, blank=True, default='None')
    addr_city = models.CharField(max_length=200, null=True, blank=True, default='None')
    addr_state = models.CharField(max_length=2, null=True, blank=True, default='NA')
    addr_zip = models.IntegerField(null=True, blank=True)
    movies = models.TextField(null=True, blank=True)
    books = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    games = models.TextField(null=True, blank=True)
    systems = models.TextField(null=True, blank=True)
    color1 = RGBColorField(default='#000000', null=True, blank=True)
    color2 = RGBColorField(default='#000000', null=True, blank=True)
    color3 = RGBColorField(default='#000000', null=True, blank=True)
    color4 = RGBColorField(default='#000000', null=True, blank=True)
    color5 = RGBColorField(default='#000000', null=True, blank=True)
    candy = models.CharField(max_length=300, null=True, blank=True)
    animal = models.CharField(max_length=200, null=True, blank=True)
    drink = models.CharField(max_length=200, null=True, blank=True)
    learning = models.TextField(null=True, blank=True)
    shirt = models.CharField(max_length=200, null=True, blank=True)
    pants = models.CharField(max_length=200, null=True, blank=True)
    hat = models.CharField(max_length=200, null=True, blank=True)
    dress = models.CharField(max_length=200, null=True, blank=True)
    shoe = models.CharField(max_length=200, null=True, blank=True)
    # colors = ArrayField(RGBColorField(blank=True, null=True))


#####
# #WYSIWYG Editor class
# #Do we need both fields?
# #Lets keep this out for now. Get the initial site working before adding 3rd parties
#####
# class WYSIWYG(models.Model):
#     content = RichTextField(config_name='toolbar_Eric')
#     upload = RichTextUploadingField(config_name='toolbar_Eric')

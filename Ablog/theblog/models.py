from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    
    profile_pic =  models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_icon = models.ImageField(null=True,blank=True,upload_to="images/social/")
    facebook_icon = models.ImageField(null=True,blank=True,upload_to="images/social/")
    twitter_icon = models.ImageField(null=True,blank=True,upload_to="images/social/")
    instagram_icon = models.ImageField(null=True,blank=True,upload_to="images/social/")
    website_url = models.CharField(max_length=255,null=True,blank=True)
    fb_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    instagram_url = models.CharField(max_length=255,null=True,blank=True)
    # likes = models.ManyToManyField(User,related_name='blog_posts')
    print(user)
    def __str__(self):
        return str(self.user)
        
    
    def get_absolute_url(self):
        return reverse('home')
    


class Post(models.Model):
    title = models.CharField(max_length=255)
    # img = models.ImageField(upload_to='images',blank=True,null=True)
    # header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    # snippet = models.CharField(max_length=255)
    # category = models.CharField(max_length=255, default='codings')
    # post_time = models.DateTimeField(auto_created=True)
    # description = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str (self.author)

    def get_absolute_url(self):
        # return reverse("article-details", args=(str(self.id)))
        return reverse('home')
    
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s'%(self.post.title, self.name)


    
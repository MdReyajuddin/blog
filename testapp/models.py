from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('publish','Publish'))
    body=models.TextField()
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    title=models.CharField(max_length=264)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering =('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])



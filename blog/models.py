from django.db import models
from django.utils import timezone

'''defines model object that will be eventually added to database with
properties defined below as column headings.'''

class Post(models.Model):
    '''Define Post model'''
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #define a function to publish the post model with specific properties
        self.published_date = timezone.now()
        self.save()
    '''when this function is called, it will publish the post model with title.'''
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name = 'comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

def approved_comments(self):
    return self.comments.filter(approved_comment = True)

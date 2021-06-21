from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=255, verbose_name='Title of Your Post')
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    content = models.TextField(verbose_name='Write your content Here')
    blog_image = models.ImageField(verbose_name='Image', upload_to='blog_images')
    publish_time = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class comment(models.Model):
    blog_comment = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment_content = models.TextField(verbose_name="Comment Here")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return slef.comment_content


class like(models.Model):
    blog_like = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_likes")
    user_like = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    
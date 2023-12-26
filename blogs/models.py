from django.db import models
class Blog(models.Model):
    blog_title=models.CharField(max_length=50)
    blog_image=models.ImageField(max_length=50)
    blog_Desc=models.TextField()
    publish_date=models.DateField()
    like_count=models.IntegerField()


class Comment(models.Model):
    blog_comment=models.TextField()
    blog_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.

from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length = 50 ,primary_key=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = 'Categories'
    
    def __str__(self):
        return self.category

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        db_table = 'Posts'
        ordering = ('created_date',)

    def __str__(self):
        return self.title
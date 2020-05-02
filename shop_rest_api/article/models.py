from django.db import models
from django.contrib.auth.models import User
import time
def upload(instance, filename):
    lastDot = filename.rfind('.')
    extension= filename[lastDot:len(filename):1]
    return 'images/products/%s-%s%s' % (instance.title, time.time(), extension)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    sale = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to=upload, blank=True, null=True)
   
class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
   


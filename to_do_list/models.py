from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length = 40)
    slug= models.CharField(max_length= 64,default=None)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length = 65)
    description = models.CharField(max_length = 100)
    author = author = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)
    priority = models.CharField(max_length = 15)
    marked_done = models.BooleanField()
    def __str__(self):
        return self.title

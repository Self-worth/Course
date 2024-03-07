from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BaseModel (models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course (BaseModel):
    name = models.CharField(max_length=255)
    decription =RichTextField(null=True)
    image = models.ImageField(upload_to='courseappp/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return  self.name

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField(null=True)
    image = models.ImageField(upload_to='courseappp/%Y/%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return  self.name
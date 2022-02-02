from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    text = models.TextField(verbose_name='Текст поста')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Categories", blank=True)

    

class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=150, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    




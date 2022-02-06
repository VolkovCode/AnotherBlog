from django.db import models
from django.contrib.auth import get_user_model
from transliterate import slugify

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    title = models.CharField(max_length=50, verbose_name="Заголовок статьи")
    slug = models.SlugField(max_length=50, editable=False)
    text = models.TextField(verbose_name='Текст поста')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField("Categories", blank=True, related_name='categories')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
  

class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=150, verbose_name='Описание категории')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, related_name='comments')

#class Subscribe(models.Model):
 #   follower = models.ForeignKey(User, on_delete=models.CASCADE)

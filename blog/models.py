from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(unique=True, max_length=200)
    is_publish = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('-name',)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ('-name',)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    

    #content = models.TextField()
    content_preview = RichTextField()
    content = RichTextField()
    
    created_date = models.DateTimeField(
            default=timezone.now)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

    is_publish = models.BooleanField(default=False)


    # изображения превью
    preview_image = models.ImageField()
    category = models.ForeignKey(Category, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name='posts')

    # колличество просмотров страницы
    number_views = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-published_date',)

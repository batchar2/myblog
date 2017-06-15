from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField

from django.core.urlresolvers import reverse

from PIL import Image


class SitePage(models.Model):
    class Meta:
        verbose_name = 'Страница сайта'
        verbose_name_plural = 'Страницы сайта'
        ordering = ('-name',)


    name = models.CharField(max_length=100, default='')
    url = models.CharField(max_length=100, default='')

    content = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    number_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/' + self.url


class Tag(models.Model):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('-name',)
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(unique=True, max_length=200)
    is_publish = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name




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
    meta_kayword = models.CharField(u'Ключевые слова', default='', max_length=200)
    meta_description = models.CharField(u'Описание статьи для поисковика', default='', max_length=200)

    content_preview = RichTextField()
    content = RichTextField()

    #content_preview = HTMLField()
    #content = HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    is_publish = models.BooleanField(default=False)

    # изображения превью
    preview_image = models.ImageField()
    category = models.ForeignKey(Category, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name='posts')

    # колличество просмотров страницы
    number_views = models.PositiveIntegerField(default=0)

    allow_comments = models.BooleanField('allow comments', default=True)

    def save(self):
        if not self.id and not self.preview_image:
            return

        super(Post, self).save()

        image = Image.open(self.preview_image)
        (width, height) = image.size

        size = (200, 200)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.preview_image.path)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    #def get_absolute_url(self):
    #    return "/blog/{0}/".format(self.slug)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-published_date',)


    def url(self):
        return 'uploads' + self.preview_image

from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify


# TODO from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"

    first_name = models.CharField('Імʼя автора', max_length=100, null=True)
    last_name = models.CharField('Призвище автора', max_length=100, null=True)
    email = models.EmailField('Email автора', max_length=50, null=True)
    age = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name} {self.last_name}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subscriber(models.Model):
    class Meta:
        verbose_name = "Підписник"
        verbose_name_plural = "Підписники"

    name = models.CharField('Імʼя автора', max_length=100, null=True)
    email_to = models.EmailField("Email підписника")
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.email_to


# TODO: likes for Article
# TODO: Comments for Article
class Article(models.Model):
    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"

    title = models.CharField('Заголовок', max_length=150)
    description = models.CharField('Короткий опис', max_length=250)
    content = models.TextField('Текст')
    slug = models.SlugField(unique=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    name = models.CharField('Назва категорії', max_length=250)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField('Назва книги', max_length=250)
    author = models.ForeignKey(Author, models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, models.CASCADE, related_name='books', null=True, blank=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    class Meta:
        verbose_name = "Звернення"
        verbose_name_plural = "Звернення"

    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return f'{self.email} - {self.subject}'

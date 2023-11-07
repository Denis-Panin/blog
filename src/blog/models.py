from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField('Имя автора', max_length=100, null=True)
    email = models.EmailField('Email автора', max_length=50, null=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

    email_to = models.EmailField("Email подписчика")
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.email_to


class Post(models.Model):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    title = models.CharField('Заголовок', max_length=150)
    description = models.CharField('Краткое описание', max_length=250)
    content = models.TextField('Статья')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField('Название категории', max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField('Название книги', max_length=250)
    author = models.ForeignKey(Author, models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, models.CASCADE, related_name='books', null=True, blank=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.email

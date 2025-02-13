# Generated by Django 4.1.3 on 2023-11-22 12:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('first_name', models.CharField(
                    max_length=100,
                    null=True,
                    verbose_name='Імʼя автора'
                    )
                 ),
                ('last_name', models.CharField(
                    max_length=100,
                    null=True,
                    verbose_name='Призвище автора'
                    )
                 ),
                ('email', models.EmailField(
                    max_length=50,
                    null=True,
                    verbose_name='Email автора'
                    )
                 ),
                ('age', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автори',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('name', models.CharField(
                    max_length=250,
                    verbose_name='Назва категорії'
                    )
                 ),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False, verbose_name='ID'
                     )
                 ),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Звернення',
                'verbose_name_plural': 'Звернення',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('name', models.CharField(
                    max_length=100,
                    null=True,
                    verbose_name='Імʼя автора'
                    )
                 ),
                ('email_to', models.EmailField(
                    max_length=254,
                    verbose_name='Email підписника'
                    )
                 ),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now
                    )
                 ),
                ('author_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='blog.author'
                    )
                 ),
            ],
            options={
                'verbose_name': 'Підписник',
                'verbose_name_plural': 'Підписники',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('title', models.CharField(
                    max_length=250,
                    verbose_name='Назва книги'
                    )
                 ),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='books',
                    to='blog.author'
                    )
                 ),
                ('category', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='books',
                    to='blog.category'
                    )
                 ),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                 ),
                ('title', models.CharField(
                    max_length=150,
                    verbose_name='Заголовок'
                    )
                 ),
                ('description', models.CharField(
                    max_length=250,
                    verbose_name='Короткий опис'
                    )
                 ),
                ('content', models.TextField(verbose_name='Текст')),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now
                    )
                 ),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='blog.author'
                    )
                 ),
            ],
            options={
                'verbose_name': 'Стаття',
                'verbose_name_plural': 'Статті',
            },
        ),
    ]

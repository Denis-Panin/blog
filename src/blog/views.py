import csv

from django.utils import timezone
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from django_filters.views import FilterView
from django.http import Http404
from django.contrib import messages
from .filrers import BookFilter, ArticleFilter
from .forms import ArticleForm, SubscriberForm

from .models import Author, Book, Category, ContactUs, Article, Subscriber


def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_create.html', {'form': form})


def show_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/article_show.html', {"title": article.title, "article": article})


def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_update.html', {'form': form})


def delete_article(request, slug):
    get_object_or_404(Article, slug=slug).delete()
    return redirect('article_list')


class ArticleListView(FilterView):
    # queryset = Post.objects.all()
    filterset_class = ArticleFilter

    # paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # code for searching posts
        context['get_params'] = '&'.join(
            f'{key}={val}'
            for key, val in self.request.GET.items() if key != 'page'
        )
        context['cnt'] = context['object_list'].count()
        context['title'] = 'Усі пости'
        return context

    template_name = 'blog/articles_list.html'


def get_subscribers(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'blog/subscribers.html', {"title": "Subscribers", "subscribers": subscribers})


def add_subscriber(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        email_to = request.POST.get('email_to')
        if form.is_valid():
            if Subscriber.objects.filter(email_to=email_to).exists():
                return HttpResponse('Subscriber already exists with this email')
            form.save()
            return redirect('subscribers')
    else:
        form = SubscriberForm()
    return render(request, 'blog/subscribe_add.html', {'form': form})


def get_authors(request):
    authors = Author.objects.all().prefetch_related('books')
    return render(request, 'blog/authors.html', {"title": "Authors", "authors": authors})


def delete_author(request, slug):
    get_object_or_404(Author, slug=slug).delete()
    return redirect('authors_all')


def get_categories(request):
    categories = Category.objects.all().only('name')
    return render(request, 'blog/categories.html', {"title": "Categories", "categories": categories})


class BooksListView(FilterView):
    queryset = Book.objects.all()
    filterset_class = BookFilter

    # paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['get_params'] = '&'.join(
            f'{key}={val}'
            for key, val in self.request.GET.items()
            if key != 'page'
        )
        context['cnt'] = context['object_list'].count()
        context['title'] = 'Все книги'
        return context

    template_name = 'blog/book_list.html'


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'blog/contact-us-list.html'


class ContactUsView(CreateView):
    success_url = reverse_lazy('contact-us-list')
    model = ContactUs
    fields = ('email', 'subject', 'message')

# def display_attr(obj, atrr: str):
#     get_display = f'get_{atrr}_display'
#     if hasattr(obj, get_display):
#         return getattr(obj, get_display)()
#     return getattr(obj, atrr)
#
#
# class PostXLSX(View):
#     headers = ['title']
#     filename = 'posts_all_list.xlsx'
#
#
# def get(self, request, *args, **kwargs):
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#         headers={'Content-Disposition': f'attachment; filename="{self.filename}"'},
#     )
#     writer = csv.writer(response)
#     writer.writerow(self.headers)
#     for post in Post.objects.all().iterator():
#         writer.writerow([display_attr(post, header) for header in self.headers])
#     return response

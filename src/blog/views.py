from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_filters.views import FilterView
from .filrers import BookFilter, ArticleFilter
from .forms import ArticleForm
from .models import Author, Book, ContactUs, Article
from .helpers import get_new_articles, get_all_categories

articles = get_new_articles()
categories = get_all_categories()


def home_page(request):
    return render(request, 'blog/home_page.html', {'articles': articles, "categories": categories})


def about_us(request):
    return render(request, 'blog/about_us.html', {'articles': articles, "categories": categories})


def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')
    else:
        form = ArticleForm()
    context = {
        'form': form,
        "articles": articles,
        "categories": categories
    }
    return render(request, 'blog/article_create.html', context=context)


def show_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        "title": article.title,
        "article": article,
        "articles": articles,
        "categories": categories
    }
    return render(request, 'blog/article_show.html', context=context)


def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        "articles": articles,
        "categories": categories
    }
    return render(request, 'blog/article_update.html', context=context)


def delete_article(request, slug):
    get_object_or_404(Article, slug=slug).delete()
    return redirect('blog:article_list')


class ArticleListView(FilterView):
    filterset_class = ArticleFilter

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # code for searching posts
        context['get_params'] = '&'.join(
            f'{key}={val}'
            for key, val in self.request.GET.items() if key != 'page'
        )
        context['cnt'] = context['object_list'].count()
        context['title'] = 'Усі пости'
        context['articles'] = articles
        context['categories'] = categories
        return context

    template_name = 'blog/articles_list.html'


def get_authors(request):
    authors = Author.objects.all().prefetch_related('books')
    context = {
        "title": "Authors",
        "authors": authors,
        "articles": articles,
        "categories": categories
    }
    return render(request, 'blog/authors.html', context=context)


def delete_author(request, slug):
    get_object_or_404(Author, slug=slug).delete()
    return redirect('blog:authors_all')


# def get_categories(request):
#     categories = Category.objects.all().only('name')
#     return render(request, 'blog/categories.html', {"title": "Categories", "categories": categories})


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
        context['articles'] = articles
        context['categories'] = categories
        return context

    template_name = 'blog/book_list.html'


class ContactUsView(CreateView):
    success_url = reverse_lazy('blog:home_page')
    model = ContactUs
    fields = ('name', 'email', 'subject', 'message')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = articles
        context['categories'] = categories
        return context

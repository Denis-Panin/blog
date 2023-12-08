from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_filters.views import FilterView

from .filrers import ArticleFilter, BookFilter
from .forms import ArticleForm, CommentForm
from .helpers import get_all_categories, get_new_articles, get_top_authors
from .models import Article, Author, Book, Category, ContactUs

articles = get_new_articles()
categories = get_all_categories()


def home_page(request):
    top_authors = get_top_authors()
    context = {
        'articles': articles,
        'categories': categories,
        'top_authors': top_authors
    }
    return render(request, 'blog/home_page.html', context=context)


def about_us(request):
    return render(
        request,
        'blog/about_us.html',
        {'articles': articles,
         'categories': categories}
    )


@login_required(login_url='account:login')
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')
    else:
        form = ArticleForm()
    context = {
        'form': form,
        'articles': articles,
        'categories': categories
    }
    return render(
        request,
        'blog/article/article_create.html',
        context=context
    )


def show_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'title': article.title,
        'article': article,
        'articles': articles,
        'categories': categories
    }
    return render(
        request,
        'blog/article/article_show.html',
        context=context
    )


def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:article_list')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'articles': articles,
        'categories': categories
    }
    return render(
        request,
        'blog/article/article_update.html',
        context=context
    )


def delete_article(request, slug):
    get_object_or_404(Article, slug=slug).delete()
    return redirect('blog:article_list')


def article_category(request, slug):
    articles_categories = Article.objects.filter(
        category__slug=slug
    ).order_by('-created')
    category_name = Category.objects.get(slug=slug).name
    cnt = articles_categories.count()
    context = {
        'articles_category': articles_categories,
        'articles': articles,
        'categories': categories,
        'cnt': cnt,
        'category_name': category_name,
    }
    return render(
        request,
        'blog/article/articles_list_categories.html',
        context=context
    )


class ArticleListView(FilterView):
    filterset_class = ArticleFilter

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # code for searching articles
        context['get_params'] = '&'.join(
            f'{key}={val}'
            for key, val in self.request.GET.items() if key != 'page'
        )
        # code for searching articles
        context['cnt'] = context['object_list'].count()
        context['title'] = 'Articles'
        context['articles'] = articles
        context['categories'] = categories
        return context

    template_name = 'blog/article/articles_list.html'


@login_required(login_url='account:login')
def add_comment_to_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('blog:article_show', slug=slug)
    else:
        form = CommentForm()
    context = {
        'form': form,
        'article': article,
        'articles': articles,
        'categories': categories
    }
    return render(
        request,
        'blog/add_comment_to_article.html',
        context=context
    )


def get_authors(request):
    authors = Author.objects.all().prefetch_related('articles').order_by(
        'first_name'
    )
    context = {
        'title': 'Authors',
        'authors': authors,
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/author/authors.html', context=context)


def get_author(request, slug):
    author = get_object_or_404(Author, slug=slug)
    articles_ = Article.objects.filter(author=author.id)
    context = {
        'author': author,
        'articles_': articles_,
        'cnt': articles_.count(),
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/author/author.html', context=context)


def delete_author(request, slug):
    get_object_or_404(Author, slug=slug).delete()
    return redirect('blog:authors_all')


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

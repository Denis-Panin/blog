import csv

from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from django_filters.views import FilterView
from django.http import Http404
from django.contrib import messages
from .filrers import BookFilter, PostFilter
from .forms import PostForm, SubscriberForm

from .models import Author, Book, Category, ContactUs, Post, Subscriber
from faker import Faker


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_show.html', {"title": post.title, "post": post})


def post_delete(request, post_id):
    get_object_or_404(Post, pk=post_id).delete()
    return redirect('posts_list')


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form})


def get_subscribers(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'blog/subscribers.html', {"title": "Subscribers", "subs": subscribers})


def subscriber_add(request):
    subscribe_success = False
    email_to = request.POST.get('email_to')
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                subscribe_success = True
                return redirect('subscribers')
            else:
                error = form.errors
        except ValidationError:
            error = 'Already subscribed'
    else:
        form = SubscriberForm()
    return render(request, 'blog/subscribe_add.html', {'form': form})


def authors_all(request):
    authors = Author.objects.all().prefetch_related('books')
    return render(request, 'blog/authors.html', {"title": "Authors", "authors": authors})


def author_delete(request, author_id):
    get_object_or_404(Author, id=author_id).delete()
    return render(request, 'blog/home_page.html')


def categories_all(request):
    categories = Category.objects.all().only('name')
    return render(request, 'blog/categories.html', {"title": "Categories", "categories": categories})


class BooksListView(FilterView):
    queryset = Book.objects.all()
    filterset_class = BookFilter
    # paginate_by = 10

    # def get_context_data(self, *args, **kwargs):
    #         context = super().get_context_data(*args, **kwargs)
    #         context['get_params'] = '&'.join(
    #             f'{key}={val}'
    #             for key, val in self.request.GET.items()
    #             if key != 'page'
    #         )
    #         context['cnt'] = context['object_list'].count()
    #         context['title'] = 'Все книги'
    #         return context

    template_name = 'blog/book_list.html'


class PostsListView(FilterView):
    queryset = Post.objects.all()
    filterset_class = PostFilter
    # paginate_by = 2

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['get_params'] = '&'.join(
    #         f'{key}={val}'
    #         for key, val in self.request.GET.items()
    #         if key != 'page'
    #     )
    #     context['cnt'] = context['object_list'].count()
    #     context['title'] = 'Все посты'
    #     return context
    template_name = 'blog/posts_filter.html'


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

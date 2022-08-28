from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.decorators import cache
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/sport_blog/static/assets/img/favicon/favicon.ico')),

    path('', TemplateView.as_view(template_name='sport_blog/home_page.html'), name='home_page'),
    path('about/', TemplateView.as_view(template_name='sport_blog/about.html'), name='about'),
    path('end/registration/',
         TemplateView.as_view(template_name='sport_blog/thanks_for_activation.html'),
         name='end_registration'),

    path('posts/list/', views.PostsListView.as_view(), name='posts_list'),
    path('posts/list/csv/', views.PostXLSX.as_view(), name='posts_list_csv'),
    path('posts/create/', views.post_create, name='posts_create'),
    path('post/<int:post_id>/', views.post_show, name='post_show'),
    path('post/update/<int:post_id>/', views.post_update, name='post_update'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),

    path('subscribers/', views.subscribers, name='subscribers'),
    path('subscriber/add/', views.subscriber_add, name='subscriber_add'),
    path('authors/new/', views.authors_new, name='authors_new'),
    path('authors/all/', cache.cache_page(60 * 2)(views.authors_all), name='authors_all'),
    path('author/delete/<int:author_id>/', views.author_delete, name='author_delete'),

    path('book/list/', views.BooksListView.as_view(), name='book_list'),
    path('categories/all/', views.categories_all, name='categories_all'),

    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/subscribe/', views.api_subscribe, name='api_subscribe'),
    path('api/authors/', views.api_authors, name='api_authors'),
    path('api/authors/new/', views.api_fake_authors, name='api_authors_new'),

    path('contact/us/create/', views.ContactUsView.as_view(), name='contact-us-create'),
    path('contact/us/list/', views.ContactUsListView.as_view(), name='contact-us-list'),

    path('api/v1/', include('api.urls')),

    path('posts_page/', TemplateView.as_view(template_name='sport_blog/posts_page.html'), name='posts_page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

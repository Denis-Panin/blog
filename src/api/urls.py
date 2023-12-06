from api.views import ArticleAPIViewSet, ArticleAPIViewSet2, AuthorAPIView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='articles', viewset=ArticleAPIViewSet,
                basename='article')

urlpatterns = [
    path('article2/', ArticleAPIViewSet2.as_view(), name='article2'),
    path('author/', AuthorAPIView.as_view(), name='author')
]
urlpatterns.extend(router.urls)

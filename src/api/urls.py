from api.views import AuthorAPIView, PostAPIViewSet, PostAPIViewSet2
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='articles', viewset=PostAPIViewSet, basename='article')

urlpatterns = [
    path('post2/', PostAPIViewSet2.as_view(), name='post2'),
    path('author/', AuthorAPIView.as_view(), name='author')
]
urlpatterns.extend(router.urls)

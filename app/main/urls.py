from rest_framework import routers

from main import views

router = routers.SimpleRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'comments', views.PostViewSet, basename='comments')
router.register(r'tags', views.TagViewSet, basename='tags')

urlpatterns = router.urls

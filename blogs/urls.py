from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('blog_posts', views.PostViewSet)
router.register('blog_posts', views.PostDetailsViewSet)

router.register('comments', views.CommentViewSet)
router.register('comments', views.CommentDetailsViewSet)

router.register('categories', views.CategoryViewSet)
router.register('categories', views.CategoryDetailsViewSet)


# URLConf
urlpatterns = router.urls

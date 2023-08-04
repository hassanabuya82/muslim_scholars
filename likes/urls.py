from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('like', views.LikeViewSet)
router.register('like', views.LikeDetailsViewSet)



# URLConf
urlpatterns = router.urls
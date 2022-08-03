from rest_framework.routers import DefaultRouter
from . import views

app_name = "toilet"
router = DefaultRouter()
router.register("", views.ToiletViewSet)

urlpatterns = router.urls
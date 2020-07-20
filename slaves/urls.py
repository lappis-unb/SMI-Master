from .views import SubordinateViewSet

from rest_framework import routers


app_name = "subordinates"

router = routers.DefaultRouter()
router.register(r'subordinates', SubordinateViewSet)

urlpatterns = []

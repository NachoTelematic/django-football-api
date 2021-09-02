from rest_framework import routers
from .views import LeagueViewSet

router = routers.DefaultRouter()
router.register(r'leagues', LeagueViewSet)

urlpatterns = router.urls

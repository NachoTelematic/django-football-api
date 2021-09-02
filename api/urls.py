from rest_framework import routers
from .views import LeagueViewSet, TeamViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register(r'leagues', LeagueViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = router.urls

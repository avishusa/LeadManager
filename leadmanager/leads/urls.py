from rest_framework import routers
from .api import LeadviewSet

router = routers.DefaultRouter()
router.register('api/leads',LeadviewSet,'leads')

urlpatterns = router.urls
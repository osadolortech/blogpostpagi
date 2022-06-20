from rest_framework import routers
from .views import BlogApi


router = routers.DefaultRouter()
router.register('blogpost',BlogApi)

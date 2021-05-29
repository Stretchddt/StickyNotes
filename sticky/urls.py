from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StickNoteViewSet

router = DefaultRouter()
router.register('sticky-notes', StickNoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AuthorViewSet,
    BookViewSet,
    ChapterViewSet,
    ProblemViewSet,
    SectionViewSet,
)

router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)
router.register(r"chapters", ChapterViewSet)
router.register(r"sections", SectionViewSet)
router.register(r"problems", ProblemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

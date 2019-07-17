
from .views import PersonalViewSet,SimpleApiView
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'', PersonalViewSet, basename='Personal')


from .views import (
    PersonalListView, 
    PersonalRetrieveView, 
    PersonalCreateView, 
    PersonalDestroyView,
    PersonalUpdateView
)

urlpatterns = [
    path('all/',include(router.urls)),
    path('',PersonalListView.as_view()),
    path('create/',PersonalCreateView.as_view()),
    path('<pk>/',PersonalRetrieveView.as_view()),
    path('<pk>/update/',PersonalUpdateView.as_view()),
    path('<pk>/delete/',PersonalDestroyView.as_view()),
    path('encode/', SimpleApiView.as_view()),
]

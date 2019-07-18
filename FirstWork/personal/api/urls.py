
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register(r'all', PersonalViewSet )



from .views import *

urlpatterns = [
    path('',include(router.urls)),
    path('encode/', SimpleApiView.as_view()),
]

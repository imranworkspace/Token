from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from viewset_api import views


router=DefaultRouter()

router.register('studentapi',views.StudentModelViewset,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]

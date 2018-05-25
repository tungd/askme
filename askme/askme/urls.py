import asking.views as asking_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:slug>', asking_views.ProfileView.as_view(),
         name='profile'),
    path('', asking_views.IndexView.as_view(), name='index')
]

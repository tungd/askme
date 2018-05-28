import asking.views as asking_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         asking_views.IndexView.as_view(),
         name='index'),
    path('questions/<int:pk>',
         asking_views.UpdateQuestionView.as_view(),
         name='answer'),
    path('questions',
         asking_views.CreateQuestionView.as_view(),
         name='ask'),
    path('<str:slug>',
         asking_views.ProfileView.as_view(),
         name='profile'),
]

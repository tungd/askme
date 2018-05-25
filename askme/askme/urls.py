import asking.views as asking_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asking_views.IndexView.as_view())
]

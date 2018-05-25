from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, ListView

from . import models


class IndexView(LoginView, ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return self.request.user.questions.filter(answer='').all()


class ProfileView(DetailView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'profile.html'

from django.contrib.auth.views import LoginView
from django.views.generic import ListView

from . import models


class IndexView(LoginView, ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return self.request.user.questions.filter(answer='').all()

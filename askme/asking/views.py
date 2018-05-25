from django.views.generic import ListView

from . import models


class IndexView(ListView):
    template_name = 'index.html'
    queryset = models.Question.objects.all()

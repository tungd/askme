from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView

from . import forms


class IndexView(LoginView, ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return self.request.user.questions.filter(answer='').all()


class ProfileView(DetailView, FormView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'profile.html'
    form_class = forms.QuestionForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['questions'] = self.get_object().questions.exclude(answer=None)
        return context

    def get_success_url(self):
        return reverse('profile', args=[self.kwargs['slug']])

    def form_valid(self, form):
        username = self.kwargs['slug']
        answerer = self.model.objects.get(username=username)
        form.instance.answerer = answerer
        form.save()
        return super().form_valid(form)

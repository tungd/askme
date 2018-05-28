from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView

from . import forms, models


class IndexView(LoginView, ListView):
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return user.questions.all()


class UpdateQuestionView(UpdateView):
    model = models.Question
    fields = ['answer']
    success_url = reverse_lazy('index')


class CreateQuestionView(CreateView):
    model = models.Question
    fields = ['name', 'text']

    def get_success_url(self):
        return reverse('profile', args=[
            self.object.answerer.username
        ])

    def form_valid(self, form):
        form.instance.answerer_id = self.request.POST.get('answerer_id')
        form.save()
        return super().form_valid(form)


class ProfileView(DetailView, FormView):
    model = get_user_model()
    slug_field = 'username'
    template_name = 'profile.html'
    form_class = forms.QuestionForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['questions'] = self.get_object().questions.exclude(answer='')
        return context

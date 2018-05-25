from askme.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Question(BaseModel):
    name = models.CharField(_('Name of asker'), max_length=255)
    text = models.TextField(_('Question'))

    answerer = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text

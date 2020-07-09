from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile'
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfis")

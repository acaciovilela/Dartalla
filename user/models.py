from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to="user/profile/picture", null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile'
        verbose_name = _("Profile")

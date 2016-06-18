from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings


# User = get_user_model()



class Profile(models.Model):
    _genders = (
        ('M', 'Male', ),
        ('F', 'Female', ),
    )
    # user = models.OneToOneField(User)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=1, choices=_genders)


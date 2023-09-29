from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from apps.users.managers import CustomeUserManager
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)  # is_staff and is_active are needed while overriding the user class
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'  # we are treating email as username

    # we can also have REQUIRED_FIELD to be set while creating
    # superuser such that those field cannot be empty, for now we are leaving as empty as full name is not compulsion
    REQUIRED_FIELDS = []
    objects = CustomeUserManager()

    def __str__(self):
        # send the string form of object
        return self.email

    def clean(self) -> None:
        # chekcing if full name character is less than three
        if len(self.fullname) < 3:
            raise ValidationError({'fullname': 'Full name cannont be less than three character'})

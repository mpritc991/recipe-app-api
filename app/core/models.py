"""
Django models for the core application."""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
# Create your models here.

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a regular user with the given email and password."""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

#    def create_superuser(self, email, password):
#        """Create and save a superuser with the given email and password."""
#        user = self.create_user(email, password)
#        user.is_staff = True
#        user.is_superuser = True
#        user.save(using=self._db)

#        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username."""
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'

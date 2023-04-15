from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager,
                                        PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, username=None, is_simplified=False, *args, **kwargs):

        if email is None:
            raise TypeError('Obrigatório informar o  Email')

        user = self.model(
            username=self.normalize_email(email) if not username else username,
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name', ""),
            last_name=kwargs.get('last_name', ""),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password, username)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractUser, PermissionsMixin):

    username = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = ('Usuário')
        verbose_name_plural = ('Usuários')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'
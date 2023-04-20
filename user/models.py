from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager,
                                        PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, username=None, is_simplified=False, *args, **kwargs):

        if email is None:
            raise TypeError('Obrigatório informar o  Email')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        
        username = None

        user = self.create_user(email, password, username)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractUser, PermissionsMixin):

    #simplify user model
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('Usuário')
        verbose_name_plural = ('Usuários')

    def __str__(self):
        return f'{self.email}'
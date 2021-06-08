from datetime import time
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.deletion import CASCADE
from django.utils import timezone
import pytz


class UserManager(BaseUserManager):
    def create_user(self, username, password):
        '''
        Crea un nuevo usuario.
        '''
        fields = ('username', 'password',)
        for field in fields:
            if not field:
                raise ValueError(f'El usuario tiene que tener un {field}.')

        user = self.model(username=username, password=password)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        '''
        Crea un nuevo superusuario.
        '''
        user = self.create_user(username=username, password=password)

        user.is_admin = True
        user.save(using=self._db)

        return user


class UserModel(AbstractBaseUser):
    '''
    User model.
    '''
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('password',)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        bs_tz = pytz.timezone('America/Buenos_Aires')
        timezone.activate(bs_tz)
        if not self.id:
            self.created_on = timezone.localtime(timezone.now())
        self.updated_on = timezone.localtime(timezone.now())
        return super(UserModel, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class TuitModel(models.Model):
    '''
    Tuit Model.
    '''
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=280)
    author = models.ForeignKey(UserModel, related_name='tuits', on_delete=CASCADE)
    created_on = models.DateTimeField()

    def save(self, *args, **kwargs):
        bs_tz = pytz.timezone('America/Buenos_Aires')
        timezone.activate(bs_tz)
        if not self.id:
            self.created_on = timezone.localtime(timezone.now())
        return super(TuitModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.content[:10]

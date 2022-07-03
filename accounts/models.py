from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not nickname:
            raise ValueError("Users must have an nickname")
            
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth = date_of_birth,
            nickname = nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, nickname, password):
        user = self.create_user(
            email,
            nickname = nickname,
            password = password,
            date_of_birth = date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email',
        max_length=255,
        unique=True,
    )

    nickname = models.CharField(
        max_length = 20,
        null = False,
        unique = True,
    )

    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['date_of_birth', 'email']

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

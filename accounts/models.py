from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    # use_in_migrations = True

    def create_user(self,uid, password, **extra_fields):
        """
        Create and save a User with the given uid and password.
        """
        if not uid:
            raise ValueError("The UID must be set")
        user = self.model(uid=uid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, uid, password, **extra_fields):
        """
        Create and save a Superuser with the given uid and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser = True")
        if extra_fields.get('is_admin') is not True:
            raise ValueError("Superuser must have is_admin = True")
        return self.create_user(uid, password,**extra_fields)


class User(AbstractBaseUser):
    uid = models.CharField(unique=True,max_length=20)
    password = models.CharField(max_length=100,null=True)
    # flag = models.IntegerField()
    ROLE_TYPES = (
        (0, 'ADMIN'),
        (1, 'TEACHER'),
        (2, 'STUDENT'),
    )
    role = models.IntegerField(choices=ROLE_TYPES,null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = UserManager()

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['password']
    class Meta:
        app_label = "accounts"
        db_table = "User"
    
    def __str__(self):
        return str(self.uid)

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return self.is_staff

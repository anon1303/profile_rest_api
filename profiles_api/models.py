from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manage user profiles"""

    def create_user(self, email, mobile, first_name, last_name, password=None):
        if not email:
            raise ValueError('Required Email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, mobile=mobile,first_name=first_name, last_name=last_name,)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, mobile,first_name, last_name, password):
        """Create and save new superuser with given details"""
        user = self.create_user(email, mobile, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system""" 
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile', 'first_name', 'last_name']

    def get_name(self):
        """GET FULLNAME OF THE USER"""
        fullname = self.first_name +' '+ self.last_name
        return fullname
    
    def get_user_fname(self):
        return self.first_name
    
    def __str__(self):
        """Return the string representation of the user"""
        return self.email
    


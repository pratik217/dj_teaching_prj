from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have email address")

        email= self.normalize_email(email)
        user= self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Create a super user"""
        user=self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)

    objects =UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

class StudentItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    admission_date = models.DateTimeField(auto_now_add=True)
    picture= models.FileField(upload_to='documents/',default=True)
    standard = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    reg_no= models.CharField(max_length=100)
    gender=models.CharField(max_length=15)

    def __str__(self):
        """Return the model as a string"""
        return self.name
class TeacherItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    joining_date = models.DateTimeField(auto_now_add=True)
    designation = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    age =models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    reg_no= models.CharField(max_length=100)
    gender=models.CharField(max_length=15)

    def __str__(self):
        """Return the model as a string"""
        return self.name
class StaffItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    joining_date = models.DateTimeField(auto_now_add=True)
    scale = models.CharField(max_length=100)
    pay = models.CharField(max_length=100)
    age =models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    reg_no= models.CharField(max_length=100)
    gender=models.CharField(max_length=15)


    def __str__(self):
        """Return the model as a string"""
        return self.name

# Create your models here.

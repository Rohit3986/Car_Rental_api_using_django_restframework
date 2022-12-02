from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, user_type, password=None,password2=None):

        if not username:
            raise ValueError('User must have username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, user_type, password=None, password2=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            user_type=user_type
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True)
    username = models.CharField(max_length=30,unique=True)
    user_type = models.CharField(choices=(('1','Owner'),('2','renter')),default="1",max_length=7)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','user_type']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class LoginLogs(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.DO_NOTHING)
    user_type=models.CharField(max_length=7,choices=(("1","owner"),("2","rental")),default="1")
    login_at=models.DateTimeField(auto_now_add=True)

class Car(models.Model):
    car_model=models.CharField(max_length=30)
    colour=models.CharField(max_length=20)
    fuel_type=models.CharField(max_length=4,choices=(("1","petrol"),("2","diesel"),("3","cng"),("4","bio-diesel")))
    car_images=models.FileField(upload_to="E:\pythonproject\django\django rest framework\VehicleRentalApi\cars",blank=True)
    price_per_hour=models.IntegerField()
    is_available=models.BooleanField()
    owner=models.ForeignKey(default=1,to=User,on_delete=models.CASCADE)
    def __str__(self):
        return self.car_model

class BookingRequest(models.Model):
    requested_by=models.ForeignKey(to=User,on_delete=models.DO_NOTHING,related_name="renter")
    requested_to=models.ForeignKey(to=User,on_delete=models.DO_NOTHING,related_name="owner")
    requested_for=models.ForeignKey(to=Car,on_delete=models.DO_NOTHING)
    request_status=models.CharField(max_length=10,choices=(("1","pending"),("2","not approved"),("3","approved")),default="1")
    created_on=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now_add=True)



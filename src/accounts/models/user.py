from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.models.user_manager import UserManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


class User(AbstractUser):
    PHONE_REGEX = RegexValidator(
        regex=r"^09\d{9}",
        message="{}\n{}".format(
            _("Phone number must be entered in the format: '09999999999'."),
            _("Up to 11 digits allowed."),
        ),
    )
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    first_name = models.CharField(max_length=250,null=True,blank=True)
    last_name = models.CharField(max_length=250,null=True,blank=True)
    username = models.CharField(max_length=250,unique=True)
    email = models.EmailField(max_length=250,unique=True)
    phone_number = models.CharField(validators=[PHONE_REGEX],max_length=11,unique=True,null=True,blank=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    profile_picture = models.ImageField(default="user_img/default.png",upload_to="user_img",blank=True,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(blank=True,null=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    organisation = models.CharField(max_length=500,null=True,blank=True)
    state = models.CharField(max_length=250,null=True,blank=True)
    zip_code = models.CharField(max_length=250,null=True,blank=True)
    country = models.CharField(max_length=250,null=True,blank=True)
    language = models.CharField(max_length=250,null=True,blank=True)
    time_zone = models.CharField(max_length=250,null=True,blank=True)
    currency = models.CharField(max_length=250,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.email) +' | '+ str(self.first_name) +' '+ str(self.last_name)
    def is_profile_fill(self):
        if self.email is not None and self.username is not None and self.first_name is not None and self.last_name is not None:
            return True
        else:
            return False
    def img_tag(self):
        if self.profile_picture:
            return mark_safe('<img src="{}" height="20"/>'.format(self.profile_picture.url))
    img_tag.short_description = 'profile'



class Plan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    days = models.IntegerField(default=0)
    tokens = models.IntegerField(default=0)
    emails = models.IntegerField(default=0)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.user) + ' | days: '+ str(self.days) + ' | tokens: '+ str(self.tokens)
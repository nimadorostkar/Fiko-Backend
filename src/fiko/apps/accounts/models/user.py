from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from fiko.apps.accounts.models.user_manager import UserManager

class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^09\d{9}",
        message="{}\n{}".format(
            _("Phone number must be entered in the format: '09999999999'."),
            _("Up to 11 digits allowed."),
        ),
    )
    username = None
    email = None
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex],max_length=11,unique=True)
    birth_date = models.DateField(null=True,blank=True)
    invite_code = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default="audingo_user_image/default.png", upload_to="audingo_user_image", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = None
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.phone_number) +' | '+ str(self.first_name) +' | '+ str(self.last_name)

    def is_profile_fill(self):
        if self.first_name is not None and self.last_name is not None:
            return True
        else:
            return False
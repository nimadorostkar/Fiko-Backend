from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import User


class TelegramChannel(models.Model):
    is_connect = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bot_token = models.CharField(max_length=200,unique=True)
    bot_username = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.bot_username)





class SingletonModel(models.Model):
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError('There can be only one instance of this model.')
        return super(SingletonModel, self).save(*args, **kwargs)


class Settings(SingletonModel):
    IR_yearly = models.IntegerField(default=0)
    IR_monthly = models.IntegerField(default=0)
    TR_yearly = models.IntegerField(default=0)
    TR_monthly = models.IntegerField(default=0)
    EN_yearly = models.IntegerField(default=0)
    EN_monthly = models.IntegerField(default=0)
    token1M = models.IntegerField(default=0)
    token3M = models.IntegerField(default=0)
    token5M = models.IntegerField(default=0)
    token10M = models.IntegerField(default=0)
    email1K = models.IntegerField(default=0)
    email3K = models.IntegerField(default=0)
    email5K = models.IntegerField(default=0)
    email10K = models.IntegerField(default=0)

    def __str__(self):
        return str(self.IR_yearly) + " | " + str(self.IR_monthly) + " | " + str(self.EN_yearly) + " | " + str(self.EN_monthly)
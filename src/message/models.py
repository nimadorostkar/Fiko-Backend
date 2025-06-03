from django.db import models
import uuid
from accounts.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    SOURCE_CHOICES = [
        ('unknown', 'unknown'),
        ('telegram', 'telegram'),
        ('instagram', 'instagram'),
    ]
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000,null=True,blank=True)
    profile_picture = models.ImageField(default="customer_img/default.png", upload_to="customer_img", blank=True, null=True)
    tag = models.ManyToManyField(Tag, related_name='customers')
    source = models.CharField(max_length=90,choices=SOURCE_CHOICES,default='unknown')
    source_id = models.CharField(max_length=90,unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''} | {self.source}"



class Conversation(models.Model):
    STATUS_CHOICES = [
        ('active', 'active'),
        ('support_active', 'support_active'),
        ('marketing_active', 'marketing_active'),
        ('closed', 'closed'),
    ]
    SOURCE_CHOICES = [
        ('unknown', 'unknown'),
        ('telegram', 'telegram'),
        ('instagram', 'instagram'),
    ]
    title = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active')
    is_active = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    source = models.CharField(max_length=90,choices=SOURCE_CHOICES,default='unknown')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='conversations')
    priority = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation with {self.customer} by {self.user} (Status: {self.status})"



class Message(models.Model):
    TYPE_CHOICES = [
        ('customer', 'customer'),
        ('AI', 'AI'),
        ('support', 'support'),
        ('marketing', 'marketing'),
    ]
    type = models.CharField(max_length=60, choices=TYPE_CHOICES, default='customer')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField(max_length=1000)
    is_ai_response = models.BooleanField(default=False)
    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} | {self.content}"
# Generated by Django 5.2.1 on 2025-06-03 13:11

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('profile_picture', models.ImageField(blank=True, default='customer_img/default.png', null=True, upload_to='customer_img')),
                ('source', models.CharField(choices=[('unknown', 'unknown'), ('telegram', 'telegram'), ('instagram', 'instagram')], default='unknown', max_length=90)),
                ('source_id', models.CharField(blank=True, max_length=90, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('support_active', 'support_active'), ('marketing_active', 'marketing_active'), ('closed', 'closed')], default='active', max_length=60)),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('source', models.CharField(choices=[('unknown', 'unknown'), ('telegram', 'telegram'), ('instagram', 'instagram')], default='unknown', max_length=90)),
                ('priority', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='message.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('type', models.CharField(choices=[('customer', 'customer'), ('AI', 'AI'), ('support', 'support'), ('marketing', 'marketing')], default='customer', max_length=60)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=1000)),
                ('is_ai_response', models.BooleanField(default=False)),
                ('is_answered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='message.conversation')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='message.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='tag',
            field=models.ManyToManyField(related_name='customers', to='message.tag'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-05 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.BigIntegerField(unique=True, verbose_name='Telegram Chat Id')),
                ('username', models.CharField(unique=True, verbose_name='Telegram Username')),
                ('verification_code', models.CharField(max_length=16, verbose_name='Verification Code')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Telegram User',
                'verbose_name_plural': 'Telegram Users',
            },
        ),
    ]

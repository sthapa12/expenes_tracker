# Generated by Django 4.2.5 on 2023-09-16 15:49

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
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('YUAN', 'YUAN'), ('AUD', 'AUD')], default='USD', max_length=20, null=True)),
                ('amount', models.FloatField()),
                ('transaction_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('YUAN', 'YUAN'), ('AUD', 'AUD')], default='USD', max_length=20, null=True)),
                ('transaction_category', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('YUAN', 'YUAN'), ('AUD', 'AUD')], default='USD', max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

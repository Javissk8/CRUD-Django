# Generated by Django 2.1.3 on 2018-12-01 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('business', '0002_auto_20181128_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Business')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('phone_number', models.CharField(max_length=45)),
                ('birthday', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
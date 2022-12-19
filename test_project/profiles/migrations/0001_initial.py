# Generated by Django 4.1.4 on 2022-12-10 12:27

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=20)),
                ('jobtitle', models.CharField(max_length=20)),
                ('lastlogin', models.DateTimeField(auto_now=True)),
                ('loggedIn', models.BooleanField(default=False)),
                ('dateformat', models.CharField(default='Y-M-D h:m:s', max_length=20)),
                ('picture', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
<<<<<<< HEAD
# Generated by Django 3.2.13 on 2022-08-16 22:50
=======
# Generated by Django 3.2.14 on 2022-08-22 07:34
>>>>>>> cce6dda622ac49ffca6c75bd728a20c71d57f42d

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
            name='ResetPasswordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resetuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
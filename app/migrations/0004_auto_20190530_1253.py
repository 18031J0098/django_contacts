# Generated by Django 2.2.1 on 2019-05-30 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20190529_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='contact',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.2 on 2020-12-11 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0019_db_project_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_step',
            name='public_header',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

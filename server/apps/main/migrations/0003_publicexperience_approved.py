# Generated by Django 2.2.3 on 2019-07-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_publicexperience_experience_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicexperience',
            name='approved',
            field=models.CharField(default='not reviewed', max_length=50),
        ),
    ]

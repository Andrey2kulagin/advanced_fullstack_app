# Generated by Django 4.1.7 on 2023-03-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_candidate_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='job',
            field=models.CharField(max_length=5, null=True),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-12 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('rates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingaverage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

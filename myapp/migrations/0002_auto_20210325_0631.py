# Generated by Django 3.1.7 on 2021-03-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='size',
        ),
        migrations.AddField(
            model_name='dog',
            name='breed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Walk',
        ),
    ]

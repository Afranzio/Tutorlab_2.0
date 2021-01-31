# Generated by Django 3.1.4 on 2021-01-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_auto_20210123_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Languages',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='seek_skills',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='teach_skills',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

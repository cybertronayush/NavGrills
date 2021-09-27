# Generated by Django 3.2.7 on 2021-09-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
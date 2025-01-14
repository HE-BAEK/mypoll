# Generated by Django 5.1.4 on 2025-01-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth",
            field=models.DateField(blank=True, null=True, verbose_name="생일"),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=50, verbose_name="이름"),
        ),
    ]

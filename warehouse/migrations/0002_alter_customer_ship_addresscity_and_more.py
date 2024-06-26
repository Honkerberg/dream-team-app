# Generated by Django 5.0.4 on 2024-05-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="Ship addresscity",
            field=models.CharField(blank=True, max_length=40, verbose_name="City"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="Ship addressnumber",
            field=models.IntegerField(blank=True, verbose_name="Number"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="Ship addresspostal_code",
            field=models.CharField(
                blank=True, max_length=6, verbose_name="Postal code"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="Ship addressstreet",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Ship address"
            ),
        ),
    ]

# Generated by Django 4.2.10 on 2024-03-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_anbar_akhal_id_alter_anbar_khamir_ghadim_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplier", name="username", field=models.TextField(blank=True),
        ),
    ]
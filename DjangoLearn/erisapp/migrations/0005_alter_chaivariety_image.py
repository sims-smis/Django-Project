# Generated by Django 4.2.17 on 2025-01-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erisapp', '0004_chaivariety_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaivariety',
            name='image',
            field=models.ImageField(default='adam-thomas-Ta1viaIDvIk-unsplash_JQsFeLm.jpg', upload_to='chais/'),
        ),
    ]
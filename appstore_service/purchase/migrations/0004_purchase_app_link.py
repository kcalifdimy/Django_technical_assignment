# Generated by Django 5.0.8 on 2024-08-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_alter_purchase_unique_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='app_link',
            field=models.URLField(max_length=300, null=True),
        ),
    ]

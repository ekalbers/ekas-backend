# Generated by Django 4.2.3 on 2023-08-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ek_drones', '0002_alter_inforequest_company_alter_inforequest_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inforequest',
            name='message',
            field=models.TextField(blank=True, default='None'),
        ),
        migrations.AlterField(
            model_name='inforequest',
            name='phone',
            field=models.CharField(blank=True, default='None', max_length=16),
        ),
    ]

# Generated by Django 3.0.3 on 2020-10-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20201016_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='adminresponse',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='adminstatus',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

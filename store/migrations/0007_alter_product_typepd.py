# Generated by Django 3.2.2 on 2021-05-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_shippingaddress_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='typePD',
            field=models.CharField(blank=True, choices=[('CPU', 'Cpu'), ('Mainboard', 'Mainboard'), ('RAM', 'Ram'), ('VGA', 'Vga'), ('PSU', 'Psu')], max_length=10),
        ),
    ]

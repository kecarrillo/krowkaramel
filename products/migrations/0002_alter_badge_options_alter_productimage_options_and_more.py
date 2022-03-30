# Generated by Django 4.0.3 on 2022-03-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='badge',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ('image',)},
        ),
        migrations.AlterField(
            model_name='product',
            name='promoted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
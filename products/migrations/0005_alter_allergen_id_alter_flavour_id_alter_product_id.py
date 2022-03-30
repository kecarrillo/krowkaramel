# Generated by Django 4.0.3 on 2022-03-30 13:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_allergen_id_alter_flavour_id_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergen',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a799b518-da23-49cc-b02b-eb3d3bb0fadd'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b48644d8-aaa5-4fce-8a43-9d7dd694deb0'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('5c69fcfb-3951-401c-b8b3-fe9e61f01531'), editable=False, primary_key=True, serialize=False),
        ),
    ]

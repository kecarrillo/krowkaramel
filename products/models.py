# products/models.py
import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone


# Create your models here.
class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Allergen(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(),
                          editable=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Flavour(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(),
                          editable=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(),
                          editable=False, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    flavour = models.ForeignKey(Flavour, related_name='products',
                                on_delete=models.CASCADE)
    allergen = models.ForeignKey(Allergen, related_name='products',
                                 on_delete=models.CASCADE)

    AVAILABLE = 'AV'
    STOCK_OUT = 'SO'
    SHUTDOWN = 'SH'
    AVAILABILITY_CHOICES = [
            (AVAILABLE, 'Available'),
            (STOCK_OUT, 'Stock-out'),
            (SHUTDOWN, 'Shutdown'),
    ]
    available = models.CharField(
            max_length=2,
            choices=AVAILABILITY_CHOICES,
            default=STOCK_OUT,
    )
    image = models.ImageField(upload_to='products/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    is_bio = models.BooleanField(default=True)
    is_gluten_free = models.BooleanField(default=True)
    is_glucose_syrup_free = models.BooleanField(default=True)
    is_hydrogenated_vegetable_fats_free = models.BooleanField(default=True)
    is_handcrafted = models.BooleanField(default=True)
    is_eur_label_bio = models.BooleanField(default=True)
    is_fr_label_bio = models.BooleanField(default=True)
    unit_number = models.IntegerField()

    class Meta:
        ordering = ('name',)
        # index_together = (('id', 'slug'),)
        indexes = [
                models.Index(fields=['id'], name='id_index'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[str(self.id)])


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    edition_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.review

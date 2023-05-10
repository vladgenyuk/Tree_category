from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    level = models.SmallIntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return f'{self.title}'

    def get_url(self):
        return reverse('categories', kwargs={'category': self.title})


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Product description')
    cost = models.PositiveIntegerField(default=0, verbose_name='Product cost', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Product category')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self):
        return f'{self.title}'

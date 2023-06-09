from django.db import models

from .constants import CARS, TYPECARS


class ModelCars(models.Model):
    model = models.CharField(max_length=40, blank=False, null=True)
    type_car = models.CharField(max_length=40, choices=TYPECARS, default=CARS)
    year = models.IntegerField(blank=False, null=True)
    price = models.DecimalField(decimal_places=0, max_digits=10)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True, null=True, upload_to='images/')

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.model}'


class PostModelCars(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=400, blank=False, null=True)
    image = models.FileField(blank=True, null=True, upload_to='images/')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}'


class SlideModelCars(models.Model):
    title = models.CharField(max_length=40, blank=False, null=True)
    description = models.CharField(max_length=400, blank=False, null=True)
    image = models.FileField(blank=True, null=True, upload_to='images/')

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'

    def __str__(self):
        return f'{self.title}'


class ModelSheet(models.Model):
    lead = models.CharField(max_length=40, blank=False, null=True)
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=400, blank=False, null=True)
    post = models.ManyToManyField(PostModelCars)
    slide = models.ManyToManyField(SlideModelCars)
    image = models.FileField(blank=True, null=True, upload_to='images/')

    class Meta:
        verbose_name = 'Sheet'
        verbose_name_plural = 'Sheets'

    def __str__(self):
        return f'{self.title}'

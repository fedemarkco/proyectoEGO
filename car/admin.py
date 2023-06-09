from django.contrib import admin

from .models import ModelCars, ModelSheet, PostModelCars, SlideModelCars

admin.site.register(ModelCars)
admin.site.register(ModelSheet)
admin.site.register(PostModelCars)
admin.site.register(SlideModelCars)

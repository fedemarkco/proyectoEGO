from django.utils.formats import number_format
from rest_framework import serializers

from .models import ModelCars, ModelSheet, PostModelCars, SlideModelCars


class ModelCarsSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField('separate_thousand')
    type_car = serializers.CharField(source='get_type_car_display')

    class Meta:
        model = ModelCars
        fields = '__all__'

    def separate_thousand(self, obj):
        return f'$ {number_format(obj.price).replace(",", ".")}'


class PostModelCarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostModelCars
        fields = '__all__'


class SlideModelCarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SlideModelCars
        fields = '__all__'


class ModelSheetSerializers(serializers.ModelSerializer):
    post = PostModelCarsSerializers(read_only=True, many=True)
    slide = SlideModelCarsSerializers(read_only=True, many=True)

    class Meta:
        model = ModelSheet
        fields = [
            'id',
            'lead',
            'title',
            'description',
            'image',
            'slide',
            'post'
        ]

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import ModelCars, ModelSheet
from .serializer import ModelCarsSerializer, ModelSheetSerializers


class ModelCarsViewSet(viewsets.ModelViewSet):
    """
    This view gets the values of the car model
    Return:
    {
        id: integer,
        model: string,
        type_car: string,
        year: integer,
        price: decimal
        created_date: datetime
        image: file
    }
    """
    queryset = ModelCars.objects.all()
    serializer_class = ModelCarsSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['type_car']
    ordering_fields = ('price', 'year')


class ModelSheetViewSet(viewsets.ModelViewSet):
    """
    This view gets the values from the car's model sheet
    Return:
    {
        id: integer,
        lead: string,
        title: string,
        description: string,
        post: object,
        slide: object,
        image: file
    }
    """
    queryset = ModelSheet.objects.all()
    serializer_class = ModelSheetSerializers

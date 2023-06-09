from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from car.constants import PICKUPSCOMMERCIALS
from car.models import ModelCars


class ModelCarsTestCase(TestCase):
    def setUp(self):
        ModelCars.objects.create(
            model='Hilux',
            type_car=PICKUPSCOMMERCIALS,
            year=2020,
            price=150700,
            image=None
        )
        self.client = APIClient()

    def test_view_model_cars_response_status(self):
        """
        Call the model-cars api and return a status code 200
        """
        url = reverse('model-cars-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_model_cars_data(self):
        """
        Get the car models and check the quantity found
        """
        url = reverse('model-cars-list')
        response = self.client.get(url, format='json')

        model_car = ModelCars.objects.all()

        self.assertEqual(len(response.json()), len(model_car))

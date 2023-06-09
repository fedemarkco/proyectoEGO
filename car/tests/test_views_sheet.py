from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from car.models import ModelSheet, PostModelCars, SlideModelCars


class ModelSheetTestCase(TestCase):
    def setUp(self):
        self.post_model_cars = PostModelCars.objects.create(
            title='Title',
            description='Description',
            image=None
        )
        self.slide_model_cars = SlideModelCars.objects.create(
            title='Title',
            description='Description',
            image=None
        )
        model_sheet = ModelSheet.objects.create(
            lead='Lead',
            title='Title',
            description='Description',
            image=None
        )
        model_sheet.post.add(self.post_model_cars)
        model_sheet.slide.add(self.slide_model_cars)

        self.client = APIClient()

    def test_view_model_sheet_response_status(self):
        """
        Call the model-sheet api and return a status code 200
        """
        url = reverse('model-sheet-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_model_sheet_data(self):
        """
        Obtains the sheets of the car models and verifies the quantity found
        """
        url = reverse('model-sheet-list')
        response = self.client.get(url, format='json')

        sheet = ModelSheet.objects.filter(
                    post=self.post_model_cars,
                    slide=self.slide_model_cars
                )

        self.assertEqual(len(response.json()), len(sheet))

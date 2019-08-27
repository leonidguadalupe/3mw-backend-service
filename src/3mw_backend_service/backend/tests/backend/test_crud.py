import json
import pytest

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from backend.models import Datapoint, Plant
from backend.tests.factories import PlantFactory, DatapointFactory

UserModel = get_user_model()

class APIPlantTest(APITestCase):
    @pytest.mark.django_db
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test', email='test@...', password='top_secret')
        token = Token.objects.create(user=self.user)
        self.client  = APIClient()
        plant = PlantFactory()
        response = self.client.get(reverse('plant-get'), data={'plant_id': plant.uid})
        self.assertEqual(response.status_code, status.HTTP_400_NOT_FOUND)

class TestPlantList(APIPlantTest):
    @pytest.mark.django_db
    def test_hundred_plants(self):
        for counter in range(99):
            PlantFactory()
        response = self.client.get(reverse('plant-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 100)

class APIDatapointTest(APITestCase):
    @pytest.mark.django_db
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test', email='test@3mw.com', password='top_secret')
        token = Token.objects.create(user=self.user)
        self.client  = APIClient()
        self.plant = PlantFactory()
        response = self.client.get(reverse('plant-get'), data={'plant_id': plant.uid})
        self.assertEqual(response.status_code, status.HTTP_400_NOT_FOUND)

class TestDatapointDateTimeData(APIDatapointTest):
    @pytest.mark.django_db
    def test_processed_datapoint_follows_iso8601_format(self):
        url = reverse('monitoring-fetch', kwargs={'plant_id': self.plant.uid})
        response = self.client.get(url)
        iso8601_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
        time_entry = response.json()[0]["datetime"]
        #assert if it matches pattern
        self.assertTrue(isinstance(re.match(iso8601_pattern, time_entry), re.Match))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Cuboid
from .serializers import CuboidSerializer


class CuboidAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_cuboid(self):
        cuboid_data = {
            'length': 5.5,
            'breadth': 3.5,
            'height': 2.5,
        }
        response = self.client.post('/cuboid/add/', cuboid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cuboid = Cuboid.objects.get(id=response.data['id'])
        serializer = CuboidSerializer(cuboid)
        self.assertEqual(serializer.data, response.data)

    def test_update_cuboid(self):
        cuboid = Cuboid.objects.create(length=5.5, breadth=3.5, height=2.5)
        new_data = {
            'length': 7.5,
            'breadth': 4.5,
            'height': 3.5,
        }
        response = self.client.put(f'/cuboid/update/{cuboid.id}/', new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cuboid.refresh_from_db()
        self.assertEqual(cuboid.length, new_data['length'])
        self.assertEqual(cuboid.breadth, new_data['breadth'])
        self.assertEqual(cuboid.height, new_data['height'])

    def test_list_cuboids(self):
        Cuboid.objects.create(length=5.5, breadth=3.5, height=2.5)
        Cuboid.objects.create(length=7.5, breadth=4.5, height=3.5)
        response = self.client.get('/cuboid/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cuboids = Cuboid.objects.all()
        serializer = CuboidSerializer(cuboids, many=True)
        self.assertEqual(serializer.data, response.data)

    def test_my_list_cuboids(self):
        Cuboid.objects.create(length=5.5, breadth=3.5,
                              height=2.5, created_by=self.client.user)
        Cuboid.objects.create(length=7.5, breadth=4.5,
                              height=3.5, created_by=self.client.user)
        response = self.client.get('/cuboid/my_list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cuboids = Cuboid.objects.filter(created_by=self.client.user)
        serializer = CuboidSerializer(cuboids, many=True)
        self.assertEqual(serializer.data, response.data)

    def test_delete_cuboid(self):
        cuboid = Cuboid.objects.create(
            length=5.5, breadth=3.5, height=2.5, created_by=self.client.user)
        response = self.client.delete(f'/cuboid/delete/{cuboid.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Cuboid.DoesNotExist):
            cuboid.refresh_from_db()

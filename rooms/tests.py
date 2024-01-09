from rest_framework.test import APITestCase

from users.models import User
from . import models


class TestAmenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Amenity Des"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200",
        )
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESC)

    def test_create_amenity(self):
        failed_name = "HEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOO"
        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity desc."

        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(data["name"], new_amenity_name)
        self.assertEqual(data["description"], new_amenity_description)
        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)

        response = self.client.post(
            self.URL,
            data={
                "name": failed_name,
            },
        )  # 최대길이 150글자만 가능한 name에 150 이상을 준 경우
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test Dsc"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(data["description"], self.DESC)

    def test_put_amenity(self):
        failed_name = "HEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOOHEEEEEEEEEEEELLLLLLLLOOOOOOOO"

        response = self.client.put(
            "/api/v1/rooms/amenities/1",
            data={"name": self.NAME, "description": self.DESC},
        )
        data = response.json()
        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)
        self.assertEqual(response.status_code, 200)

        response = self.client.put(
            "/api/v1/rooms/amenities/1", data={"name": failed_name}
        )
        data = response.json()
        self.assertEqual(response.status_code, 400)

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 204)


class TestRooms(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")

        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)
        response = self.client.post("/api/v1/rooms/")

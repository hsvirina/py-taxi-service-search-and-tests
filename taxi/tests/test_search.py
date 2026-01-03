from django.urls import reverse

from taxi.models import Manufacturer, Driver, Car


def test_car_search_by_model(self):
    Car.objects.create(model="BMW X5", manufacturer=self.manufacturer)
    Car.objects.create(model="Audi A4", manufacturer=self.manufacturer)

    response = self.client.get(
        reverse("taxi:car-list"),
        {"model": "BMW"}
    )

    self.assertContains(response, "BMW X5")
    self.assertNotContains(response, "Audi A4")


def test_driver_search_by_username(self):
    Driver.objects.create_user(
        username="john_doe",
        password="12345",
        license_number="ABC12345"
    )
    Driver.objects.create_user(
        username="anna",
        password="12345",
        license_number="DEF67890"
    )

    response = self.client.get(
        reverse("taxi:driver-list"),
        {"username": "john"}
    )

    self.assertContains(response, "john_doe")
    self.assertNotContains(response, "anna")


def test_manufacturer_search_by_name(self):
    Manufacturer.objects.create(name="BMW", country="DE")
    Manufacturer.objects.create(name="Audi", country="DE")

    response = self.client.get(
        reverse("taxi:manufacturer-list"),
        {"name": "BMW"}
    )

    self.assertContains(response, "BMW")
    self.assertNotContains(response, "Audi")

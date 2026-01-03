from django.test import TestCase

from taxi.models import Driver, Car, Manufacturer


class ModelTestCase(TestCase):
    def test_car_str(self):
        car = Car.objects.create(model="test")
        self.assertEqual(str(car), car.model)

    def test_driver_str(self):
        driver = Driver.objects.create(username="test")
        self.assertEqual(str(driver), driver.username)

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="test")
        self.assertEqual(str(manufacturer), manufacturer.name)



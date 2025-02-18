from unittest import TestCase
from wsgiref.validate import validator

from speed_boat import SpeedBoat

class TestSpeedBoat(TestCase):

    def test_add_fuel_cant_add_negative(self):
        # Arrange - setup our variables for testing
        fast_boat = SpeedBoat("", "", 10, 10, 10)

        # Act - call the code we're testing - and get values
        try:
            fast_boat.add_fuel(11)

        except ValueError as ex:
            self.assertEqual(str(ex), "Too much, please don't spill")


        # Assert - did we get what we expected?


    def test_drive(self):
        # Arrange - setup our variables for testing
        fast_boat = SpeedBoat("", "", 10, 10, 10)
        fast_boat.add_fuel(10)
        expected_fuel = 9

        # Act - call the code we're testing - and get values
        fast_boat.drive()
        actual_fuel = fast_boat.get_fuel_in_liters()

        # Assert - did we get what we expected?
        self.assertEqual(expected_fuel, actual_fuel)

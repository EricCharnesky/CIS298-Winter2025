from boat import Boat

class SpeedBoat(Boat):

    def __init__(self, make, model, length, engine_size, max_fuel_in_liters):
        super().__init__(make, model, length)
        self._engine_size = engine_size
        self._fuel_in_liters = 0
        self._max_fuel_in_liters = max_fuel_in_liters

    def get_fuel_in_liters(self):
        return self._fuel_in_liters

    def drive(self):
        # TODO - use fuel based on engine size
        if self._fuel_in_liters < 1:
            raise ValueError("Not enough fuel!")
        print("vroom")
        self._fuel_in_liters -= 1

    def add_fuel(self, fuel_in_liters):
        if self._fuel_in_liters + fuel_in_liters > self._max_fuel_in_liters:
            raise ValueError("Too much, please don't spill")
        if fuel_in_liters < 0:
            raise ValueError("Can't add negative fuel, please obey physics")
        self._fuel_in_liters += fuel_in_liters


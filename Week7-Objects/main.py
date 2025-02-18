import boat # module or file name

from boat import Boat # imports specific class from a module
from row_boat import RowBoat
from speed_boat import SpeedBoat

some_boat = Boat("bayliner", '34', 5) # implicitly calls init
another_boat = boat.Boat("", "", 0)

some_boat._width = 10

another_boat._width = 20

some_boat._color = 'white'

another_boat.set_color('blue')

# weird
boat.Boat.set_color(another_boat, 'orange')

print(another_boat.get_color())

another_boat.drive()

print(type(another_boat))

small_row_boat = RowBoat("", "", 2)

small_row_boat.drive()

fast_boat = SpeedBoat("", "", 10, 1, 10)

fast_boat.add_fuel(1)
fast_boat.drive()
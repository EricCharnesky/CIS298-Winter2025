from boat import Boat

# ( inherited from )
class RowBoat(Boat):

    def __init__(self, make, model, number_of_oars):
        super().__init__(make, model, 5)
        self._number_of_oars = number_of_oars

    def drive(self):
        for oar in range(self._number_of_oars):
            print("row row row your boat")
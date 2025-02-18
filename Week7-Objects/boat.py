class Boat:
    _width = 0 # static?
    # initialize function ( constructor )
    def __init__(self, make, model, length): # self is like a this pointer
        self._color = "" # starting a self variable with an underscore indicates private
        self._make = make
        self._model = model
        self._length = length

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_length(self):
        return self._length

    @staticmethod
    def drive():
        print("brrrrr")

# allows you to have code that ONLY runs if you run the specific module file
if __name__ == '__main__':
    print("hi from boat module in main check")
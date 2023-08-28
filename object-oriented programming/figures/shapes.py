class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.height = square.height

    def get_area(self):
        return self.square.get_area() * 6

    def get_volume(self):
        return self.square.get_area() * self.height


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def get_volume(self):
        return self.base.get_area() * self.height

    def get_area(self):
        return (self.base.get_area() + self.base.height * self.height + self.base.width * self.height) * 2

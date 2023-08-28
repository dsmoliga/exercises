from shapes import Rectangle, Square, Cube, Cuboid

my_rectangle = Rectangle(10, 30)
my_square = Square(5)
my_cube = Cube(Square(10))
my_cuboid = Cuboid(Rectangle(15, 30), 5)

print(my_rectangle.get_area())
print(my_square.get_area())
print(my_cube.get_area())
print(my_cube.get_volume())
print(my_cuboid.get_area())
print(my_cuboid.get_volume())

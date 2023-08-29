import unittest
from shapes import Rectangle, Square, Cube, Cuboid


class TestRectangle(unittest.TestCase):
    def test_rectangle_size_with_negative_or_zero(self):
        my_rectangle = Rectangle(-10, 5)
        self.assertGreater(my_rectangle.height, 0)
        self.assertGreater(my_rectangle.width, 0)
        self.assertEqual(my_rectangle.get_area(), 50)

    def test_rectangle_size_with_letters(self):
        my_rectangle = Rectangle('a', 10)
        with self.assertRaises(TypeError):
            result = my_rectangle


class TestSquare(unittest.TestCase):
    def test_square_size_with_negative_or_zero(self):
        my_square = Square(-5)
        self.assertGreater(my_square.height, 0)
        self.assertGreater(my_square.width, 0)
        self.assertEqual(my_square.get_area(), 25)

    def test_square_size_with_letters(self):
        my_square = Square('a')
        with self.assertRaises(TypeError):
            result = my_square


class TestCube(unittest.TestCase):
    def test_cube_size_with_negative_or_zero(self):
        my_cube = Cube(Square(-5))
        self.assertGreater(my_cube.height, 0)
        self.assertEqual(my_cube.get_area(), 150)
        self.assertEqual(my_cube.get_volume(), 125)

    def test_cube_with_different_base(self):
        my_cube = Cube(Rectangle(5, 6))
        self.assertEqual(my_cube.square.width, my_cube.square.height)

    def test_cube_size_with_letters(self):
        my_cube = Cube(Square('a'))
        with self.assertRaises(TypeError):
            result = my_cube


class TestCuboid(unittest.TestCase):
    def test_cuboid_size_with_negative_or_zero(self):
        my_cuboid = Cuboid(Rectangle(4, 10), 0)
        self.assertGreater(my_cuboid.height, 0)
        self.assertEqual(my_cuboid.get_area(), 360)
        self.assertEqual(my_cuboid.get_volume(), 400)

    def test_cuboid_with_rectangle_base(self):
        my_cuboid_rectangle = Cuboid(Rectangle(5, 10), 10)
        self.assertEqual(my_cuboid_rectangle.get_area(), 400)
        self.assertEqual(my_cuboid_rectangle.get_volume(), 500)

    def test_cuboid_with_square_base(self):
        my_cuboid_square = Cuboid(Square(5), 10)
        self.assertEqual(my_cuboid_square.get_area(), 250)
        self.assertEqual(my_cuboid_square.get_volume(), 250)

    def test_cuboid_size_with_letters(self):
        my_cuboid = Cuboid((Square(5)), 'a')
        with self.assertRaises(TypeError):
            result = my_cuboid


if __name__ == '__main__':
    unittest.main()

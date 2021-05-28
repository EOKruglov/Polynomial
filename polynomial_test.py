import unittest

from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def test_empty_args(self):
        with self.assertRaises(TypeError):
            p = Polynomial()

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            p = Polynomial([])

    def test_empty_tuple(self):
        with self.assertRaises(ValueError):
            p = Polynomial(())

    def test_incorrect_type(self):
        with self.assertRaises(TypeError):
            p = Polynomial(1.2)

    def test_incorrect_list_type(self):
        with self.assertRaises(TypeError):
            p = Polynomial(['1', '2', '3'])

    def test_incorrect_tuple_type(self):
        with self.assertRaises(TypeError):
            p = Polynomial(('1', '2', '3'))

    def test_copy_polynomial(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial(p1)
        self.assertEqual(p1, p2)

    def test_add_with_constant(self):
        p1 = Polynomial([1, 2, 3])
        c = 3
        result = Polynomial([1, 2, 6])
        self.assertEqual(p1 + c, result)

    def test_add_with_polynom(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        result = Polynomial([2, 4, 6])
        self.assertEqual(p1 + p2, result)

    def test_add_const_with_polynom(self):
        p1 = Polynomial([1, 2, 3])
        c = 3
        result = Polynomial([1, 2, 6])
        self.assertEqual(c + p1, result)

    def test_sub_with_constant(self):
        p1 = Polynomial([1, 2, 3])
        c = 2
        result = Polynomial([1, 2, 1])
        self.assertEqual(p1 - c, result)

    def test_sub_with_polynom(self):
        p1 = Polynomial([2, 4, 6])
        p2 = Polynomial([1, 2, 3])
        result = Polynomial([1, 2, 3])
        self.assertEqual(p1 - p2, result)

    def test_sub_const_with_polynom(self):
        p1 = Polynomial([1, 2, 3])
        c = 1
        result = Polynomial([-1, -2, -2])
        self.assertEqual(c - p1, result)

    def test_mul_with_constant(self):
        p1 = Polynomial([1, 2, 3])
        c = 2
        result = Polynomial([2, 4, 6])
        self.assertEqual(p1 * c, result)

    def test_mul_with_polynom(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        result = Polynomial([1, 4, 10, 12, 9])
        self.assertEqual(p1 * p2, result)

    def test_mul_const_with_polynom(self):
        p1 = Polynomial([1, 2, 3])
        c = 2
        result = Polynomial([2, 4, 6])
        self.assertEqual(c * p1, result)

    def test_print_polynom(self):
        p1 = Polynomial([0, 1, 2, 3])
        ref_str = 'x^2+2x+3'
        self.assertEqual(str(p1), ref_str)

    def test_print_polynom_negative_values(self):
        p1 = Polynomial([0, -1, 2, -3])
        ref_str = '-x^2+2x-3'
        self.assertEqual(str(p1), ref_str)


if __name__ == "__main__":
    unittest.main()

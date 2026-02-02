import unittest
from classify import (
    classify_package,
    is_bulky,
    is_heavy,
    STANDARD,
    SPECIAL,
    REJECTED,
    MAX_VOLUME,
    MAX_DIMENSION,
    MAX_WEIGHT,
)


class TestIsBulky(unittest.TestCase):

    def test_not_bulky_small_package(self):
        self.assertFalse(is_bulky(10, 10, 10))

    def test_bulky_volume_at_threshold(self):
        self.assertTrue(is_bulky(100, 100, 100))

    def test_bulky_volume_above_threshold(self):
        self.assertTrue(is_bulky(101, 100, 100))

    def test_not_bulky_volume_below_threshold(self):
        self.assertFalse(is_bulky(99, 100, 100))

    def test_bulky_width_at_threshold(self):
        self.assertTrue(is_bulky(150, 10, 10))

    def test_bulky_height_at_threshold(self):
        self.assertTrue(is_bulky(10, 150, 10))

    def test_bulky_length_at_threshold(self):
        self.assertTrue(is_bulky(10, 10, 150))

    def test_not_bulky_dimension_below_threshold(self):
        self.assertFalse(is_bulky(149, 10, 10))

    def test_bulky_dimension_above_threshold(self):
        self.assertTrue(is_bulky(200, 10, 10))


class TestIsHeavy(unittest.TestCase):

    def test_not_heavy_light_package(self):
        self.assertFalse(is_heavy(10))

    def test_heavy_at_threshold(self):
        self.assertTrue(is_heavy(20))

    def test_not_heavy_below_threshold(self):
        self.assertFalse(is_heavy(19))

    def test_heavy_above_threshold(self):
        self.assertTrue(is_heavy(25))


class TestClassifyPackage(unittest.TestCase):

    def test_standard_small_light_package(self):
        self.assertEqual(classify_package(10, 10, 10, 10), STANDARD)

    def test_standard_near_limits(self):
        self.assertEqual(classify_package(99, 100, 100, 19), STANDARD)

    def test_standard_dimension_near_limit(self):
        self.assertEqual(classify_package(149, 10, 10, 19), STANDARD)

    def test_special_heavy_only(self):
        self.assertEqual(classify_package(10, 10, 10, 20), SPECIAL)

    def test_special_heavy_above_threshold(self):
        self.assertEqual(classify_package(10, 10, 10, 25), SPECIAL)

    def test_special_bulky_by_width(self):
        self.assertEqual(classify_package(150, 10, 10, 10), SPECIAL)

    def test_special_bulky_by_height(self):
        self.assertEqual(classify_package(10, 150, 10, 10), SPECIAL)

    def test_special_bulky_by_length(self):
        self.assertEqual(classify_package(10, 10, 150, 10), SPECIAL)

    def test_special_bulky_by_volume(self):
        self.assertEqual(classify_package(100, 100, 100, 10), SPECIAL)

    def test_special_bulky_dimension_above_threshold(self):
        self.assertEqual(classify_package(200, 10, 10, 10), SPECIAL)

    def test_rejected_bulky_volume_and_heavy(self):
        self.assertEqual(classify_package(100, 100, 100, 20), REJECTED)

    def test_rejected_bulky_dimension_and_heavy(self):
        self.assertEqual(classify_package(150, 10, 10, 20), REJECTED)

    def test_rejected_very_bulky_and_very_heavy(self):
        self.assertEqual(classify_package(200, 200, 200, 100), REJECTED)

    def test_rejected_bulky_by_both_volume_and_dimension_and_heavy(self):
        self.assertEqual(classify_package(150, 150, 150, 25), REJECTED)

    def test_zero_dimensions(self):
        self.assertEqual(classify_package(0, 0, 0, 0), STANDARD)

    def test_one_dimension_zero(self):
        self.assertEqual(classify_package(100, 100, 0, 10), STANDARD)


class TestConstants(unittest.TestCase):

    def test_max_volume_value(self):
        self.assertEqual(MAX_VOLUME, 1_000_000)

    def test_max_dimension_value(self):
        self.assertEqual(MAX_DIMENSION, 150)

    def test_max_weight_value(self):
        self.assertEqual(MAX_WEIGHT, 20)


if __name__ == "__main__":
    unittest.main()

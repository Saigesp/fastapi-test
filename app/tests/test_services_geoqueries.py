import unittest

from app.services.geoqueries import get_parsed_bounds


class GeoQueriesTest(unittest.TestCase):

    def setUp(self):
        self.bounds = "-3.7271749,40.384994,-6.3991346,38.3233673"

    def test_get_parsed_bounds_returns_4_elements(self):
        """
        get_parsed_bounds() returns 4 elements for the default input
        """
        result = get_parsed_bounds(self.bounds)
        self.assertEqual(len(result), 4)

    def test_get_parsed_bounds_returns_floats(self):
        """
        All elements returned by get_parsed_bounds() are floats
        """
        result = get_parsed_bounds(self.bounds)
        self.assertTrue(all([isinstance(x, float) for x in result]))

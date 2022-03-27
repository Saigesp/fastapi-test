import unittest

from app.services.geoqueries import get_parsed_bounds


class GeoQueriesTest(unittest.TestCase):
    def setUp(self):
        self.bounds = "-3.7271749,40.384994,-6.3991346,38.3233673"

    def test_get_parsed_bounds_returns_4_elements(self):
        """
        get_parsed_bounds() returns a dict with 4 keys
        """
        result = get_parsed_bounds(self.bounds)
        self.assertTrue(result.get("lngNE"))
        self.assertTrue(result.get("latNE"))
        self.assertTrue(result.get("lngSW"))
        self.assertTrue(result.get("latSW"))

    def test_get_parsed_bounds_returns_floats(self):
        """
        All elements returned by get_parsed_bounds() are floats
        """
        result = get_parsed_bounds(self.bounds)
        self.assertTrue(all([isinstance(result[k], float) for k in result.keys()]))

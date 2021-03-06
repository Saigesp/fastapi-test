from app.tests import AsyncioDBTestCase

from app.selectors.postal_codes import get_postal_codes_from_bounds


class PostalCodesSelectorTest(AsyncioDBTestCase):
    async def test_postal_codes_filters_by_bounds(self):
        """
        get_postal_codes_from_bounds() returns only one result
        for Carabanchel 🤟 coordinates
        """
        opanel_coords = {
            "lngNE": -3.7228258,
            "latNE": 40.3866711,
            "lngSW": -3.7240934,
            "latSW": 40.3860618,
        }
        results = await get_postal_codes_from_bounds(opanel_coords)
        self.assertEqual(len(results), 1)
        self.assertTrue(results[0].get("geometry"))
        self.assertEqual(results[0].get("total_turnover"), 13195094.0)

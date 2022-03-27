from app.tests import AsyncioDBtestCase

from app.selectors.postal_codes import get_postal_codes_from_bounds


class PostalCodesSelectorTest(AsyncioDBtestCase):
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

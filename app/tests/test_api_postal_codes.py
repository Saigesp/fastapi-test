from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from app.api.postal_codes import get_postal_codes


class PostalCodesAPITest(IsolatedAsyncioTestCase):
    @patch("app.api.postal_codes.get_postal_codes_from_bounds")
    @patch("app.api.postal_codes.get_parsed_bounds")
    @patch("app.api.postal_codes.validate_bounds")
    async def test_postal_codes_calls_validation(self, mock, *args):
        """
        get_postal_codes() calls validate_bounds()
        """
        _ = await get_postal_codes("2,2,1,1")
        mock.assert_called_with("2,2,1,1")

    @patch("app.api.postal_codes.get_postal_codes_from_bounds")
    @patch("app.api.postal_codes.validate_bounds")
    @patch("app.api.postal_codes.get_parsed_bounds")
    async def test_postal_codes_calls_parse_bounds(self, mock, *args):
        """
        get_postal_codes() calls get_parsed_bounds()
        """
        _ = await get_postal_codes("2,2,1,1")
        mock.assert_called_with("2,2,1,1")

    @patch("app.api.postal_codes.get_postal_codes_from_bounds")
    async def test_postal_codes_calls_selector(self, mock, *args):
        """
        get_postal_codes() calls get_postal_codes_from_bounds()
        """
        _ = await get_postal_codes("2,2,1,1")
        mock.assert_called_with(
            {
                "lngNE": 2.0,
                "latNE": 2.0,
                "lngSW": 1.0,
                "latSW": 1.0,
            }
        )

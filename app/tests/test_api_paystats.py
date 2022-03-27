from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from app.api.paystats import get_paystats_by_age_gender


class PostalCodesAPITest(IsolatedAsyncioTestCase):
    @patch("app.api.paystats.get_paystats_by_age_gender_from_postal_code_id")
    @patch("app.api.paystats.validate_postal_code_id")
    async def test_paystats_age_gender_calls_validation(self, mock, *args):
        """
        get_paystats_by_age_gender() calls validate_postal_code_id()
        """
        _ = await get_paystats_by_age_gender(1)
        mock.assert_called_with(1)

    @patch("app.api.paystats.get_paystats_by_age_gender_from_postal_code_id")
    async def test_paystats_age_gender_calls_selector(self, mock, *args):
        """
        get_paystats_by_age_gender() calls get_paystats_by_age_gender_from_postal_code_id()
        """
        _ = await get_paystats_by_age_gender(1)
        mock.assert_called_with(1)

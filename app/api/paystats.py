from app.services.validation import validate_postal_code_id
from app.selectors.paystats import (
    get_paystats_by_age_gender_from_postal_code_id,
    get_paystats_by_time_gender_from_postal_code_id,
)


async def get_paystats_by_age_gender(postal_code_id: int):
    validate_postal_code_id(postal_code_id)
    data = await get_paystats_by_age_gender_from_postal_code_id(postal_code_id)

    return {
        "postal_code_id": postal_code_id,
        "results": data,
    }


async def get_paystats_by_time_gender(postal_code_id: int):
    validate_postal_code_id(postal_code_id)
    data = await get_paystats_by_time_gender_from_postal_code_id(postal_code_id)

    return {
        "postal_code_id": postal_code_id,
        "results": data,
    }

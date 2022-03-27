from app.db import database


async def get_paystats_by_age_gender_from_postal_code_id(postal_code_id: int):
    """
    Get paystats for a given postal code grouped by age and gender
    and aggregate total ammount

    :param postal_code_id: postal code entity ID
    """
    query = (
        "SELECT paystats.p_age AS age"
        ", paystats.p_gender AS gender"
        ", SUM(paystats.amount) AS total_amount"
        " FROM paystats"
        " WHERE paystats.postal_code_id = :postal_code_id"
        " GROUP BY paystats.p_age, paystats.p_gender"
    )
    values = {
        "postal_code_id": postal_code_id,
    }
    return await database.fetch_all(query=query, values=values)


async def get_paystats_by_time_gender_from_postal_code_id(postal_code_id: int):
    """
    Get paystats for a given postal code grouped by date and gender
    and aggregate total ammount

    :param postal_code_id: postal code entity ID
    """
    query = (
        "SELECT paystats.p_month AS month"
        ", paystats.p_gender AS gender"
        ", SUM(paystats.amount) AS total_amount"
        " FROM paystats"
        " WHERE paystats.postal_code_id = :postal_code_id"
        " GROUP BY paystats.p_month, paystats.p_gender"
        " ORDER BY paystats.p_month, paystats.p_gender"
    )
    values = {
        "postal_code_id": postal_code_id,
    }
    return await database.fetch_all(query=query, values=values)

from app.db import database


async def get_adm1s_from_prefix(prefix: str):
    """
    Get adm1 (CCAA in Spain) geometry from a given postal code prefix
    and aggregate total turnover ammount

    :param prefix: postal code prefix
    """
    query = (
        "SELECT SUBSTRING(postal_codes.code::varchar, 1, 2) AS prefix"
        ", SUM(paystats.amount) AS total_turnover"
        ", ST_AsGeoJSON(ST_Union(postal_codes.the_geom)) as geometry"
        " FROM postal_codes"
        " LEFT JOIN paystats ON paystats.postal_code_id = postal_codes.id"
        " WHERE"
        " postal_codes.code::varchar LIKE :prefix"
        " GROUP BY prefix"
    )
    values = {
        "prefix": f"{prefix}%",
    }
    return await database.fetch_all(query=query, values=values)

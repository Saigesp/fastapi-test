from app.db import database


async def get_postal_codes_from_bounds(bounds: dict, srid: int = 4326):
    """
    Get postal codes geometries from a given bounds box (NE-SW)
    and aggregate total turnover ammount

    :param bounds: bounds box dict (lngNE, latNE, lngSW and latSW)
    :param srid: spatial reference system
    """
    query = (
        "SELECT DISTINCT postal_codes.id"
        ", postal_codes.code"
        ", ST_AsGeoJSON(postal_codes.the_geom) AS geometry"
        ", SUM(paystats.amount) AS total_turnover"
        " FROM postal_codes"
        " LEFT JOIN paystats ON paystats.postal_code_id = postal_codes.id"
        " WHERE"
        " ST_Intersects(postal_codes.the_geom, st_makeenvelope(:lngSW, :latSW, :lngNE, :latNE, :srid))"
        " GROUP BY postal_codes.id"
    )
    values = {
        **bounds,
        "srid": srid,
    }
    return await database.fetch_all(query=query, values=values)

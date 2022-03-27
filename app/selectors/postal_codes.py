from app.db import database


async def get_postal_codes_from_bounds(bounds: dict, srid: int = 4326):
    query = (
        "SELECT id"
        ", code"
        ", ST_AsGeoJSON(the_geom) AS geometry"
        " FROM postal_codes"
        " WHERE "
        " ST_Intersects(the_geom, st_makeenvelope(:lngSW, :latSW, :lngNE, :latNE, :srid))"
    )
    values = {
        **bounds,
        "srid": srid,
    }
    return await database.fetch_all(query=query, values=values)

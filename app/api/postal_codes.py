from app.services.validation import validate_bounds
from app.services.geoqueries import get_parsed_bounds


async def get_postal_codes(bounds: str = ""):
    """
    Get geometries (polygons) fro a given bounds
    :param bounds: NE-SW lng-lat string separated by commas
    """
    validate_bounds(bounds)
    bounds = get_parsed_bounds(bounds)

    # TODO: Get geometry data from db
    # TODO: Serialize geometry data from db
    # TODO: Get turnover data from db
    # TODO: Serialize turnover data data from db

    return {
        "bounds": bounds,
        # TODO: Add requested data
    }

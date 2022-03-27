from app.services.validation import validate_bounds
from app.services.geoqueries import get_parsed_bounds
from app.selectors.postal_codes import get_postal_codes_from_bounds
from app.serializers.postal_codes import PostalCodesOutputSerializer


async def get_postal_codes(bounds: str = ""):
    """
    Get geometries (polygons) fro a given bounds
    :param bounds: NE-SW lng-lat string separated by commas
    """
    validate_bounds(bounds)
    bounds = get_parsed_bounds(bounds)
    data = await get_postal_codes_from_bounds(bounds)

    # TODO: Get turnover data from db
    # TODO: Serialize turnover data data from db

    return {
        "bounds": bounds,
        "results": PostalCodesOutputSerializer(data).data,
    }

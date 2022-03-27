import re
from fastapi import HTTPException


def validate_bounds(bounds: str) -> bool:
    """
    Check that 'bounds' queryparam has correct format

    :param bounds: NE-SW lng-lat bounds separated by commas
    :return: True if validation succeded
    :raises HTTPException: bounds not provided or incorrect format

    TODO: Validate latitude between -90 and 90
          Validate longitude between -180 and 180
          Validate NE > SW
    """
    format_error = HTTPException(
        status_code=400,
        detail=(
            "Error: Incorrect 'bounds' format. "
            "Expected 4 floats representing NE-SW lng-lat "
            "coordinates on EPSG:4326 system, separated by commas. "
            "Ex.: -3.7271749,40.384994,-6.3991346,38.3233673."
        ),
    )

    if not bounds:
        raise HTTPException(
            status_code=400,
            detail=("Error: 'bounds' param not provided"),
        )

    if not isinstance(bounds, str):
        raise format_error

    if not len(bounds.split(",")) == 4:
        raise format_error

    if not all(
        [str(c).lstrip("-").replace(".", "", 1).isdigit() for c in bounds.split(",")]
    ):
        raise format_error

    return True


def validate_postal_code_id(postal_code_id: int) -> bool:
    """
    Check that 'postal_code_id' queryparam is correct

    :param postal_code_id: postal code ID
    :return: True if validation succeded
    :raises HTTPException: if postal_code_id format is incorrect
    """
    format_error = HTTPException(
        status_code=400,
        detail=(
            "Error: Incorrect 'postal_code_id' format. "
            "Expected integer greater than 0."
        ),
    )

    if not isinstance(postal_code_id, int):
        raise format_error

    if postal_code_id <= 0:
        raise format_error

    return True

def validate_postal_code_prefix(prefix: str) -> bool:
    """
    Check that 'postal_code_prefix' queryparam is correct

    :param prefix: postal code prefix (can be '08')
    :return: True if validation succeded
    :raises HTTPException: if prefix format is incorrect
    """
    format_error = HTTPException(
        status_code=400,
        detail=(
            "Error: Incorrect 'postal_code_prefix' format. "
            "Expected 2-integers string (Ex: 08)."
        ),
    )

    pattern = re.compile(r"^\d{2}$")

    if not pattern.match(prefix):
        raise format_error

    return True

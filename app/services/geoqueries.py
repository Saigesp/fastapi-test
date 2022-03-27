def get_parsed_bounds(bounds: str):
    """
    Parse bounds querystring
    :param bounds: NE-SW lng-lat bounds separated by commas
    :return: bounds as list of floats
    """
    lngNE, latNE, lngSW, latSW = [float(b) for b in bounds.split(",")]

    return {
        "lngNE": lngNE,
        "latNE": latNE,
        "lngSW": lngSW,
        "latSW": latSW,
    }

def get_parsed_bounds(bounds: str):
    """
    Parse bounds querystring
    :param bounds: NE-SW lng-lat bounds separated by commas
    :return: bounds as list of floats
    """
    return [float(b) for b in bounds.split(",")]

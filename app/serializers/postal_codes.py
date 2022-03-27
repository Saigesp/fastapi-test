import json


class PostalCodesOutputSerializer:
    """
    Serialize postal_codes table entities:
        - Transform geometry field: str -> dict

    # TODO: Move total_turnover inside geometry.properties
    """

    def __init__(self, data):
        self.data = self.get_serialized_data(data)

    def get_serialized_data(self, data):
        return PostalCodesOutputSerializer.serialize(data)

    @staticmethod
    def serialize(data):
        return [{**d, "geometry": json.loads(d.geometry)} for d in data]

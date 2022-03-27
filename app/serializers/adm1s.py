import json


class Adm1OutputSerializer:
    """
    Serialize adm1 aggregated entities (joined postal_codes):
        - Transform geometry field: str -> dict

    # TODO: Move total_turnover inside geometry.properties?
    """

    def __init__(self, data):
        self.data = self.get_serialized_data(data)

    def get_serialized_data(self, data):
        return Adm1OutputSerializer.serialize(data)

    @staticmethod
    def serialize(data):
        return [{**d, "geometry": json.loads(d.geometry)} for d in data]

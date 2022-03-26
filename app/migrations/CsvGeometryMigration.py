from shapely import wkb
from .CsvMigration import CsvMigration


class CsvGeometryMigration(CsvMigration):
    """
    Migration class to insert each row from a CSV file into a table

    - The csv must have a header row, that will be matched with the given
      table column names
    - The geometry field must be WKB data type (Future improvements: handle
      more types)
    """
    def __init__(
        self,
        *,
        db,
        name: str,
        file: str,
        table: str,
        geometry_field: str = "geometry",
        srid: int = 4326,
        force: bool = False,
    ):
        self.srid = srid
        self.geometry_field = geometry_field

        super().__init__(
            db=db,
            name=name,
            file=file,
            table=table,
            force=force,
        )

    def set_value_type(self, key: str, value: str):
        if key == self.geometry_field:
            geometry = wkb.loads(value, hex=True)
            return f"SRID={self.srid};{geometry.wkt}"
        
        return super().set_value_type(key, value)

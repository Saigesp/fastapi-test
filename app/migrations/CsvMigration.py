import os
import re
import csv
from datetime import datetime
from .Migration import Migration


class CsvMigration(Migration):
    """
    Migration class to insert each row from a CSV file into a table

    - The csv must have a header row, that will be matched with the given
      table column names
    """

    def __init__(
        self,
        *,
        db,
        name: str,
        file: str,
        table: str,
        force: bool = False,
    ):
        self.file = file
        self.table = table
        query, values = self.get_query_from_csv()

        super().__init__(
            db=db,
            name=name,
            query=query,
            values=values,
            force=force,
        )

    def get_query_from_csv(self):
        with open(self.file, "r") as csvfile:
            values = [self.set_row_types(row) for row in csv.DictReader(csvfile)]
            headers = values[0].keys()
            columns = map((lambda x: f":{x}"), headers)
            query = (
                f"INSERT INTO {self.table} ("
                + ", ".join(headers)
                + ") VALUES ("
                + ", ".join(columns)
                + ")"
            )

        return query, values

    def set_row_types(self, row: dict):
        return {k: self.set_value_type(k, v) for k, v in row.items()}

    def set_value_type(self, key: str, value: str):
        if str(value).isdigit():
            return int(value)
        if str(value).lstrip("-").replace(".", "", 1).isdigit():
            return float(value)
        if re.search(r"\d{4}-\d{2}-\d{2}", value):
            return datetime.strptime(value, "%Y-%m-%d")
        return value

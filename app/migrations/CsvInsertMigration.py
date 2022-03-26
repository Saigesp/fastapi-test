import re
import csv
from datetime import datetime
from .Migration import Migration


class CsvInsertMigration(Migration):
    def __init__(
        self,
        *,
        db,
        name: str,
        file: str,
        table: str,
        force: bool = False,
    ):
        query, values = self.get_query_from_csv(file, table)

        super().__init__(
            db=db,
            name=name,
            query=query,
            values=values,
            force=force,
        )

    def get_query_from_csv(self, file: str, table: str):
        with open(file, 'r') as csvfile:
            values = [self.set_row_types(row) for row in csv.DictReader(csvfile)]
            headers = values[0].keys()
            columns = map((lambda x: f":{x}"), headers)
            query = f"INSERT INTO {table} (" + ", ".join(headers) + ") VALUES (" + ", ".join(columns) + ")"

        return query, values

    def set_row_types(self, row):
        return {k: self.set_value_type(v) for k, v in row.items()}

    def set_value_type(self, value):
        if str(value).isdigit():
            return int(value)
        if str(value).replace('.', '', 1).isdigit():
            return float(value)
        if re.search(r'\d{4}-\d{2}-\d{2}', value):
            return datetime.strptime(value, '%Y-%m-%d')
        return value
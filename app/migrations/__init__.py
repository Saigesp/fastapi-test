from .Migration import Migration
from .CsvMigration import CsvMigration
from .CsvGeometryMigration import CsvGeometryMigration


async def run_migrations(db):
    await Migration(
        db=db,
        name="0000",
        query=(
            "CREATE TABLE IF NOT EXISTS migrations ("
                "id SERIAL PRIMARY KEY"
                ", name VARCHAR(200) NOT NULL UNIQUE"
            ")"
        ),
        force=True,
    ).migrate()

    await Migration(
        db=db,
        name="0001",
        query=(
            "CREATE TABLE paystats ("
                "id INTEGER PRIMARY KEY"
                ", amount FLOAT(24)"
                ", p_month DATE"
                ", p_age VARCHAR(10)"
                ", p_gender VARCHAR(1)"
                ", postal_code_id INTEGER"
            ")"
        ),
    ).migrate()

    await CsvMigration(
        db=db,
        name="0002",
        file="data/paystats.csv",
        table="paystats",
    ).migrate()

    await Migration(
        db=db,
        name="0003",
        query=(
            "CREATE TABLE postal_codes ("
                "id INTEGER PRIMARY KEY"
                ", the_geom GEOMETRY"
                ", code INTEGER"
            ")"
        ),
    ).migrate()

    await CsvGeometryMigration(
        db=db,
        name="0004",
        file="data/postal_codes.csv",
        table="postal_codes",
        geometry_field="the_geom",
    ).migrate()

from fastapi.logger import logger


class Migration:
    def __init__(self, db, name, query, force=False):
        self.db = db
        self.name = name
        self.query = query
        self.force = force

    async def migrate(self):
        if self.force or not await self.is_already_applied():
            await self.db.execute(query=self.query)
            await self.register_migration()
        logger.info(f"--> Migration {self.name} OK")

    async def is_already_applied(self):
        return await self.db.execute(
            query=(
                "SELECT EXISTS("
                    "SELECT * FROM public.migrations "
                    f"WHERE name = '{self.name}'"
                ")"
            )
        )

    async def register_migration(self):
        await self.db.execute(
            query=(
                "INSERT INTO migrations(name) "
                f"VALUES ('{self.name}') "
                "ON CONFLICT DO NOTHING;"
            )
        )


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
                ", p_age VARCHAR(4)"
                ", p_gender VARCHAR(1)"
                ", postal_code_id VARCHAR(5)"
            ")"
        ),
    ).migrate()


async def check_migrations(db):
    if not db.is_connected:
        await db.connect()

    await run_migrations(db)

class Migration:
    """
    Migration class to handle raw sql queries
    """

    def __init__(
        self,
        *,
        db,
        name: str,
        query: str,
        values: list = [],
        force: bool = False,
    ):
        self.db = db
        self.name = name
        self.query = query
        self.values = values
        self.force = force

    async def migrate(self):
        if self.force or not await self.is_already_applied():
            await self.execute_migration()
            await self.register_migration()

    async def is_already_applied(self):
        return await self.db.execute(
            query=(
                "SELECT EXISTS("
                    "SELECT * FROM public.migrations "
                    f"WHERE name = '{self.name}'"
                ")"
            )
        )

    async def execute_migration(self):
        if len(self.values):
            await self.db.execute_many(query=self.query, values=self.values)
        else:
            await self.db.execute(query=self.query)

    async def register_migration(self):
        await self.db.execute(
            query=(
                "INSERT INTO migrations(name) "
                f"VALUES ('{self.name}') "
                "ON CONFLICT DO NOTHING;"
            )
        )

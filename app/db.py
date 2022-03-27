import os
import databases

database = databases.Database(os.getenv("DATABASE_URL"))
# TODO: Configure db for tests with
# database = databases.Database(URL, force_rollback=True)

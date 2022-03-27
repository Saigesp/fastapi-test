import os
import databases

database = databases.Database(os.getenv("DATABASE_URL"))
# TODO: Configure db as
#       database = databases.Database(URL, force_rollback=True)
#       for tests

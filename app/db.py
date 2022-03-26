import os
import databases

database = databases.Database(os.getenv("DATABASE_URL"))

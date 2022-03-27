from unittest import IsolatedAsyncioTestCase
from app.db import database


class AsyncioDBTestCase(IsolatedAsyncioTestCase):
    """
    Class to execute tests that touch the database
    """

    async def asyncSetUp(cls):
        if not database.is_connected:
            await database.connect()

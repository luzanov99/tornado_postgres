import tornado


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        conn = self.application.db
        result = await conn.fetch("SELECT * FROM example_table")
        self.write(f"Data from PostgreSQL: {result}")



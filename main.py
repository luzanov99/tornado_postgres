from handlers import MainHandler
import tornado.ioloop
import tornado.web
import asyncpg
import os



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def init_db():
    db_url = os.environ.get("DB_URL", "postgresql://user:password@localhost:5432/database")
    return await asyncpg.connect(db_url)

if __name__ == "__main__":
    app = make_app()
    app.db = tornado.ioloop.IOLoop.current().run_sync(init_db)
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
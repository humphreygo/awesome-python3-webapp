import orm
from models import User,Blog,Comment

import asyncio

aloop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from orm.create_pool(loop=aloop, user='www-data', password='www-data',db='awesome')

    u = User(name = 'test', email = 'test@example.com', passwd ='1234556677', image = 'about:blank')

    yield from u.save()

aloop.run_until_complete(test())
aloop.close()

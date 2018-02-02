import orm
from models import User,Blog,Comment,next_id 

import asyncio

aloop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from orm.create_pool(loop=aloop, user='www-data', password='www-data',db='awesome')
    blog = Blog(id = 2,user_id='00151742755147359f8f21f530043e7b5c7ed2eace44692000',user_name='hrconnect@126.com',user_image='about:blank',name='dfdsaf',summary='dfasdfasdfads',content='fdasfasdfasd')
    #u = User(name = 'test', email = 'test@example.com', passwd ='1234556677', image = 'about:blank')

    yield from blog.save()

aloop.run_until_complete(test())
aloop.close()

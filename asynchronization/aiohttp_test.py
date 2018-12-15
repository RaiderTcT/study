import asyncio
from aiohttp import web
# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
"""
/ - 首页返回b'<h1>Index</h1>'；
/hello/{name} - 根据URL参数返回文本hello, %s!。
"""
# async def index(request):
#     await asyncio.sleep(0.5)
#     return web.Response(body=b'<h1>Index</h1>',  content_type='text/html')

# async def hello(request):
#     await asyncio.sleep(0.5)
#     text = f"<h1>Hello, {request.match_info['name']}</h1>"
#     return web.Response(body=text.encode('utf-8'), content_type='text/html')

# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     app.router.add_route('GET', '/hello/{name}', hello)
#     srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
#     print("Server start at http:127.0.0.1: 8000...")
#     return srv
routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    # return web.Response(text='Hello Aiohttp!')
    return web.json_response({'name': 'index'})


@routes.get('/about')
async def hello(request):
    await asyncio.sleep(0.5)
    text = f"Asynchronous HTTP Client/Server for asyncio and Python."
    return web.Response(text=text)


def init():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(init(loop))
    # loop.run_forever()
    init()

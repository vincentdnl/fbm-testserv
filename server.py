import asyncio
import aiohttp
import aiohttp.web
import aiohttp.web_request


def make_app(aiohttp_app):
    async def receive_posts(request: aiohttp.web_request.Request):
        print(request.headers)
        return aiohttp.web.Response()

    def add_routes(the_app):
        the_app.router.add_post('/', receive_posts)

    add_routes(aiohttp_app)
    return aiohttp_app

"""
Starting the app!
"""
app = make_app(aiohttp.web.Application(loop=asyncio.get_event_loop()))

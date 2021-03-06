import asyncio
import time

import aiohttp
import aiohttp.web
import aiohttp.web_request

import config

time_first_request_handled = None
number_of_requests = 0


WHITE, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BLACK = (i + 30 for i in range(8))
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


def make_app(aiohttp_app):
    async def receive_posts(request: aiohttp.web_request.Request):
        """
        Handle reception of posts that would otherwise go to the Facebook Messenger API.
        """
        global time_first_request_handled
        global number_of_requests
        elapsed_time = await get_elapsed_time()
        number_of_requests += 1
        await print_status(elapsed_time, request)
        return aiohttp.web.Response()

    async def get_name(request: aiohttp.web_request.Request):
        """
        Getting the full name
        """
        return aiohttp.web.json_response({
            "first_name": "John",
            "last_name": "Doe",
        })

    async def print_status(elapsed_time, request):
        request_word = "requests" if number_of_requests > 1 else "request"
        requests_per_seconds = f"{COLOR_SEQ % RED}" \
                               f"[{number_of_requests} {request_word} in {round(elapsed_time)}s]" \
                               f"{RESET_SEQ}"
        headers_infos = f"{COLOR_SEQ % YELLOW}" \
                        f"[{request.headers['User-Agent']}]" \
                        f"{RESET_SEQ}"
        request_json = await request.json()
        request_json = f"{COLOR_SEQ % BLUE}" \
                       f"{request_json}" \
                       f"{RESET_SEQ}"
        print(
            f"{requests_per_seconds}"
            f"{headers_infos} "
            f"{request_json}"
        )

    async def get_elapsed_time():
        global time_first_request_handled
        if time_first_request_handled is None:
            time_first_request_handled = time.time()
        elapsed_time = time.time() - time_first_request_handled
        return elapsed_time

    def add_routes(the_app):
        """
        Adding routes to the aiohttp_application
        """
        the_app.router.add_post(f'/{config.API_VERSION}/me/messages', receive_posts)
        the_app.router.add_get(f'/{config.API_VERSION}/{{facebook_id:\d+}}', get_name)

    add_routes(aiohttp_app)
    return aiohttp_app


"""
Starting the app!
"""
app = make_app(aiohttp.web.Application(loop=asyncio.get_event_loop()))

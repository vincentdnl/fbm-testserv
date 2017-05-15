import aiohttp
import asyncio
import json
from collections import defaultdict
# from aiohttp.client_reqrep import ClientResponse


async def web_hook(client: aiohttp.ClientSession, status_count):
    json_data = json.dumps(message())
    headers = {'content-type': 'application/json'}
    async with client.post('http://localhost:8080', data=json_data, headers=headers) as resp:
        status_count[resp.status] += 1


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        status_count = defaultdict(int)
        for index in range(10):
            await web_hook(client, status_count)
        print(dict(status_count))


def message():
    return {
        "object": "page",
        "entry": [
            {
                "id": "PAGE_ID",
                "time": 1458692752478,
                "messaging": [
                    {
                        "sender": {
                            "id": "USER_ID"
                        },
                        "recipient": {
                            "id": "PAGE_ID"
                        },

                        # ...
                    }
                ]
            }
        ]
    }


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

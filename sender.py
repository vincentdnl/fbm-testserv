import asyncio
import json
import time
from collections import defaultdict

import aiohttp


async def web_hook(client: aiohttp.ClientSession, status_count):
    json_data = json.dumps(message())
    headers = {'content-type': 'application/json'}
    async with client.post('http://localhost:8082/', data=json_data, headers=headers) as resp:
        print(resp.text)
        status_count[resp.status] += 1


async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as client:
        status_count = defaultdict(int)
        start_time = time.time()
        for index in range(5000):
            await web_hook(client, status_count)
        stop_time = time.time()
        print(f"---------- TOTAL EXECTUTION TIME: {stop_time - start_time} ----------")
        print(dict(status_count))


def message():
    return {
        "object": "page",
        "entry": [
            {
                "id": "652783874878686",
                "time": 1458692752478,
                "messaging": [
                    {
                        "sender": {
                            "id": "1255799917785059"
                        },
                        "recipient": {
                            "id": "652783874878686"
                        },
                        "message": {
                            "mid": "mid.1457764197618:41d102a3e1ae206a38",
                            "text": "hello, world!",
                            "quick_reply": {
                                "payload": "DEVELOPER_DEFINED_PAYLOAD"
                            }
                        }
                    }
                ]
            }
        ]
    }


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

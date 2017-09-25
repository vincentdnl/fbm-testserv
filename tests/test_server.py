from aiohttp.test_utils import TestClient

import config


async def test_50_messages(
        cli: TestClient,
):
    payload_example = {'recipient': {'id': '1234567891234567'}, 'message': {'text': 'Hello, world!'}}
    payloads = 50*[payload_example]

    for payload in payloads:
        response = await cli.post(f'/{config.API_VERSION}/me/messages', json=payload)
        assert response.status == 200

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


async def test_get_name(
        cli: TestClient,
):
    response = await cli.get(f'/{config.API_VERSION}/123456789')
    assert response.status == 200
    assert await response.json() == {"first_name": "John", "last_name": "Doe"}

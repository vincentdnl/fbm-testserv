import aiohttp.web
import pytest

import server


@pytest.fixture
def test_app(loop):
    return server.make_app(
        aiohttp.web.Application(loop=loop),
    )


@pytest.fixture
def cli(loop, test_client, test_app):
    return loop.run_until_complete(test_client(test_app))

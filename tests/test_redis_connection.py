import pytest
from config.redis_conf import redis_stream, redis_connection as redis


@pytest.mark.asyncio
async def test_db_connection():
    """ Tests if the database
    connection is functioning
    """
    assert redis.ping() == True


@pytest.mark.asyncio
async def test_stream_connection():
    """ Tests if the streams
    connection for ecents pub-sub
    sourcing is functioning
    """
    assert redis_stream.ping() == True

import redis.asyncio.client as redis

ENCODING = "utf-8"
HOST = "atomflare.af"
PORT = 6388

DB_INDEX = 3
STREAM_INDEX = 1

STREAM_URL = f"redis://{HOST}:{PORT}/{STREAM_INDEX}"

redis_stream = redis.Redis.from_url(
    url=STREAM_URL,
    encoding=ENCODING,
    decode_responses=True,
)


DB_URL = f"redis://{HOST}:{PORT}/{DB_INDEX}"

redis_connection = redis.Redis.from_url(
    url=DB_URL,
    encoding=ENCODING,
    decode_responses=True,
)

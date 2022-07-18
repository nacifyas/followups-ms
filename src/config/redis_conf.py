import redis

ENCODING = "utf-8"
HOST = "atomflare.af"
PORT = 6388
DB_INDEX = 1
STREAM_URL = f"redis://{HOST}:{PORT}/{DB_INDEX}"

redis_stream = redis.Redis.from_url(
    url=STREAM_URL,
    encoding=ENCODING,
    decode_responses=True
)
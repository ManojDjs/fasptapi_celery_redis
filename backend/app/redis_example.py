import redis

redis_cli = redis.Redis(
    host='localhost',
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

#Set your key
redis_cli.set('my-first-key', 'code-always')

#Get the value of inserted key
print(redis_cli.get('my-first-key'))
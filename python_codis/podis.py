# -*- coding:utf-8 -*-
import redis
import logging
import traceback

logger = logging.getLogger(__name__)


def redis_getter(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result or None
        except Exception, ex:
            logger.error(traceback.format_exc())
            raise
    return wrapper


def redis_setter(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            return True
        except Exception, ex:
            logger.error(traceback.format_exc())
            raise
    return wrapper


class Podis(object):

    def __init__(self, pool):
        self._connection = redis.StrictRedis(connection_pool=pool)

    @redis_getter
    def ping(self):
        return self._connection.ping()

    @redis_getter
    def get(self, key):
        return self._connection.get(key)

    @redis_setter
    def set(self, key, value):
        self._connection.set(key, value)

    @redis_setter
    def lpush(self, key, *value):
        self._connection.lpush(key, *value)

    @redis_getter
    def lpop(self, key):
        return self._connection.lpop(key)

    @redis_getter
    def lrange(self, key, start, end):
        return self._connection.lrange(key, start, end)

    @redis_setter
    def sadd(self, key, *value):
        self._connection.sadd(key, *value)

    @redis_setter
    def srem(self, key, *value):
        self._connection.srem(key, *value)

    @redis_getter
    def zrange(self,key,start,end):
        return self._connection.zrange(key,start,end)

    @redis_getter
    def zrevrange(self,key,start,end):
        return self._connection.zrevrange(key,start,end,withscores=True)

    @redis_getter
    def zscore(self,key,*value):
        return self._connection.zscore(key,value)

    @redis_setter
    def zadd(self,key,score,*value):
        self._connection.zadd(key,score,value)

    @redis_getter
    def smembers(self, key):
        return self._connection.smembers(key)

    @redis_getter
    def hgetall(self, key):
        return self._connection.hgetall(key)

    @redis_getter
    def hget(self, key, name):
        return self._connection.hget(key, name)

    @redis_getter
    def hkeys(self, key):
        return self._connection.hkeys(key)

    @redis_setter
    def hset(self, key, name, value):
        self._connection.hset(key, name, value)

    @redis_setter
    def hmset(self, name, mapping):
        self._connection.hmset(name, mapping)

    @redis_setter
    def hdel(self, key, name):
        self._connection.hdel(key, name)

    @redis_setter
    def delete(self, *key):
        self._connection.delete(*key)

    # codis不支持
    @redis_getter
    def keys(self, pattern):
        return self._connection.keys(pattern)

    @redis_setter
    def expire(self, key, time):
        return self._connection.expire(key, time)

    @redis_getter
    def ttl(self, key):
        return self._connection.ttl(key)

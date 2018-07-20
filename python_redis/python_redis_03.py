#!/usr/bin/env python
# coding=utf-8
import json

import redis
import time

"""
使用redis操作，使用连接池

redis set 的操作
"""
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

"""
start = time.time()*1000
for i in xrange(100000):
	if (i > 1000) and (i < 9000):
		i = i % 10
	r.sadd('ids_set_01', 1000+i)

print('Game over, use redis set cost time = %s ms' % (time.time()*1000 - start))


start = time.time()*1000
ids_set_02 = r.get('ids_set_02')
if ids_set_02:
	ids_set_02 = eval(ids_set_02)
	ids_set_02 = set(ids_set_02)
else:
	ids_set_02 = set()
for i in xrange(100000):
	if (i > 1000) and (i < 9000):
		i = i % 10
	ids_set_02.add(1000+i)
r.set('ids_set_02', json.dumps(list(ids_set_02)))
print('Game over, use python set cost time = %s ms' % (time.time()*1000 - start))


start = time.time()*1000
for i in xrange(10000000):
	if (i > 1000) and (i < 90000):
		i = i % 10
	r.zadd('ids_set_03', 1000+i, int(time.time()))
print('Game over, use redis zset cost time = %s ms' % (time.time()*1000 - start))
"""


start = time.time()*1000
for i in xrange(100000):
	if (i > 1000) and (i < 9000):
		i = i % 10
	key = 'clp_user_check_in_uids_dev_sg_2018-06-14'
	r.zadd(key, 1000+i, int(time.time()))
print('Game over, use redis zset cost time = %s ms' % (time.time()*1000 - start))


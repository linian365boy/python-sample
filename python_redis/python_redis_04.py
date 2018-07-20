#!/usr/bin/env python
# coding=utf-8
import json

import redis
import time
import sys

"""
使用redis操作，使用连接池

redis set 的操作
"""
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def notify_user(uid):
	'''
	result = 0
	for i in xrange(100):
		result = result + i
	return result
	'''
	pass

'''
start = time.time()*1000
length = r.scard('ids_set_01')
print('ids_set_01 length=%s' % length)
i = 0
while i < length:
	uid = r.spop('ids_set_01')
	i = i + 1
	notify_user(int(uid))

print('Game over, use redis set pop cost time = %s ms' % (time.time()*1000 - start))


start = time.time()*1000
ids_set = r.get('ids_set_02')
print('ids_set_02 size=%s' % (sys.getsizeof(ids_set)))
sets = json.loads(ids_set)
length = len(sets)
print('ids_set_02 length=%s, size=%s' % (length, sys.getsizeof(sets)))
for uid in sets:
	notify_user(int(uid))
print('Game over, use python get cost time = %s ms' % (time.time()*1000 - start))
'''

'''
start = time.time()*1000
ids_set = r.zrange('ids_set_03', 0, -1)
# print('ids_set_03 length=%s, cost time=%s ms' % (len(ids_set), (time.time()*1000 - start)))
for uid in ids_set:
	notify_user(int(uid))
print('Game over, use redis zrange cost time = %s ms' % (time.time()*1000 - start))
'''

start = time.time()*1000
# user page, 1000 per
zset_size = r.zcard('ids_set_03')
loop_size = zset_size/1000 if (zset_size % 1000 == 0) else zset_size/1000 + 1
result_count = 0
for i in xrange(loop_size):
	ids_set = r.zrange('ids_set_03', i*1000, i*1000 + 999)
	# print('ids_set_03 length=%s, size=%s' % (len(ids_set), sys.getsizeof(ids_set)))
	if i == (loop_size-1):
		print('len set = %s' % len(ids_set))
		print('last ids set = %s' % ids_set)
	result_count += len(ids_set)
	for uid in ids_set:
		notify_user(int(uid))
print('Game over, use redis zrange page cost time = %s ms, result_count = %s' % ((time.time()*1000 - start), result_count))

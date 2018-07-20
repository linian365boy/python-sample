#!/usr/bin/env python
# coding=utf-8

import redis

"""
使用redis操作，使用连接池
"""
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')
print(r.get('gender'))


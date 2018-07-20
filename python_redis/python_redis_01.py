#!/usr/bin/env python
# coding=utf-8

import redis

"""
使用redis操作，未使用连接池
redis提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，
并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。

redis连接实例是线程安全的，可以直接将redis连接实例设置为一个全局变量，直接使用。
如果需要另一个Redis实例（or Redis数据库）时，就需要重新创建redis连接实例来获取一个新的连接。
同理，python的redis没有实现select命令。

"""
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('hello', 'niange')
print(r['hello'])
print(r.get('hello'))
print(type(r.get('hello')))

uids = ['hello', 'hello1', 'hello2', 'nima']
values_list = r.mget(uids)
values = {}
for i in xrange(len(uids)):
	value = values_list[i]
	if value is not None:
		values[uids[i]] = value
print(values)

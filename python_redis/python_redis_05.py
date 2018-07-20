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

# r.set('clp_user_check_in_switch_1000', 'on')
user_switch_status = r.get('clp_user_check_in_switch_1000')
if not user_switch_status or user_switch_status == 'on':
	print('on')
else:
	print('off')

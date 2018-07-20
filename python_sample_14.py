#!/usr/bin/env python
# coding=utf-8

import cPickle as pickle
# import pickle
import logging

a = {
	'uid': 123,
	'username': '123',
	'age': 27,
	'email': '123@qq.com'
}

str = pickle.dumps(a, True)

str_obj = pickle.loads(str)
logging.warn('log log info => {str_obj}'.format(str_obj=str_obj))
print(str_obj)
print('-------')
print(type(str_obj))
print('-------')
print(str)


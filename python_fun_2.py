# -*- coding: utf-8 -*-
import json

import python_fun
from decimal import Decimal

if __name__ == '__main__':
	func = u'main'
	func_args = u"(265015, u'test')"
	func_kwargs = u"{'age': 34, 'department': u'niubi'}"
	func_name = getattr(python_fun, func)
	func_result = func_name(*eval(func_args), **eval(func_kwargs))
	print(func_result)

	func = u'main_2'
	func_args = u"(2343565, Decimal('1.5896'))"
	func_kwargs = u"{'age': 34, 'department': u'niubi'}"
	func_name = getattr(python_fun, func)
	func_result = func_name(*eval(func_args), **eval(func_kwargs))
	print(func_result)

	str = '%s_%s' % ('3453453454', 56456456)
	print(str)

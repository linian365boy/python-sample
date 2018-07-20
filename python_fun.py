# -*- coding: utf-8 -*-
from decimal import Decimal


def main(uid, username, **kwargs):
	age = kwargs.get('age')
	department = kwargs.get('department')
	str = ('%s_%s_%s_%s' % (uid, username, age, department))
	return str


def main_2(uid, coins, **kwargs):
	str_coins = str(coins)
	print('coins str=%s' % str_coins)
	str_2 = ('%s_%s' % (uid, coins))
	return str_2


if __name__ == '__main__':
	result = main(1, 'rfv', age=34, department='niubi')
	print(result)
	result = main(1, 'rfv')
	print(result)

	result = main_2(2343565, Decimal.from_float(1.346).quantize(Decimal('0.00')))
	print(result)

	'''
	func = u'main'
	func_args = (265015, u'test')
	func_kwargs = {'age': 34, 'department': u'niubi'}
	func(func_args, func_kwargs)
	'''
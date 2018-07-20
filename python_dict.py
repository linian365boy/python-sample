# -*- coding: utf-8 -*-


def main():
	result = [{
		'uid': 1,
		'name': 'niange',
		'age': 23
	}, {
		'uid': 2,
		'name': 'lily',
		'age': 22
	}]
	for x in result:
		del x['uid']
	for x in result:
		print(x)
	print('result={}'.format(result))
	return result


if __name__ == '__main__':
	result_obj = main()
	print('main result_obj={}'.format(result_obj))
	print(next(iter(result_obj)))
	print(result_obj[0])

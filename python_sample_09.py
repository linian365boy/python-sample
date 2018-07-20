# -*- coding: utf-8 -*-


def package_page_param(data):
	try:
		page_size = data['page_size']
	except KeyError:
		page_size = 10
	try:
		page_no = data['page_no']
	except KeyError:
		page_no = 1
	start_index = (page_no - 1) * page_size
	end_index = start_index + page_size
	return start_index, end_index


if __name__ == '__main__':
	data_dict = dict()
	tuple_result = (package_page_param(data_dict))
	print(tuple_result[0])
	print(tuple_result[1])

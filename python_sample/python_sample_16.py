import time

ranks = [
	{'order': 1, 'score': '3.69', 'username': 'muckky'},
	{'order': 2, 'score': '3.60', 'username': 'prarakorn'},
	{'order': 3, 'score': '3.42', 'username': 'm.chubby'},
	{'order': 4, 'score': '3.37', 'username': 'ravathai'},
	{'order': 5, 'score': '3.37', 'username': 'pimpisutnat'},
	{'order': 6, 'score': '3.32', 'username': 'prapojkhyn'},
	{'order': 7, 'score': '3.24', 'username': 'aemru'},
	{'order': 8, 'score': '3.21', 'username': 'cookiesandcars2.th'}
	]

print([i for i in range(0, len(ranks)) if i % 3 == 0])

for j in [i for i in range(0, len(ranks)) if i % 3 == 0]:
	if float(ranks[j]['score']) % 100 != 0:
		print(ranks[j]['score'])




def convert_to_today_timestamp(time_str):
	"""
	:param time_str: format:%H:%M
	:return: now_timestamp
	"""
	time_struct = time.localtime()
	notify_date_time_str = time.strftime('%Y-%m-%d', time_struct)
	notify_date_time_str = notify_date_time_str + ' ' + time_str
	return int(time.mktime(time.strptime(notify_date_time_str, '%Y-%m-%d %H:%M')))


if __name__ == '__main__':
	date = convert_to_today_timestamp("08:00")
	print(date)

	now_timestamp = int(time.time())

	if now_timestamp >= date:
		print('niubi')
	else:
		print('fuck')

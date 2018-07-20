import datetime


def truncate_date_string(now=None):
	if type(now) is int or type(now) is float:
		now = datetime.datetime.fromtimestamp(now)
	if not now:
		now = datetime.datetime.now()
	return now.strftime('%Y-%m-%d')


def main(now):
	yes = now - 24 * 60 * 60
	print('yes=%s' % truncate_date_string(yes))
	tom = now + 24 * 60 * 60
	print('tom=%s' % truncate_date_string(tom))


if __name__ == '__main__':
	now = 1533107096
	main(now=now)

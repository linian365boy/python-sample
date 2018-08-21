import json
import time
import datetime
import cPickle as pickle


def truncate_date_string(now=None):
	if type(now) is int or type(now) is float:
		now = datetime.datetime.fromtimestamp(now)
	if not now:
		now = datetime.datetime.now()
	return now.strftime('%Y-%m-%d')



def rollback_check_in_v2(today=None):
	if not today:
		today == time.time()
	checkin_day_dict = {'2018-09-12':'34', '2018-09-13':'24', '2018-09-14':'44', '2018-08-17': '67'}
	del checkin_day_dict['2018-09-13']
	print(json.dumps(checkin_day_dict))



if __name__ == '__main__':
	#rollback_check_in_v2(time.time())
	rollback_check_in_v2()
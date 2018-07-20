from celery.schedules import crontab_parser

r = crontab_parser(23, 0).parse('9-12, 20')
print(r)

data = {
		'status': 'error',
		'message': 'Invalid Minute'
	}

print(data.get('status'))
print(data['status'])

data['status'] = 'success'
print(data)

dict_s = {
	'datetime': {
		'minute': 0,
		'hour': 20
	},
	'switch_status': 0
}

result = type(dict_s.get('switch_status'))
print(result)

result = dict_s.get('switch_status')
print(result)
print(result == 0)

print(int(result) == 0)


hour = '20'
print(hour < 0)
print(hour > 23)

print(int(hour) < 0)
print(int(hour) > 23)


logid = '442278481615295684518278623'
print(logid)
print(int(logid))

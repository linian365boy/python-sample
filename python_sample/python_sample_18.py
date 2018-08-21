import time


class Request(object):
	def __init__(self):
		pass

request = Request()

deviceinfo = {
			"deviceid": '3453',
			"devicetype": 'fff'
		}

#setattr(request, 'deviceinfo', deviceinfo)
now = time.time()

result = {
		'success': False,
		'userid': 234,
		'username': 'niange',
		'mtime': now,
		'logid': '4234234234234234234',
		'redeemid': 12312,
		'timestamp': now,
		'partner': True
	}

print(getattr(request, 'deviceinfo', {}))

result.update(getattr(request, 'deviceinfo', {}))

print(result)

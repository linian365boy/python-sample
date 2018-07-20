import redis


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)


def get_partner_code(code):
	if code:
		for code_obj in code:
			res = r.setnx('test.partner_%s' % code_obj['code'], 1)
			if res:
				return code_obj
	return None


if __name__ == '__main__':
	result = r.set('key_hello', 'value_hello', nx=True)
	print('3=%s' % result)
	result = r.set('key_hello', 'value_hello', nx=True)
	print('4=%s' % result)

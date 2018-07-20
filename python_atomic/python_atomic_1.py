import json
import threading
import redis
import time

from python_atomic.atomic_add import addCount

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

PARTNER_CODE_REDEMPTION = 'partner_code_redemption_%s'

default_partner_id = 1678

lock = threading.Lock()

def set_redeem_partner_code(userid):
	redeem_list = \
		[{
			'partner_id': default_partner_id,
			'redeem_count': 0
		}, {
			'partner_id': default_partner_id + 1,
			'redeem_count': 0
		}, {
			'partner_id': default_partner_id + 2,
			'redeem_count': 0
		}, {
			'partner_id': default_partner_id + 3,
			'redeem_count': 0
		}, {
			'partner_id': default_partner_id + 4,
			'redeem_count': 0
		}]
	r.set(PARTNER_CODE_REDEMPTION % userid, json.dumps(redeem_list), 14*24*60*60)


redeem_partner_count = addCount()
def redeem_partner_code(partner_id, userid):
	return redeem_partner_count.dosomething(partner_id, userid)


if __name__ == '__main__':
	# set_redeem_partner_code(633)
	# redeem_list = redeem_partner_code(default_partner_id+3, 633)
	# print(redeem_list)
	start = int(time.time() * 1000)
	thread_size = 1000
	ts = []
	for i in range(thread_size):
		t = threading.Thread(target=redeem_partner_code, args=(default_partner_id + 3, 633))
		ts.append(t)

	for m in ts:
		m.start()

	for n in ts:
		n.join()

	print('Game Over, cost time=> %s ms' % (int(time.time() * 1000) - start))
	redemption = r.get(PARTNER_CODE_REDEMPTION % 633)
	redeem_list = json.loads(redemption)
	for redeem_dict in redeem_list:
		if int(redeem_dict['partner_id']) == int(default_partner_id + 3):
			print('redeem count=> %s' % redeem_dict['redeem_count'])

	for redeem_dict in redeem_list:
		if int(redeem_dict['partner_id']) == int(default_partner_id + 3):
			redeem_dict['redeem_count'] = 0
	r.set(PARTNER_CODE_REDEMPTION % 633, json.dumps(redeem_list), 14 * 24 * 60 * 60)
	print('redis data is reset')

import json
import threading
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
PARTNER_CODE_REDEMPTION = 'partner_code_redemption_%s'


class addCount(object):

	def __init__(self):
		self._lock = threading.RLock()

	def dosomething(self, partner_id, userid):
		with self._lock:
			redemption = r.get(PARTNER_CODE_REDEMPTION % userid)
			if redemption:
				redeem_list = json.loads(redemption)
				flag = False
				for redeem_dict in redeem_list:
					if int(redeem_dict['partner_id']) == int(partner_id):
						redeem_dict['redeem_count'] = int(redeem_dict['redeem_count']) + 1
						flag = True
				if not flag:
					redeem_list.append({'partner_id': partner_id, 'redeem_count': 1})
				r.set(PARTNER_CODE_REDEMPTION % userid, json.dumps(redeem_list), 14 * 24 * 60 * 60	)
		return redeem_list

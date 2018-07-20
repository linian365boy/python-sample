import time
from time import struct_time


def isVaildDate(date):
	datetime = None
	try:
		datetime = time.strptime(date, "%H:%M:%S")
		return datetime
	except:
		return datetime


result = isVaildDate('23:34:56')
print(result)
print(result.tm_min)
print(result.tm_hour)


result = None
if result == 'on':
	print('heh')
else:
	print('nima')



meta_obj = None
if meta_obj and meta_obj['meta_value'] == 'on':
	print('111')
else:
	print('fuck')


nowtime = time.strftime('%H:%M')
print(nowtime)


def test():
	meta_info_list = []
	for i in range(4):
		meta_info = {
			'meta_key': 'meta_key'+str(i),
			'meta_value': 'meta_value'+str(i)
		}
		meta_info_list.append(meta_info)
	return meta_info_list


result = test()
print(result)

g = lambda x, y: x['meta_value'] if x['meta_key'] == y else None

meta_value_0 = None
meta_value_1 = None
meta_value_2 = None
meta_value_3 = None

print('%s - %s - %s - %s' % (meta_value_0, meta_value_1, meta_value_2, meta_value_3))

LIVE = False
REGION = 'SG'

if LIVE:
	COINS_LANDING_PAGE_URL = 'https://%(domain_suffix)s/%(shopee_coins)s/'
else:
	COINS_LANDING_PAGE_URL = 'https://%(env)s.%(domain_suffix)s/%(shopee_coins)s/'

if REGION.lower() == 'id':
	COINS_LANDING_PAGE_URL = COINS_LANDING_PAGE_URL % {
		'shopee_coins': 'koin-shopee'
	}
else:
	COINS_LANDING_PAGE_URL = COINS_LANDING_PAGE_URL % {
		'env': 'ss',
		'domain_suffix': 'fg',
		'shopee_coins': 'shopee-coins'
	}

print(COINS_LANDING_PAGE_URL)
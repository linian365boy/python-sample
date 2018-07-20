import time

import functools

import binascii

import sys
from random import randint

LAG_SEC = 3
DEFAULT_TIME_OUT = 60 * 5


def get_banners(now):
	return [x for x in db_get_banners()]


def lag_sec(now):
	now = (now / LAG_SEC + 1) * LAG_SEC
	return now


def db_get_banners(now=None):
	if not now:
		now = int(time.time())
	now = lag_sec(now)
	return _get_banners(now)


def LOCAL_CACHE(timeout=2, nkwargs=None):
	def _func(func):
		@functools.wraps(func)
		def wrap(*args, **kwargs):
			now = int(time.time())
			pr
			keys = [func.__name__, ]
			if not nkwargs:
				keys.extend(args)
				keys.extend(kwargs.values())
			else:
				for k,v in kwargs.iteritems():
					if k in nkwargs:
						keys.append(v)
			key = '_'.join([binascii.hexlify(k.encode('utf-8')) if type(k) == unicode else str(k) for k in keys])
			cache_data = getattr(func, key, None)
			cache_data_ctime = getattr(func, key.join('_timeout'), 0)
			cache_data_condition = getattr(func, key.join('_condition'), False)
			if now < (cache_data_ctime + timeout):
				if cache_data is None:
					raise None
				return cache_data
			elif cache_data_condition:
				if cache_data is None:
					raise None
				return cache_data
			else:
				setattr(func, key.join('_condition'), True)
				try:
					value = func(*args, **kwargs)
					time.sleep(5)
				except Exception as e:
					setattr(func, key.join('_condition'), False)
					_, ex, traceback = sys.exc_info()
					raise ValueError, e.args, traceback
				finally:
					setattr(func, key.join('_condition'), False)
				if value is not None:
					setattr(func, key, value)
					setattr(func, key.join('_timeout'), now)
				return value
		return wrap
	return _func


@LOCAL_CACHE(timeout=LAG_SEC*2)
def _get_banners(now):
	# TODO
	banners = []
	#banners = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]

	return \
		[
			{
				'id': b['id'],
			} for b in banners
		]
	time.sleep(2)
	# return None


if __name__ == '__main__':
	import threading

	now = int(time.time())
	threads = []
	for i in range(1000000):
		threads.append(threading.Thread(target=get_banners(now), name='get_banners_'+str(i)))

	for t in threads:
		t.start()

	for t in threads:
		t.join()
		print('thread %s end' % t.name)


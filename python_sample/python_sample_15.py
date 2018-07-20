import time
import functools
import binascii
from gevent.event import Event
import sys
from random import randint

LAG_SEC = 3
DEFAULT_TIME_OUT = 60 * 5


def __filter_right_cycle():
	cycle = get_cycle_days()
	return cycle


def lag_sec(now):
	now = (now / LAG_SEC + 1) * LAG_SEC
	return now


def LOCAL_LOCKED_CACHE(timeout=10, nkwargs=None):
	def _func(func):
		@functools.wraps(func)
		def wrap(*args, **kwargs):
			now = time.time()
			keys = [func.__name__, ]
			if not nkwargs:
				keys.extend(args)
				keys.extend(kwargs.values())
			else:
				for k,v in kwargs.iteritems():
					if k in nkwargs:
						keys.append(v)
			key = '_'.join([binascii.hexlify(k.encode('utf-8')) if type(k) == unicode else str(k) for k in keys])
			evt = getattr(func, 'evt'+key, None)
			if not evt:
				evt = Event()
				setattr(func, 'evt'+key, evt)
			else:
				if not evt.is_set():
					evt.wait(timeout=0.1)
			cache_data = getattr(func, key, None)
			cache_data_ctime = getattr(func, key.join('_timeout'), 0)
			cache_data_condition = getattr(func, key.join('_condition'), False)
			if now < (cache_data_ctime + timeout):
				return cache_data
			elif cache_data_condition:
				# now, it shall avoid. unless func return last more than 100ms
				return cache_data
			else:
				setattr(func, key.join('_condition'), True)
				try:
					value = func(*args, **kwargs)
				except Exception as e:
					setattr(func, key.join('_condition'), False)
					_, ex, traceback = sys.exc_info()
					raise ValueError, e.args, traceback
				finally:
					setattr(func, key.join('_condition'), False)
					evt.set()
				if value is not None:
					setattr(func, key, value)
					setattr(func, key.join('_timeout'), now)
				return value
		return wrap
	return _func


@LOCAL_LOCKED_CACHE(timeout=3)
def get_cycle_days():
	return []


if __name__ == '__main__':
	import threading
	now = int(time.time())
	threads = []
	for i in range(10):
		threads.append(threading.Thread(target=__filter_right_cycle(), name='filter_right_cycle_' + str(i)))

	for t in threads:
		t.start()

	for t in threads:
		t.join()
		print('thread %s end' % t.name)

import functools

import binascii

from repoze import lru

LOCAL_CACHE_NAME = '__LOCAL_CACHE__'
LOCAL_CACHE_TIME_NAME = '__LOCAL_CACHE_CTIME__'

DEFAULT_LRU = lru.ExpiringLRUCache(500000, 300)
COOLDOWN_LRU = lru.ExpiringLRUCache(500000, 1)

LRU_CACHES = {'default': DEFAULT_LRU, 'cool-down': COOLDOWN_LRU}


def CACHE(lru_name='default', lru_size=5000, timeout=300):
	def _func(func):
		@functools.wraps(func)
		def wrap(*args, **kwargs):
			keys = [func.__name__, ]
			keys.extend(args)
			keys.extend(kwargs.values())
			key = '_'.join([binascii.hexlify(k.encode('utf-8')) if type(k) == unicode else str(k) for k in keys])
			# print('key=%s' % key)
			if lru_name in LRU_CACHES:
				lru_cache = LRU_CACHES.get(lru_name)
				value = lru_cache.get(key)
			else:
				lru_cache = lru.ExpiringLRUCache(lru_size, timeout)
				LRU_CACHES[lru_name] = lru_cache
				value = None
			if value:
				pass
			else:
				value = func(*args, **kwargs)
				if value is not None:
					lru_cache.put(key, value, timeout)
			if value is None:
				print('haha is you...')
			return value
		return wrap
	return _func

banners = [dict, ]
@CACHE(timeout=300)
def get_banners(now=None):
	dict = {'id': 1, 'name': 'good'}
	banners = [dict, ]
	return [{'id': b.get('id'), 'name': b.get('name')} for b in banners]


import gevent
list = [gevent.spawn(get_banners, i) for i in xrange(0, 50)]
gevent.joinall(list)
list.extend(gevent.spawn(get_banners, m) for m in xrange(0, 50))
banners = None
gevent.joinall(list)
list.extend(gevent.spawn(get_banners, m) for m in xrange(0, 50))
gevent.joinall(list)
banners = None
list.extend(gevent.spawn(get_banners, m) for m in xrange(0, 50))
gevent.joinall(list)
list.extend(gevent.spawn(get_banners, m) for m in xrange(0, 50))
gevent.joinall(list)
print('back..1')




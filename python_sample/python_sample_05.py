from repoze import lru

DEFAULT_LRU = lru.ExpiringLRUCache(500000, 300)
COOLDOWN_LRU = lru.ExpiringLRUCache(500000, 1)
LRU_CACHES = {'default': DEFAULT_LRU, 'cool-down': COOLDOWN_LRU}


lru_name = 'default'
if lru_name in LRU_CACHES:
	print('enter default cache.')
	lru_cache = LRU_CACHES.get(lru_name)
	value = lru_cache.get('123123')
	print('value=%s' % value)
else:
	print('enter other cache.')

if value:
	pass
else:
	lru_cache.put('123123', [], 200)
	value = lru_cache.get('123123')
	print('value=====%s' % value)


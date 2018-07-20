import time
from elasticsearch import Elasticsearch, Connection

ELASTICSEARCH_COINS_CONFIG = [
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	]

global_es_client = Elasticsearch(ELASTICSEARCH_COINS_CONFIG)

start = int(time.time())
try:
	global_es_client.index(index="hello-2011-09-24", doc_type='type2', id=None, body={'hello': 'world'})
finally:
	print('cost time => %s' % (int(time.time()) - start))


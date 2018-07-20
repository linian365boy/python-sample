import time
from elasticsearch import Elasticsearch, Connection

ELASTICSEARCH_COINS_CONFIG = [
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	{'host': '127.0.0.2', 'port': '9200'},
	]

global_es_client = Elasticsearch(ELASTICSEARCH_COINS_CONFIG, max_retries=3)

start = int(time.time())
global_es_client.index(index="hello-2011-09-23", doc_type='type2', id=None, body={})
print('cost time => %s' % (int(time.time()) - start))


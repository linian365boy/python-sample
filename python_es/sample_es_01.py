from elasticsearch import Elasticsearch

ELASTICSEARCH_COINS_CONFIG = [
	{'host': '10.65.228.81', 'port': '9200'},
	{'host': '10.65.228.82', 'port': '9200'},
	{'host': '10.65.228.83', 'port': '9200'},
	{'host': '10.65.228.84', 'port': '9200'},
	{'host': '10.65.228.85', 'port': '9200'},
	]


global_es_client = Elasticsearch(ELASTICSEARCH_COINS_CONFIG)

print(global_es_client.__hash__())
print(id(global_es_client))
print('234234sf'+str(id(global_es_client)))

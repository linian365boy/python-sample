from datetime import datetime
import time
import pytz
from elasticsearch import Elasticsearch

ELASTICSEARCH_COINS_CONFIG = [
	{'host': '127.0.0.1', 'port': '9200'},
	]


global_es_client = Elasticsearch(ELASTICSEARCH_COINS_CONFIG)
now = time.time()
now_date = datetime.fromtimestamp(now, pytz.timezone('Asia/Singapore'))
year_month_day = now_date.strftime('%Y%m%d')


def es_index():
	index = "gameabr_id_dev_32_190_group.%s" % year_month_day
	body = {
		"eventid": 32,
		"sessionid": 190,
		"group_id": "13066202042740015294893051552638",
		"group_member": [295739, 2195738, 245739, 124939],
		"group_member_count": 4,
		"group_full": False
	}
	result = global_es_client.index(index=index, body=body, doc_type='default')
	return result


if __name__ == '__main__':
	result = es_index()
	print('es index result=%s' % result)

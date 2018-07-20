import time
from datetime import datetime
import pytz
from elasticsearch import Elasticsearch

ELASTICSEARCH_COINS_CONFIG = [
	{'host': '127.0.0.1', 'port': '9200'},
	]
es = Elasticsearch(ELASTICSEARCH_COINS_CONFIG)
now = time.time()
now_date = datetime.fromtimestamp(now, pytz.timezone('Asia/Singapore'))
year_month_day = now_date.strftime('%Y%m%d')


def es_index(index, index_type, logid, body):
	res = es.index(index=index, doc_type='default', id=logid, body=body)
	return res


if __name__ == '__main__':
	joined_users = [156, 267]
	logid = 'thisMyTestLogId'
	joined_users.append(567)
	joined_users.append(789)
	joined_users.append(456)
	body = {
		'group_id': '23423523242342342',
		'group_member': joined_users,
		'group_members_num': len(joined_users),
		'group_status': 'non_full' if len(joined_users) < 5 else 'group_full'
	}
	index = "gameabr_id_dev_32_190_group.%s" % year_month_day
	res = es_index(index, None, logid, body)
	print(res)

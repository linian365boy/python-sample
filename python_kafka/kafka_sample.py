import time
from pykafka import KafkaClient

'''
client = KafkaClient(hosts='kafka-shopee-nonlive-10-65-132-21:9092,'
						   'kafka-shopee-nonlive-10-65-132-22:9092,'
						   'kafka-shopee-nonlive-10-65-132-23:9092')
'''

client = KafkaClient(hosts='127.0.0.1:9092')
topics = client.topics
# pykafka.cluster.TopicDict
print(topics)
topic = client.topics['test_kafka']

start = int(time.time() * 1000)
with topic.get_sync_producer() as producer:
	for i in range(4):
		producer.produce('test message ' + str(i ** 2))
print('1 cost time => {time} ms'.format(time=int(time.time() * 1000) - start))

start = int(time.time() * 1000)
with topic.get_producer(delivery_reports=True) as producer:
	count = 0
	while True:
		count += 1
		producer.produce('test msg', partition_key='{}'.format(count))
		# adjust this or bing lots of RAM
		if count % 10 ** 5 == 0:
			while True:
				try:
					msg, exc = producer.get_delivery_report(block=False)
					if exc is not None:
						print 'Failed to deliver msg {}:{}'.format(msg.partition_key, repr(exc))
					else:
						print 'Successfully delivered msg {}'.format(msg.partition_key)
				except Exception as e:
					break
print('2 cost time => {time} ms'.format(time=int(time.time() * 1000) - start))
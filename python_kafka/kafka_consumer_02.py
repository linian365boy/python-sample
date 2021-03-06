from pykafka import KafkaClient
from pykafka.common import OffsetType

client = KafkaClient(hosts='127.0.0.1:9092', broker_version='1.0.0')
topic = client.topics['auto_create_kafka_topic']

consumer = topic.get_simple_consumer(
	consumer_group="test_mygroup",
	auto_offset_reset=OffsetType.EARLIEST,
	reset_offset_on_start=False,
	consumer_timeout_ms=5000
)

for message in consumer:
	if message is not None:
		print('offset=%s, msg=%s' % (message.offset, message.value))

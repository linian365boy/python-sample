from __future__ import absolute_import, unicode_literals

from celery import Celery


app = Celery('myTask1', backend='rpc://', broker='amqp://guest:guest@localhost:5672//', include=['celery_sample.tasks'])

app.conf.update(
	result_expires=3600
)


if __name__ == '__main__':
	app.start()
	from celery_sample.tasks import add
	result = add.s(4, 5)





import gevent
from gevent.lock import BoundedSemaphore

sem = BoundedSemaphore(2)


def worker(n):
	sem.acquire(timeout=5)
	print('Worker %i acquired semaphore' % n)
	gevent.sleep(20)
	sem.release()
	print('Worker %i released semaphore' % n)


gevent.joinall([gevent.spawn(worker, i) for i in xrange(0, 6)])

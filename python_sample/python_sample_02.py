import time

TIMEOUT = 300
now_time = int(time.time())
print('now_time=%s, type=%s' % (now_time, type(now_time)))

if TIMEOUT:
	now = now_time / TIMEOUT * TIMEOUT
	print('enter timeout type=%s' % type(now))
else:
	now = now_time
	print('not enter timeout')

print('now time=%s' % now)

print(type(9/5))

print(type(9.0/5))

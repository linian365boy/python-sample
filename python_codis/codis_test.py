import time
import threading
from codis_pool import codis_config
from codis_pool import CodisPool, RoundRobinPickUp


codis_pool1 = CodisPool(codis_config)
print '------1-------'
pick_up1 = RoundRobinPickUp()
print '------2-------'
codis_pool2 = CodisPool(codis_config)
print '------3-------'
pick_up2 = RoundRobinPickUp()
print '------4-------'


def func(i):
    for i in range(10):
        podis1 = codis_pool1.get_connection(pick_up=pick_up1)
        podis2 = codis_pool2.get_connection(pick_up=pick_up2)
        podis1.delete(i)
        podis2.delete(i)
        time.sleep(1)


thread_list = []
for i in range(100):
    thread_list.append(threading.Thread(target=func, args=[i]))

for thread in thread_list:
    thread.setDaemon(True)
    thread.start()

time.sleep(300)

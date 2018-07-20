# -*- coding:utf-8 -*-
import abc
import uuid
import time
import logging
import traceback
import threading
import redis
from podis import Podis

logger = logging.getLogger(__name__)


class CodisPool(object):

    def __init__(self, codis_config):
        self._pool_shards = []
        self._availables = []
        self._connection = None
        self._create_pool(codis_config)
        self._check_available_backgroud()

    def _check_available_backgroud(self):
        bg = Background(self._check_pool_shards)
        bg.start()

    def _create_pool(self, codis_config):
        address_list = codis_config.get('addrs').split(',')
        for address in address_list:
            host = address.split(':')[0]
            port = address.split(':')[1]
            self._pool_shards.append(
                Podis(
                    redis.ConnectionPool(
                        host=host, port=port, db=0,
                        password=codis_config.get('password'),
                        max_connections=codis_config.get('max_connections')
                    )
                )
            )
            self._availables.append(True)
        if len(self._pool_shards) == 0:
            logger.error('创建codis链接池失败')
            raise Exception('创建codis链接池失败')

    def _check_pool_shards(self):
        while True:
            self._pool_shards_is_available()

    def _pool_shards_is_available(self, retry_num=3):
        i = 0
        for pool in self._pool_shards:
            try:
                retry = retry_num
                go_on = True
                while go_on and retry > 0:
                    try:
                        pong = pool.ping()
                        if not pong:
                            retry -= 1
                        else:
                            go_on = False
                    except Exception, ex:
                        retry -= 1
                        raise
                    finally:
                        time.sleep(1)
                if retry <= 0:
                    self._availables[i] = False
                else:
                    self._availables[i] = True
            except Exception, ex:
                logger.error(traceback.format_exc())
            finally:
                i += 1

    def _get_available_shards(self):
        i = 0
        available_shards = []
        for shard in self._pool_shards:
            if self._availables[i]:
               available_shards.append(shard)
            i += 1
        return available_shards

    def get_connection(self, pick_up=None):
        if isinstance(pick_up, PickUp):
            codisPool = pick_up.pick_up(self._get_available_shards())
        else:
            pick_up = RandomPickUp()
            codisPool = pick_up.pick_up(self._get_available_shards())
        return codisPool

    def get_pool_shards(self):
        return self._pool_shards

    def get_availables(self):
        return self._get_available_shards()


class Background(object):
    def __init__(self, target, daemon=True):
        self.daemon = daemon
        self.thread = threading.Thread(target=target)

    def start(self):
        self.thread.setDaemon(self.daemon)
        self.thread.start()


class PickUp(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def pick_up(self, pool_list):
        return


class RandomPickUp(PickUp):
    def __init__(self):
        PickUp.__init__(self)

    def pick_up(self, pool_list):
        pool_size = len(pool_list)
        index = abs(hash(uuid.uuid4())) % pool_size
        pool = pool_list[index]
        print "RandomPickUp, 拿到第", index, "个pool"
        return pool


class RoundRobinPickUp(PickUp):

    def __init__(self):
        PickUp.__init__(self)
        self.index = 0
        self.round_robin_lock = threading.Lock()

    def pick_up(self, pool_list):
        with self.round_robin_lock:
            pool_size = len(pool_list)
            self.index += 1
            index = abs(self.index) % pool_size
            pool = pool_list[index]
            print "RoundRobinPickUp, 拿到第", index, "个pool"
            return pool


codis_config = {
    'addrs': '100.90.186.47:3000,100.90.187.33:3000'
}

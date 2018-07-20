# -*- coding: utf-8 -*-
import cgi


def hello(str):
    try:
        str['nima']
    except KeyError:
        pass
    print('heheda')


if __name__ == '__main__':
    str1 = cgi.escape('353dfae<a3>234<html>w2356456@#@&$=53')
    print(str1)
    str1 = {'hh':234}
    hello(str1)

    print('hehe'+str(2))
# -*- coding: utf-8 -*-
import json

user_dict = dict()
user_dict['uid'] = 1231
user_dict['username'] = 'heheda'

str = json.dumps(user_dict)

if __name__ == '__main__':
    print(str)

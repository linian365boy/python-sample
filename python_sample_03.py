# -*- coding: utf-8 -*-
import json

json_str = '[{"pk": 5, "model": "shopee_partylib.activity", "fields": {"status": 0, "type_name": "testda2", "addr": "\u5e7f\u4e1c\u7701\u6df1\u5733\u5e02\u5b9d\u5b89\u533a", "title": "\u6d3b\u52a85", "start_time": 1522545010, "type_id": 2, "end_time": 1524681010, "description": "test play activity234"}}]'

obj = json.loads(json_str)[0]

fields = obj['fields']

status = fields['status']

if __name__ == '__main__':
    print(fields)
    print(type(fields))
    print(status)



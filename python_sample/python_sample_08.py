import time

cmd_table = {}

cmd_table[7] = 'niuma'

cmd_table['7'] = 'niuma7'


print(cmd_table['7'])


print(cmd_table[7])

xs = [{'number':1, 'value':'ONE'}, {'number':2, 'value':'TWO'}, {'number':3, 'value':'THREE'}]
result = {int(x['number']) : x['value'] for x in xs}

print('keys length=%s' % result.keys())

print(result[1])

print(result[2])

print(result[3])

now = int(time.time())
print now

LAG_SEC = 3

def lag_sec(now):
	'welcome to the future'
	now = (now / LAG_SEC + 1) * LAG_SEC
	return now

result_01 = lag_sec(now)
print(result_01)

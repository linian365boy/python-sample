#!/usr/bin/env python
# coding=utf-8
import time

import MySQLdb


def connectdb():
	print('connect to mysql server')
	db = MySQLdb.connect('localhost', 'root', 'root', 'party_db')
	print('connect success.')
	return db


def querydb(db):
	cursor = db.cursor()
	sql = '''SELECT `activity_tab`.`id`, `activity_tab`.`title`, `activity_tab`.`start_time`, 
`activity_tab`.`end_time`, `activity_tab`.`status`, `activity_tab`.`type_id`, `activity_tab`.`type_name` 
FROM `activity_tab` WHERE (`activity_tab`.`status` = 1  AND `activity_tab`.`start_time` < 1523948903  
AND `activity_tab`.`end_time` > 1523948903 ) ORDER BY `activity_tab`.`id` DESC LIMIT 10;'''
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		return results
	except:
		print('Error to fetch data')
		return None


def closedb(db):
	db.close()


def main():
	db = connectdb()
	start_time = time.time() * 1000
	result = querydb(db)
	print('end cost time=>{time} ms'.format(time=(time.time() * 1000 - start_time)))
	print(result)
	closedb(db)


if __name__ == '__main__':
	print('start.....')
	main()

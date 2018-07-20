#!/usr/bin/env python
# coding=utf-8

"""
python连接mysql party_db，并且插入数据
"""
import random
import time

import MySQLdb


def connectdb():
	print('connect to mysql server')
	db = MySQLdb.connect('localhost', 'root', 'root', 'party_db')
	print('connect success.')
	return db


def insert_activity_db(db):
	# get cursor
	cursor = db.cursor()
	sql = """insert into activity_tab values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
	param = []
	for i in xrange(1, 1500000):
		now = int(time.time())
		end = now + 24*60*60*30
		param.append(['activity title %s' % i, now+random.randint(0, 1500000), end+random.randint(0, 1500000),
		              'shenzhen baoan addr %s' % i,
		              'activity description %s' % i,
		              1,
		              random.randint(1,15),
		              'typename %s' % random.randint(1,20),
		              'niange'])
	try:
		cursor.executemany(sql, param)
		db.commit()
		print('all data insert success.')
	except Exception as e:
		print('rollback=>{args}, message=>{message}'.format(args=e.args, message=e.message))
		db.rollback()


def insert_user_db(db):
	# get cursor
	cursor = db.cursor()
	sql = """insert into user_tab values(null,%s,%s,%s,%s,%s,%s,%s,%s,null)"""
	param = []
	for i in xrange(1, 10000):
		now = int(time.time())
		param.append(['niange%s' % i, 'cfcd208495d565ef66e7dff9f98764da', '%s@s.com' % i,
		              'upload/user/images/default.jpg',
		              0,
		              now,
		              0,
		              1])
	try:
		cursor.executemany(sql, param)
		db.commit()
		print('all data insert success.')
	except Exception as e:
		print('rollback=>{args}, message=>{message}'.format(args=e.args, message=e.message))
		db.rollback()


def querydb(db):
	cursor = db.cursor()
	sql = 'SELECT * FROM Student'
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			ID = row[0]
			Name = row[1]
			print('ID=>{id}, name=>{name}'.format(id=ID, name=Name))
	except:
		print('Error to fetch data')


def closedb(db):
	db.close()


def main():
	db = connectdb()
	insert_activity_db(db)
	# insert_user_db(db)
	closedb(db)


if __name__ == '__main__':
	start_time = time.time()*1000
	print('start.....')
	main()
	print('end cost time=>{time} ms'.format(time=(time.time()*1000-start_time)))

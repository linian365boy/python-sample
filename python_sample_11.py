#!/usr/bin/env python
# coding=utf-8

"""
python连接mysql
"""

import MySQLdb
# import mysql.connector


def connectdb():
	print('connect to mysql server')
	db = MySQLdb.connect('localhost', 'root', 'root', 'party_db')
	print('connect success.')
	return db


def createtable(db):
	# get cursor
	cursor = db.cursor()
	cursor.execute('DROP TABLE IF EXISTS Student')
	sql = """CREATE TABLE Student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )"""
	cursor.execute(sql)


def insertdb(db):
	# get cursor
	cursor = db.cursor()
	sql = """INSERT INTO Student
         VALUES ('001', 'CZQ', 70),
                ('002', 'LHQ', 80),
                ('003', 'MQ', 90),
                ('004', 'WH', 80),
                ('005', 'HP', 70),
                ('006', 'YF', 66),
                ('007', 'TEST', 100)"""
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print('rollback')
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


def deletedb(db):
	cursor = db.cursor()
	sql = "DELETE FROM Student WHERE Grade = '%d'" % (100)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print('delete data fail.')
		db.rollback()


def updatedb(db):
	cursor = db.cursor()
	sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print('update data fail.')
		db.rollback()


def droptable(db):
	cursor = db.cursor()
	cursor.execute('drop table Student')


def closedb(db):
	db.close()


def main():
	db = connectdb()
	createtable(db)
	insertdb(db)
	print('insert data after')
	querydb(db)
	deletedb(db)
	print('delete data after')
	querydb(db)
	updatedb(db)
	print('update data after')
	querydb(db)
	droptable(db)
	closedb(db)


if __name__ == '__main__':
	main()

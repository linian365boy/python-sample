#!/usr/bin/env python
# coding=utf-8


class Local(object):
	# __slots__ = 'name', 'id'
	__slots__ = '_local__impl', '__dict__'

	def __unicode__(self):
		return '%s %s' % (self.name, self.id)

	def __str__(self):
		return '%s %s' % (self.name, self.id)


def main():
	local = Local()
	local.name = 'niange'
	local.id = 123
	local.age = 234
	local.ss = 'suibian'
	local._sdf_ = 'sdf'
	return local


if __name__ == '__main__':
	local_m = main()
	print(local_m)
	print('%s %s %s' % (local_m.id, local_m.name, local_m.age))
	print(local_m.ss)
	print(local_m._sdf_)

	local_a = Local()
	local_a.id = 35
	print(local_a.id)

import re

class Descriptor(object):
	def __get__(self, instance, owner):
		if instance is None:
			raise AttributeError("Can only be accessed by the instance")
		return self.val

	def __set__(self, instance, value):
		self.val = value

	def __delete__(self,instance):
		del self.val


class Thing(object):
		name = Descriptor()

		def __init__(self, name):
			self.name = name


if __name__ == '__main__':
	t = Thing('bob')
	print t.name
	t.name = 'ram'

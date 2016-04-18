class Thing:
	def __init__(self):
		self.number = 0
		
	def some_function(self):
		print "I got called."
		
	def add_up(self, more):
		self.number += more
		return self.number
		
# two different things
a = Thing()
b = Thing()

a.some_function()
b.some_function()

print a.add_up(20)
print a.add_up(20)
print b.add_up(30)
print b.add_up(30)

print a.number
print b.number
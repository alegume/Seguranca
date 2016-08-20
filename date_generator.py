#
# Dates generator
# author: Alexandre A. A. M. de abreu
#	

def dias():
	for i in range(1, 32):
		yield i

def meses():
	for i in range(1, 13):
		yield i

def anos():
	for i in range(1970, 2010):
		yield i


for d in dias():
	for m in meses():
		for a in anos():
			print str('%02d' % d) + str('%02d' % m) + str(a)

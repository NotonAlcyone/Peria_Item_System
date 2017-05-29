

 

class ItemMix:
	def __init__(self):
		
class Item:
	def __init__(self,name):
		self.name = name
		self.cast = []

	def addCast(self,name):

		self.cast.append(Cast(name))

class Cast:
	def __init__(self,name):
		self.name = name




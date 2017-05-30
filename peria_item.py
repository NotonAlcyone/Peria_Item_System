itemData = []
itemTable = []

class Item:
	def __init__(self,name):
		self.name = name
		self.inputCast = []
		self.outputCast = []

	def addInputCast(self,name,act,output = None):
		self.inputCast.append(Cast(name,act,output))


	def addOutputCast(self,name,act):
		self.outputCast.append(Cast(name,act))

class Cast:
	def __init__(self,name,act,output = None):
		self.name = name
		self.act = act
		self.linkedCast = output

def itemMix(itemNumber,name):
	item = itemTable[itemNumber]
	for i in range(0,len(item.inputCast)):
		if item.inputCast[i].linkedCast != None:
			if item.inputCast[i].name == name:
				outputToInput(item.outputCast[item.inputCast[i].linkedCast].name)
		elif item.inputCast[i].linkedCast  == None:
			if item.inputCast[i].name == name:
				finalOutput(item.inputCast[i].name)



def outputToInput(name):
	for i in range(0,len(itemTable)):
		for j in range(0,len(itemTable[i].inputCast)):
			if itemTable[i].inputCast[j].name == name:
				print(itemTable[i].inputCast[j].act)


	"""
	for i in range(0,len(itemTable)):
		for j in range(0,len(itemTable[i].inputCast))
	"""


def finalOutput(name):
	print(name)


	"""
	search = itemData[itemNumber].inputCast
	for i in range(0,len(search)):
		if cast == search[i].name:
			print(search[i].act)
	"""



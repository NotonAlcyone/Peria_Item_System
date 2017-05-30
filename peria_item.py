itemData = []
itemTable = []

class Item:
	def __init__(self,name):
		self.name = name
		self.inputCast = []
		self.outputCast = []
		self.act = []
		self.sync = False

	def addInputCast(self,name,link = None):
		self.inputCast.append(Cast(name,link))
	def addOutputCast(self,name):
		self.outputCast.append(Cast(name))
	def addAct(self,act,link = None):
		self.act.append(Act(act,link))

class Act:
	def __init__(self,act,link = None):
		self.act = act
		self.link = link
class Cast:
	def __init__(self,name,link = None):
		self.name = name
		self.link = link


def starter(itemNumber,name):
	print("하지마루용")
	inputCheck(itemNumber,name)





def inputCheck(itemNumber,name):
	item = itemTable[itemNumber]
	for i in range(0,len(item.inputCast)):
		if item.inputCast[i].name == name:
			if item.inputCast[i].link != None:
				actCheck(itemNumber,item.inputCast[i].link )

def actCheck(itemNumber,link):
	item = itemTable[itemNumber]
	print(item.act[link].act)
	if item.act[link].link != None:
		outputCheck(itemNumber,link)

def outputCheck(itemNumber,link):
	item = itemTable[itemNumber]
	for i in range(0,len(itemTable)):
		for j in range(0,len(itemTable[i].inputCast)):
			if itemTable[i].inputCast[j].name == item.outputCast[link].name:
				inputCheck(i,itemTable[i].inputCast[j].name)



"""

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
				itemMix(i,itemTable[i].inputCast[j].name)


	for i in range(0,len(itemTable)):
		for j in range(0,len(itemTable[i].inputCast))



def finalOutput(name):
	print(name)



	search = itemData[itemNumber].inputCast
	for i in range(0,len(search)):
		if cast == search[i].name:
			print(search[i].act)

"""


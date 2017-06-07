from postpositions import *
itemData = []
itemTable = []

class Item:
	def __init__(self, name):
		self.name = name
		self.inputCast = []
		self.outputCast = []
		self.act = []
		self.stringAct = None
		self.trans = False
		self.calc = False
		self.string = False
		self.sync = False

	def addInputCast(self, name, link = None):
		self.inputCast.append(Cast(name, link))
	
	def addOutputCast(self, name):
		self.outputCast.append(Cast(name))
	def addOutputTrans(self, name):
		self.trans = True
		self.outputCast.append(Cast(name))

	def addAct(self, act, link = None):
		self.act.append(Act(act, link))
	def addStringAct(self, link = None):
		self.string = True
		self.act.append(Act(None, link))

	def addCalc(self, act, link = None):
		self.calc = True
		self.act.append(Act(act, link))
	def addSync(self, link):
		self.sync = True
		self.act.append(Act(None, link))

class Act:
	def __init__(self, act, link = None):
		self.act = act
		self.link = link
		self.trans = [] #sync를 대비해서 배열입니다.

class Cast:
	def __init__(self, name, link = None):
		self.name = name
		self.link = link
		self.trans = [] #sync의 input을 대비해서 배열입니다.

def inputStarter(itemNumber, name = None): #명령으로 시작
	if name == None: #시작할때 직접 명령하는 용도
		print("행동을 입력해주세요")
		name = input()
	inputCheck(itemNumber, name, None)

def actStarter(itemNumber): #행동으로 시작
	if itemTable[itemNumber].string == True: #CUI에선 채팅창 전용
		actCheck(itemNumber, None, None)

def inputCheck(itemNumber, name, trans):
	item = itemTable[itemNumber] #숏컷	
	for i in range(0,len(item.inputCast)):
		if item.inputCast[i].link != None: #액트로 연결되는 링크값이 존재하고
			if item.inputCast[i].name == name: #받아온 이름값과 Input에 등록된 이름이 같다면
				if trans != None: #input이 None값이 아니면 전달해줌
					item.inputCast[i].trans = trans
				actCheck(itemNumber, item.inputCast[i].link, item.inputCast[i].trans)

def actCheck(itemNumber, link, trans):
	item = itemTable[itemNumber] #숏컷
	if item.sync == True:
		syncCheck(itemNumber, trans)
	elif item.calc == True:
		calcCheck(itemNumber, trans)
	else:
		item.act[0].trans = trans
		if link == None: #actStarter에서 온 경우 등록되어있는 링크 가져옴
			link = item.act[0].link #stringact는 0 고정
		if item.string == True: #해당 액트가 채팅창이고
			if item.act[0].trans == None: #해당 액트에 출력해야하는 문자열이 없다면
				print("채팅을 입력해주세요")
				item.act[0].trans = input() #문자열을 받습니다\
			else:
				print("채팅창에 다음과 같은 결과가 나왔습니다.")
				print(item.act[0].trans[0])#문자열은 1개만 인자를 받으므로 0번 고정입니다.
		if item.act[link].act != None: #모듈에 act가 있다면
			print("모듈이 다음과 같은 움직임을 보입니다")
			print(item.act[link].act) #GUI적 움직임 대신에 act를 나타냅니다
		if item.act[link].link != None: #해당 액트가 가리키는 output이 있다면
			outputCheck(itemNumber,link) #해당 아웃풋의 정보를 보냅니다.

def syncCheck(itemNumber, trans):
	item = itemTable[itemNumber] #숏컷
	item.act[0].trans.append(trans)
	if len(item.act[0].trans) == 2:
		outputCheck(itemNumber, item.act[0].link)

def calcCheck(itemNumber, trans): #산술소자...하드코딩...
	item = itemTable[itemNumber] #숏컷
	item.act[0].trans = []
	Sign = item.act[0].act
	X = int(trans[0])
	Y = int(trans[1])
	if Sign == "+":
		answer = X + Y
	elif Sign == "-":
		answer = X - Y
	elif Sign == "*":
		answer = X * Y
	elif Sign == "/":
		answer = X / Y
	elif Sign == "//":
		answer = X // Y
	elif Sign == "%":
		answer = X % Y
	elif Sign == "max":
		answer = max(X, Y)
	elif Sign == "min":
		answer = min(X, Y)
	elif Sign == "^" or "**":
		answer = X ^ Y

	item.act[0].trans.append(answer)
	outputCheck(itemNumber, item.act[0].link)

def outputCheck(itemNumber, link):
	item = itemTable[itemNumber] #숏컷
	item.outputCast[link].trans = item.act[0].trans #채팅창에서 입력받은 데이터를 output으로 옮깁니다.
	for i in range(0,len(itemTable)): #받아온 output과 같은 명령을 가진 input을 찾습니다
		for j in range(0,len(itemTable[i].inputCast)):
			if post_Swithcer(itemTable[i].inputCast[j].name) == post_Swithcer(item.outputCast[link].name):
				inputCheck(i, itemTable[i].inputCast[j].name, item.outputCast[link].trans) #해당 인풋에 정보를 넣어줍니다.

def post_Swithcer(string): #명령어에서 josa.txt에 있는 조사와 반점을 제거합니다.
	for i in range(0, len(case)):
		string = string.replace(case[i], "")
	string = string.replace(" ", "")
	return string


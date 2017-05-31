from peria_item import *



tmpItem = Item("전등")
tmpItem.addInputCast("불을 켜라",0)
tmpItem.addInputCast("불을 꺼라",1)
tmpItem.addAct("Activate Light")
tmpItem.addAct("Deactivate Light")
itemData.append(tmpItem)

tmpItem = Item("전등")
tmpItem.addInputCast("불을 켜라",0)
tmpItem.addInputCast("불을 꺼라",1)
tmpItem.addAct("Activate Light")
tmpItem.addAct("Deactivate Light")
itemData.append(tmpItem)


tmpItem = Item("스위치")
tmpItem.addInputCast("스위치를 켜라",0)
tmpItem.addInputCast("스위치를 꺼라",1)
tmpItem.addAct("Switch On",0)
tmpItem.addAct("Switch OFF",1)
tmpItem.addOutputCast("불을 켜라")
tmpItem.addOutputCast("불을 꺼라")
itemData.append(tmpItem)

tmpItem = Item("채팅창")
tmpItem.addStringAct(0)
tmpItem.addOutputTrans("첫번째 수는 [X] 입니다.")
itemData.append(tmpItem)

tmpItem = Item("채팅창")
tmpItem.addInputCast("첫번째 수는 [X] 입니다.",0)
tmpItem.addStringAct()
itemData.append(tmpItem)


itemTable.append(itemData[0])
itemTable.append(itemData[1])
itemTable.append(itemData[2])



inputStarter(2)
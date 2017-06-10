from peria_item import *



tmpItem = Item("파랑 발광석")
tmpItem.addInputCast("파랑 발광석 켜짐",0)
tmpItem.addInputCast("빨강 발광석 켜짐",1)
tmpItem.addAct("Activate Light")
tmpItem.addAct("Deactivate Light")
itemData.append(tmpItem)

tmpItem = Item("빨강 발광석")
tmpItem.addInputCast("빨강 발광석 켜짐",0)
tmpItem.addInputCast("파랑 발광석 켜짐",1)
tmpItem.addAct("Activate Light")
tmpItem.addAct("Deactivate Light")
itemData.append(tmpItem)


tmpItem = Item("스위치")
tmpItem.addInputCast("레버를 이쪽으로 옮깁니다.",0)
tmpItem.addInputCast("레버를 저쪽으로 옮깁니다.",1)
tmpItem.addAct("Switch On",0)
tmpItem.addAct("Switch OFF",1)
tmpItem.addOutputCast("파랑 발광석 켜짐")
tmpItem.addOutputCast("빨강 발광석 켜짐")
itemData.append(tmpItem)


itemTable.append(itemData[0]) #아이템 데이터를 아이템 테이블에 등록
itemTable.append(itemData[1])
itemTable.append(itemData[2])


inputStarter(2)

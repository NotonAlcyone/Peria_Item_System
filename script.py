from peria_item import *



tmpItem = Item("전등")
tmpItem.addInputCast("불을 켜라","Activate Light")
tmpItem.addInputCast("불을 꺼라","Deactivate Light")
itemData.append(tmpItem)

tmpItem = Item("스위치")
tmpItem.addInputCast("스위치를 켜라","Switch ON",0)
tmpItem.addInputCast("스위치를 꺼라","Switch OFF",1)
tmpItem.addOutputCast("불을 켜라","Switch ON")
tmpItem.addOutputCast("불을 꺼라","Switch OFF")
itemData.append(tmpItem)


itemTable.append(itemData[0])
itemTable.append(itemData[1])


itemMix(1,"스위치를 꺼라")
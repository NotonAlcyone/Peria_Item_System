from peria_item import *


"""
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
"""

tmpItem = Item("채팅창")
tmpItem.addStringAct(0)
tmpItem.addOutputTrans("첫번째의 수는 [X] 입니다")
itemData.append(tmpItem)

tmpItem = Item("채팅창")
tmpItem.addStringAct(0)
tmpItem.addOutputTrans("두번째 수는 [X] 입니다.")
itemData.append(tmpItem)

tmpItem = Item("동기화")
tmpItem.addInputCast("첫번째 수는 [X] 입니다.",0)
tmpItem.addInputCast("두번째 수는 [X] 입니다.",0)
tmpItem.addSync(0)
tmpItem.addOutputTrans("두 수 전달")
itemData.append(tmpItem)

tmpItem = Item("산술 소자")
tmpItem.addInputCast("두 수 전달",0)
tmpItem.addCalc("+",0)
tmpItem.addOutputTrans("결과는 [Z] 입니다.")
itemData.append(tmpItem)

tmpItem = Item("채팅창")
tmpItem.addInputCast("결과는 [Z] 입니다.",0)
tmpItem.addStringAct()
itemData.append(tmpItem)


itemTable.append(itemData[0]) #아이템 데이터를 아이템 테이블에 등록
itemTable.append(itemData[1])
itemTable.append(itemData[2])
itemTable.append(itemData[3])
itemTable.append(itemData[4])




actStarter(0) #1번 채팅창 입력
actStarter(1) #2번 채팅창 입력


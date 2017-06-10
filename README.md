# Peria Item System

[유투브 페리아 연대기 아이템 설명](https://youtu.be/hEO4A5k6o2w?list=PLTgBeN24zClL73zU6CbvXuCqWXlvrRgtd)을 참고로 파이썬 CUI을 이용해 최대한 비슷하게 구현합니다

![default](https://user-images.githubusercontent.com/15938440/27004656-c14402ce-4e47-11e7-85d1-c8deabee2ae4.png)


## 사용프로그램
* Python 3

## 사용법

프로젝트의 peria_item.py 를 import 하고 빌드합니다.

## 스크립트 설명

### 아이템 이름

```python
className = Item("이름")
```
* 이름은 문자열을 입력 받습니다.

### 입력 주문
![default](https://user-images.githubusercontent.com/15938440/27004623-0a078e6e-4e47-11e7-831c-b9fe37bfe4f4.png)

![default](https://user-images.githubusercontent.com/15938440/27004620-f61c45c0-4e46-11e7-9cbb-4c04a0af81b4.png)

```python
className.addInputCast("주문",actNum)
```
* 주문은 문자열을 입력 받습니다.
* actNum은 입력주문을 받은 후, 실행 할 act을 선택합니다.

### 수동적 행동
```python
className.addAct("행동",outputNum)
```
* 행동은 문자열을 입력 받습니다.
* GUI에서의 이미지형태로 나타나는 행동을 대체합니다. ex) 불이 켜짐/꺼짐

### 능동적 행동
```python
className.addStringAct()
```
* GUI에서의 채팅창 입력을 하는 행동을 대체합니다.

### 동기화 모듈
```python
className.addSync(outputNum)
```
* 동기화 모듈에 관한 스크립트입니다.
* outputNum은 행동을 완료한후, 실행 할 output을 선택합니다.

### 산술 모듈
```python
className.addCalc("부호", outputNum)
```
* 산술모듈과 관련된 스크립트 입니다.
* 부호는 문자열로 "+, -, *, /, //, %, max, min, ^, **" 을 받습니다.
* outputNum은 행동을 완료한후, 실행 할 output을 선택합니다.


### 단순 아웃풋
![default](https://user-images.githubusercontent.com/15938440/27004637-3f584388-4e47-11e7-800c-196f6050a1e3.png)


```python
className.addOutputCast("주문")
```
* 인자없이 단순 주문만을 전달하는 역할을 합니다.

### 인자 아웃풋
![default](https://user-images.githubusercontent.com/15938440/27004636-3e607eb4-4e47-11e7-8684-b93b878843e2.png)
```python
className.addOutputTrans("주문")
```
* 인자가 포함된 주문을 전달하는 역할을 합니다.




## 등록및 시작법

### 아이템 등록
![default](https://user-images.githubusercontent.com/15938440/27004671-08bbcc86-4e48-11e7-8229-14d49a20d835.png)

```python
itemData.append(className)
```
* 스크립트 상의 기능을 모두 넣은 후, 작성할경우 itemData 리스트에 아이템이 추가됩니다.

### 아이템 테이블 등록법
![default](https://user-images.githubusercontent.com/15938440/27004673-0e7caf3c-4e48-11e7-8e4d-433dc19d023d.png)

```python
itemTable.append(itemData[num]) 
```
* 아이템을 전부 등록한 후, 사용할 아이템을 아이템 테이블에 추가합니다

### 아이템 사용 시작

```python
actStarter(itemTableNum) # 채팅창으로 시작시
inputStarter(itemTableNum) # 입력 주문 쪽으로 시작시
```


## 아이템 조합

### 전등

![default](https://user-images.githubusercontent.com/15938440/27004664-df6d7bb8-4e47-11e7-912c-61b43c8f0b29.png)

```python
tmpItem = Item("전등")
tmpItem.addInputCast("불을 켜라",0)
tmpItem.addInputCast("불을 꺼라",1)
tmpItem.addAct("Activate Light")
tmpItem.addAct("Deactivate Light")
itemData.append(tmpItem)
```

### 스위치
![default](https://user-images.githubusercontent.com/15938440/27004687-748af9dc-4e48-11e7-9d8f-11aa461978c3.png)
```python
tmpItem = Item("스위치")
tmpItem.addInputCast("스위치를 켜라",0)
tmpItem.addInputCast("스위치를 꺼라",1)
tmpItem.addAct("Switch On",0)
tmpItem.addAct("Switch OFF",1)
tmpItem.addOutputCast("불을 켜라")
tmpItem.addOutputCast("불을 꺼라")
itemData.append(tmpItem)
```

### 채팅창
![default](https://user-images.githubusercontent.com/15938440/27004688-7538cf44-4e48-11e7-88bc-556b5e4618b8.png)
```python
tmpItem = Item("채팅창")
tmpItem.addStringAct(0)
tmpItem.addOutputTrans("입력된 수는 [X] 입니다")
itemData.append(tmpItem)
```

### 동기화 소자
![default](https://user-images.githubusercontent.com/15938440/27004603-a693a296-4e46-11e7-80f0-032e6e07b9e0.png)

```python
tmpItem = Item("동기화")
tmpItem.addInputCast("첫번째 수는 [X] 입니다.", 0)
tmpItem.addInputCast("두번째 수는 [Y] 입니다.", 0)
tmpItem.addSync(0)
tmpItem.addOutputTrans("두 수 전달")
itemData.append(tmpItem)
```

### 산술 소자
![default](https://user-images.githubusercontent.com/15938440/27004607-c20161f8-4e46-11e7-9dda-2ae058f7391f.png)

```python
tmpItem = Item("산술 소자")
tmpItem.addInputCast("두 수 전달", 0)
tmpItem.addCalc("+", 0)
tmpItem.addOutputTrans("결과는 [Z] 입니다.")
itemData.append(tmpItem)
```

## 조사및 구두점 무시 시스템

![default](https://user-images.githubusercontent.com/15938440/27004618-ec87785e-4e46-11e7-876d-fa498d097f36.png)

* JOSA.txt 에서 조사목록을 불러온 후, 주문에서 해당 조사와 구두점 그리고 공백을 제거 한후 비교합니다
* "첫번째의 수는 X 입니다" 와 "첫번째 수 X 입니다." 를 같은 주문 으로 인식합니다.

## 예제 실행

### switch_light.py
![default](https://user-images.githubusercontent.com/15938440/27004599-8c5ec27a-4e46-11e7-9ec4-2de0af98c557.png)

```python
행동을 입력해주세요
>>> 레버를 이쪽으로 옮깁니다.
스위치 모듈이 다음과 같은 움직임을 보입니다
Switch On
파랑 발광석 모듈이 다음과 같은 움직임을 보입니다
Activate Light
빨강 발광석 모듈이 다음과 같은 움직임을 보입니다
Deactivate Light
```

### calc_sum.py

![default](https://user-images.githubusercontent.com/15938440/27004611-cd6b7826-4e46-11e7-8bf9-79c3fb2f6477.png)

```python
채팅을 입력해주세요
>>> 5
채팅을 입력해주세요
>>> 6
채팅창에 다음과 같은 결과가 나왔습니다.
11
```

## 기타
* 프로젝트에 관한 질문은 [메일](notonalcyone@gmail.com)로 부탁드립니다.
* JOSA.txt 의 [출처](http://nlp.kookmin.ac.kr/data/han-dic.html)
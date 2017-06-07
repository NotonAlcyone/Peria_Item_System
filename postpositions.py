file = open("JOSA.txt", 'r')
case = file.readlines()
for i in range(0, len(case)):
	case[i] = case[i].replace("\n", " ")
case.append(".")
# 조사 파일 출처 http://nlp.kookmin.ac.kr/data/han-dic.html
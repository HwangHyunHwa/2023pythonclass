outStr = ""
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for k in range(0, count) :
    outStr += inStr[count - (k + 1)]
    
#같은 내용의 코드
#for k in range(count -1, -1, -1) :
#	outStr += inStr[k]

print("내용을 거꾸로 출력 --> %s" % outStr)

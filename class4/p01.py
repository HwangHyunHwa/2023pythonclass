import random

com = random.randrange(1,21)
while com != user : #com과 user가 같으면 반복 종료
    user = int(input('1~20사이의 수 입력: '))
    if com==user:
        print('맞췄습니다')
    elif com > user :
        print('더 큰 수입니다')
    else :
        print('더 작은 수입니다')
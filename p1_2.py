def palindrom_check2(s):
    qu = []
    st = []
    for x in s:
        if x.isalpha():
            qu.append(x.lower())    #Mom도 똑같은 알파벳으로 인식
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():   #비효율적인 큐? 맨 뒤에와 맨 앞에 비교, qu는 앞에서 빼줘야하기 때문에 앞으로 당겨야 하는데 계속 삭제를 해는 점이 비효율적
            return False
            
    return True

pstringList = ['역삼역', '구로구', 'MOM', '기러기', '비둘기', '기특한 특기', 'racer', 'father', '봄', '여름']

for s in pstringList:
    idx = pstringList.index(s)  #index 안하고 필린드에 s를 줘도 가능
    #print(s, ' =  ', palindrom_check2(pstringList[idx]))
    print('{0} = {1}'.format(s, palindrom_check2(pstringList[idx])))
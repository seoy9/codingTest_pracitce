import re

# 대문자 > 소문자
def upTolow(id):
    id = id.lower()
    #print('소문자 ', id)
    
    return id

# 규칙 아닌 문자 제거
def delNoRule(id):
    id = re.sub(r'[^a-z0-9._-]', '', id)
    #print('규칙X 제거 ', id)
    
    return id

# . 2개 이상 연속 > . 1개
def changeTwoMoreDotOne(id):
    id_list = list(id)
    indexs = []
    
    for pos, char in enumerate(id):
        if(char == '.'):
            indexs.append(pos)
    
    i = 0
    count = 0
    while(i < len(indexs) - 1):
        if(indexs[i] + 1 == indexs[i+1]):
            if(count == 0):
                del id_list[indexs[i]]
            else:
                del id_list[indexs[i] - count]
            del indexs[i]
            count += 1
        else:
            i += 1
    
    id = ''.join(id_list)
    #print('. 연속 제거 ', id)
    
    return id

# . 처음/끝 제거
def delStartEndDot(id):
    id_list = list(id)
    
    if(len(id_list) != 0):
        if(id_list[0] == '.'):
            del id_list[0]
            
    if(len(id_list) != 0):
        if(id_list[len(id_list)-1] == '.'):
            del id_list[len(id_list)-1]
    
    id = ''.join(id_list)
    #print('. 처음/끝 제거 ', id)
    
    return id

# 빈 문자열 > 'a' 대입
def addNullA(id):
    id_list = list(id)
    
    if(len(id_list) == 0):
        id_list.append('a')
        
    id = ''.join(id_list)
    #print('빈 문자열 a 대입 ', id)
    
    return id

# 16개 이상 > 15개까지
def endFifteen(id):
    id_list = list(id)
    
    if(len(id_list) >= 16):
        id = id[:15]
    #print('15개까지 ', id)
    
    return id

# 2 이하 > 마지막 글자 3까지
def addBelowTwoEndToThree(id):
    if(len(id) <= 2):
        for i in range(3 - len(id)):
            id += id[-1:]
    
    #print('2 이하 마지막 3까지 ', id)
            
    return id

def solution(new_id):
    id = new_id

    # 대문자 > 소문자
    id = upTolow(id)
    
    # 규칙 아닌 문자 제거
    id = delNoRule(id)
    
    # . 2개 이상 연속 > . 1개
    id = changeTwoMoreDotOne(id)
    
    # . 처음/끝 제거
    id = delStartEndDot(id)
    
    # 빈 문자열 > 'a' 대입
    id = addNullA(id)
    
    # 16개 이상 > 15개까지
    id = endFifteen(id)
    
    # . 처음/끝 제거 (추가 - 자르면서 끝이 .이 될 수 있음)
    id = delStartEndDot(id)
    
    # 2 이하 > 마지막 글자 3까지
    id = addBelowTwoEndToThree(id)
    
    answer = id
    return answer
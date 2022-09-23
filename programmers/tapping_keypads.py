# 첫 번째, 두 번째 인덱스값 찾기
def findFirstSecondIndex(phone, number):
    first_index = 10
    second_index = 10
    isStop = 0
    
    for i in range(4):
        for j in range(3):
            if(number == phone[i][j]):
                first_index = i
                second_index = j
                isStop = 1
                break
        if(isStop == 1):
            break
    
    return (first_index, second_index)

# 거리 계산
def findDistance(first_1, second_1, first_2, second_2):
    distance = 0
    
    distance += abs(first_1 - first_2)
    distance += abs(second_1 - second_2)
    
    return distance

# 거리 비교
def compareDistanceLR(distance1, distance2, hand):
    if(distance1 < distance2):
        return 'L'
    elif(distance1 > distance2):
        return 'R'
    else:
        if(hand == 'right'):
            return 'R'
        else:
            return 'L'

def solution(numbers, hand):
    index = 0
    number = r_number = l_number = r_distance = l_distance = -1
    first_r = first_l = 3
    second_r = 2
    second_l = 0
    answer = ''
    
    # phone 번호 2차원 배열
    phone = [[0]*3 for i in range(4)]
    
    for i in range(3):
        for j in range(3):
            if(i == 0):
                phone[i][j] = j + 1
            elif(i == 1):
                phone[i][j] = j + 4
            elif(i == 2):
                phone[i][j] = j + 7
    
    phone[3][0] = '*'
    phone[3][1] = 0
    phone[3][2] = '#'
    
    # numbers에 있는 숫자 개수만큼 반복
    while(index < len(numbers)):
        number = numbers[index]
        
        # 1, 4, 7인지 확인
        if(number == 1 or number == 4 or number == 7):
            l_number = number
            answer += 'L'
            index += 1
            continue

        # 3, 6, 9인지 확인
        if(number == 3 or number == 6 or number == 9):
            r_number = number
            answer += 'R'
            index += 1
            continue

        # 숫자 위치 측정
        first_n, second_n = findFirstSecondIndex(phone, number)
        
        # 오른쪽 위치 측정
        if(r_number != -1):
            first_r, second_r = findFirstSecondIndex(phone, r_number)
        
        # 숫자-오른쪽 거리 측정
        r_distance = findDistance(first_n, second_n, first_r, second_r)
            
        # 왼쪽 위치 측정
        if(l_number != -1):
            first_l, second_l = findFirstSecondIndex(phone, l_number)
        
        # 숫자-왼쪽 거리 측정
        l_distance = findDistance(first_n, second_n, first_l, second_l)
            
        # 거리 비교
        choice = compareDistanceLR(l_distance, r_distance, hand)

        if(choice == 'L'):
            l_number = number
            index += 1
            answer += 'L'
            continue
        elif(choice == 'R'):
            r_number = number
            index += 1
            answer += 'R'
            continue
        
    return answer
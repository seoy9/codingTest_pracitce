def popInsert(queue1, queue2, total1, total2):
    temp = queue2.pop(0)
    total2 -= queue2[0]
    queue1.append(temp)
    total1 += queue2[0]
    
    return (total1, total2)

def popInsert2(queue1, queue2):
    temp = queue2.pop(0)
    queue1.append(temp)
    
def whichPop(gap1, queue1, queue2, total1, total2):
    if(gap1 > 0):
        popInsert(queue1, queue2, total1, total2)
    elif(gap1 < 0):
        popInsert(queue2, queue1, total1, total2)
    
def solution(queue1, queue2):
    # 작업 수 담는 배열
    result = []
    
    # 각 배열의 합
    total1 = sum(queue1)
    total2 = sum(queue2)
    
    # 총 배열의 합
    total = total1 + total2
    
    if(total % 2 != 0):
        return -1
    
    same = total / 2
    
    # 작업 수
    index1 = 0
    index2 = 0
    size = len(queue1) * 2
    
    while(index1 < size and index2 < size and total1 != same):          
        if(same - total1 > 0):
            queue1.append(queue2[index2])
            total1 += queue2[index2]
            total2 -= queue2[index2]
            index2 += 1
        else:
            queue2.append(queue1[index1])
            total2 += queue1[index1]
            total1 -= queue1[index1]
            index1 += 1
            
    answer = -1
    
    if(total1 == total2):
        answer = index1 + index2
    
    return answer
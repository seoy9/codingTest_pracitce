import math

# 총 이용시간 계산
def sumTime(time):
    index = 0
    total = 0
    f = []
    s = []
    while(index < len(time)):
        if(len(time) % 2 == 1):
            if(index == len(time)-1):
                f = time[index].split(":")
                index += 1
                s = ['23', '59']
            else:
                f = time[index].split(":")
                index += 1
                s = time[index].split(":")
                index += 1
        else:
            f = time[index].split(":")
            index += 1
            s = time[index].split(":")
            index += 1
        h = int(s[0]) - int(f[0])
        m = int(s[1]) - int(f[1])
        total = total + (h * 60) + m
        
    return total

# 주차요금 계산
def sumFee(total, fees):
    fee = fees[1]
    total -= fees[0]
    
    if(total > 0):
        fee += math.ceil(total / fees[2]) * fees[3]
    
    return fee

def solution(fees, records):
    re_array = [[0]*3 for _ in range(len(records))]
    car_array = []
    time = []
    
    # "시각 번호 내역"을 ["시각", "번호", "내역"]으로 배열에 넣기
    for i in range(len(records)):
        array = records[i].split(" ")
        for j in range(3):
            re_array[i][j] = array[j]
    
    # 차량 번호만 배열에 넣기 (중복 X)
    for item in re_array:
        if(item[1] not in car_array):
            car_array.append(item[1])
            
    # 차량 번호 작은순으로 정렬
    car_array.sort()
    
    answer = []
    
    for car in car_array:
        # in > out 순서이기 때문에 순서대로 시간만 배열에 넣기
        for item in re_array:
            if(car == item[1]):
                time.append(item[0])
        
        total = sumTime(time)
        
        fee = sumFee(total, fees)
        
        answer.append(fee)
        
        # 다음 차를 위해 배열 비우기
        time.clear()
    
    return answer
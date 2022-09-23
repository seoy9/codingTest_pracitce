import math

# 소수인지 판별
def prime(num):
    for i in range(2, int(math.sqrt(num) + 1)): # 2부터 num의 제곱근까지의 숫자
        if num % i == 0:    # 나눠떨어지면 소수 아님
            return False
    return True     # 나눠떨어지지 않으면 소수
    
def solution(n, k):
    answer = 0
    
    # k진법 담을 배열, 변수
    k_result_arr = []
    k_result = ''
    
    # K진법
    if(k != 10):    # 10진법이 아니면
        while(n > 0):
            div = divmod(n, k)
            k_result_arr.append(div[1])
            n = div[0]
        k_result_arr.reverse()  # 역순
        k_result_arr = list(map(str, k_result_arr))
        k_result = ''.join(k_result_arr)
    else:   # 10진법이면
        k_result = str(n)    
    
    # 0 기준 자르기
    zero_arr = k_result.split('0')
    
    # 1 제외 나머지 10진법 계산
    for arr in zero_arr:
        if(arr != '' and arr != '1'):   # ''도 1도 아니면
            if(prime(int(arr))):    # 소수이면
                answer += 1
    
    return answer
def solution(N, stages):
    # 각 스테이지마다 머물러있는 플레이어의 수 계산
    stage_num = [0] * (N+1)
    
    for i in range(1, N+2):
        for j in range(len(stages)):
            if(i == stages[j]):
                stage_num[i-1] += 1
            
    #print('stage_num ', stage_num)
    
    
    # 각 스테이지를 도달한 플레이어 수 계산
    finish_num = [0] * N
    
    for i in range(N):
        for j in range(len(stage_num)):
            if(i <= j):
                finish_num[i] += stage_num[j]
        
    #print('finish_num ', finish_num)
    
    # 실패율 계산
    loss_num = []
    
    for i in range(N):
        # 0으로 나누면 런타임 에러 생김
        if(finish_num[i] == 0):
            loss_num.append(0.0)
        else:
            loss_num.append(stage_num[i]/finish_num[i])
    
    # 스테이지 오름차순
    answer = []
    
    for i in range(N):
        answer.append(i+1)
    
    # 실패율 높은 스테이지부터 내림차순
    index = 0
    while(index < N):
        big = loss_num[index]
        big_index = index
        
        for i in range(index, len(loss_num)):
            # 실패율이 같다면 낮은 스테이지가 먼저
            if(big == loss_num[i]):
                if(answer[big_index] > answer[i]):
                    big = loss_num[i]
                    big_index = i
            elif(big < loss_num[i]):
                big = loss_num[i]
                big_index = i
        
        # 실패율 배열과 정답 배열(스테이지 순서)을 내림차순으로 정렬
        temp = loss_num[index]
        loss_num[index] = big
        loss_num[big_index] = temp
        
        temp = answer[index]
        answer[index] = answer[big_index]
        answer[big_index] = temp
        
        index += 1
    
    return answer
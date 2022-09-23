def solution(board, moves):
    answer = 0
    doll = 0
    
    # 바구니 배열 생성
    basket = []
    
    for catch in moves:
        doll = 0
        for i in range(len(board)):
            if(board[i][catch-1] != 0):     # 인형이 있으면
                doll = board[i][catch-1]
                board[i][catch-1] = 0
                break
        
        if(doll != 0):  # 인형을 잡았으면
            if(len(basket) == 0):   # 바구니가 비어있으면
                basket.append(doll)
            elif(basket[-1] == doll):   # 직전값과 같으면
                answer += 2
                del basket[-1]
            elif(basket[-1] != doll):   # 직전값과 다르면
                basket.append(doll)
    
    return answer
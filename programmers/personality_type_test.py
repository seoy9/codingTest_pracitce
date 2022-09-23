def solution(survey, choices):
    score = [0] * 8
    
    for i in range(len(survey)):
        s = survey[i]
        if s == 'RT':
            if choices[i] < 4:
                score[0] += 4 - choices[i]
            elif choices[i] > 4:
                score[1] += choices[i] - 4
        elif s == 'TR':
            if choices[i] < 4:
                score[1] += 4 - choices[i]
            elif choices[i] > 4:
                score[0] += choices[i] - 4
        elif s == 'FC':
            if choices[i] < 4:
                score[3] += 4 - choices[i]
            elif choices[i] > 4:
                score[2] += choices[i] - 4
        elif s == 'CF':
            if choices[i] < 4:
                score[2] += 4 - choices[i]
            elif choices[i] > 4:
                score[3] += choices[i] - 4
        elif s == 'MJ':
            if choices[i] < 4:
                score[5] += 4 - choices[i]
            elif choices[i] > 4:
                score[4] += choices[i] - 4
        elif s == 'JM':
            if choices[i] < 4:
                score[4] += 4 - choices[i]
            elif choices[i] > 4:
                score[5] += choices[i] - 4
        elif s == 'AN':
            if choices[i] < 4:
                score[6] += 4 - choices[i]
            elif choices[i] > 4:
                score[7] += choices[i] - 4
        elif s == 'NA':
            if choices[i] < 4:
                score[7] += 4 - choices[i]
            elif choices[i] > 4:
                score[6] += choices[i] - 4
                
    answer = ''
    
    if score[0] > score[1]:
        answer += 'R'
    elif score[0] < score[1]:
        answer += 'T'
    else:
        answer += 'R'
        
    if score[2] > score[3]:
        answer += 'C'
    elif score[2] < score[3]:
        answer += 'F'
    else:
        answer += 'C'
    
    if score[4] > score[5]:
        answer += 'J'
    elif score[4] < score[5]:
        answer += 'M'
    else:
        answer += 'J'
        
    if score[6] > score[7]:
        answer += 'A'
    elif score[6] < score[7]:
        answer += 'N'
    else:
        answer += 'A'
        
    return answer
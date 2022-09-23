def solution(id_list, report, k):
    # 신고 수, 메일 수 딕셔너리 초기화
    re_users = {}
    mail_num = {}
    
    for i in range(len(id_list)):
        re_users[id_list[i]] = []
        mail_num[id_list[i]] = 0 
    
    # report 중복 제거
    report_set = set(report)
    
    # 신고 인원 추가
    for re in report_set:
        ids = re.split(' ')
        user = ids[0]
        re_user = ids[1]
        re_users[re_user].append(user)

    # 메일 수 추가
    for id in id_list:
        if(len(re_users[id]) >= k):
            for re in re_users[id]:
                mail_num[re] += 1
    
    # 메일 수 answer에 복사
    answer = []
    
    for id in id_list:
        answer.append(mail_num[id])
    
    return answer
def solution(id_list, report, k):
    id_dict = dict.fromkeys(id_list,0)
    report_rt = dict.fromkeys(id_list,0)
    report = list(set(report))
    
    for i in report:
        report_rt[i.split(' ')[1]] += 1
    report_list = [i for i in report_rt if report_rt[i] >= k]

    for v in report:
        if v.split(' ')[1] in report_list:
            id_dict[v.split(' ')[0]] += 1
                
    return list(id_dict.values())
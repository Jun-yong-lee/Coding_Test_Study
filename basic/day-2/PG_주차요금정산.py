import math
def solution(fees, records):
    answer = []
    total_dict = {}
    in_dict = {}
    
    dt, df, ut, uf = fees
    for each_record in records:
        time, number, status = each_record.split(" ")
        h, m = map(int, time.split(":"))
        minutes = h * 60 + m
        
        if status == "IN":
            in_dict[number] = minutes
        else:
            total_dict[number] = total_dict.get(number, 0) + (minutes - in_dict.pop(number))
    last_time = 23 * 60 + 59
    for number, in_time in in_dict.items():
        total_dict[number] = total_dict.get(number, 0) + last_time - in_time
    
    for number in sorted(total_dict.keys()):
        time = total_dict[number]
        
        if time <= dt:
            fee = df
        else:
            fee = df + math.ceil((time - dt) / ut) * uf #dt, df, ut, uf
        answer.append(fee)
    
    return answer
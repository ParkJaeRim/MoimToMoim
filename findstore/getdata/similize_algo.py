import math
def sim_msd(data, name1, name2):   #유클리디안 거리 유사도
    sum = 0
    count = 0
    for places in data[name1]:
        if places in data[name2]: #같은 장소를 갔다면
            sum += pow(data[name1][places]- data[name2][places], 2)
            count += 1

    return 1 / ( 1 + (sum / count) )

def sim_cosine(data, name1, name2):  #코사인 유사도
    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    count = 0
    for places in data[name1]:
        if places in data[name2]: #같은 장소를 갔다면
            sum_name1 += pow(data[name1][places], 2)
            sum_name2 += pow(data[name2][places], 2)
            sum_name1_name2 += data[name1][places]*data[name2][places]
    
    return sum_name1_name2 / (math.sqrt(sum_name1)*math.sqrt(sum_name2))

def sim_pearson(data, name1, name2): # 피어슨 유사도
    avg_name1 = 0
    avg_name2 = 0
    count = 0
    for places in data[name1]:
        if places in data[name2]: #같은 장소를 갔다면
            avg_name1 = data[name1][places]
            avg_name2 = data[name2][places]
            count += 1
    
    avg_name1 = avg_name1 / count
    avg_name2 = avg_name2 / count
    
    sum_name1 = 0
    sum_name2 = 0
    sum_name1_name2 = 0
    count = 0
    for places in data[name1]:
        if places in data[name2]: #같은 영화를 봤다면
            sum_name1 += pow(data[name1][places] - avg_name1, 2)
            sum_name2 += pow(data[name2][places] - avg_name2, 2)
            sum_name1_name2 += (data[name1][places] - avg_name1) * (data[name2][places] - avg_name2)
    
    return sum_name1_name2 / (math.sqrt(sum_name1)*math.sqrt(sum_name2))
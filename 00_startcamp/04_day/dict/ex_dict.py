"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

result = 0
for i in score.values():
    result += i
    avg = result/3
print(avg)




# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
result = 0
count = 0
for key in scores.keys():
    for value in scores[key].values():
        result += value
        count += 1
avg = result/count
print(avg)

# avg_score = list(map(lambda d: sum(d.values()) / len(d), scores.values()))
# result = sum(avg_score) / len(avg_score)
# print(result)


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

################### 3-1. 도시별 최근 3일의 온도 평균은?

city_avg = {x: sum(y)/3 for x, y in city.items()}
for key, value in city_avg.items():
    print(f"{key}: {value:.2f}")


################### 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

print([city for city, temp in city.items() if temp == min(temp) ])

# city_min = {x: min(y) for x, y in city.items()}
# min_name = [x for x in city_min.keys() if city_min[x] == min(city_min.values())]
# print(min_name[0])

# city_max = {x: max(y) for x, y in city.items()}
# max_name = [x for x in city_max.keys() if city_max[x] == max(city_max.values())]
# print(max_name[0])


# count = 0
# for name, temp in city.items():
#     if count == 0:
#         hot_temp = max(temp)
#         cold_temp = min(temp)
#         hot_city = name
#         cold_city = name
#     else:
#         if min(temp) < cold_temp:
#             cold_temp = min(temp)
#             cold_city = name
#         if max(temp) > hot_temp:
#             hot_temp = max(temp)
#             hot_city = name
#     count += 1

# print(f"{cold_city}: {cold_temp}")
# print(f"{hot_city}: {hot_temp}")


################### 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

print(True) if 2 in city['서울'] else print(False)
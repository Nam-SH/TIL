import random

ssafy = {
    'location': ['서울', '대전', '구미', '광주'],
    'language': {
        'python': {
            'python standard library': ['os', 'random', 'webbrowser'],
            'frameworks': {
                'flask': 'micro',
                'django': 'full-functioning'
            },
            'data_science': ['numpy', 'pandas', 'scipy', 'sklearn'],
            'scraping': ['requests', 'bs4'],
        },
        'web' : ['HTML', 'CSS']
    },
    'classes': {
        'dj': {
            'lecturer': 'harry',
            'manager': '노구하',
            'class president': '박나율',
            'groups': {
                'A': ['이길현', '우동균', '이승현', '이가경', '이병재'],
                'B': ['차진권', '박성진', '심규현', '남승현'],
                'C': ['신승호', '조현호', '이병주', '박홍은'],
                'D': ['조규홍', '조수지', '임소희', '이해인'],
                'E': ['박상원', '고병권', '김준호', '신정우', '박나율']
            }
        },
        'gj': {
            'lecturer': 'change',
            'manager': 'pro-gj'
        }
    }
}
type(ssafy)

#1 지역(location)은 몇 개 있나요?
loc_count = len(ssafy["location"])
print(f"지역의 갯수는 {loc_count}개 입니다.\n")


#2 python standard library에 'requests'가 있나요?
req_in = "requests" in ssafy["language"]["python"]["python standard library"]
print(f"python standard library에 'requests'가 있나요?: {req_in}\n")


#3 dj 반의 반장의 이름을 출력하세요.

cls_president = ssafy["classes"]["dj"]["class president"]
print(f"dj반의 반장의 이름은 {cls_president}씨 입니다.\n")


#4 ssafy에서 배우는 언어들을 출력하세요.

lan = ssafy["language"].keys()
for key in lan:
    print(f"ssafy에서 배우는 언어는 {key}입니다.\n")


#5 ssafy gj반의 강사와 매니저의 이름을 출력하세요.

manager = ssafy["classes"]["gj"]
for key, value in manager.items():
    print(f"gj반의 {key}는 {value}입니다.\n")


#6 framework 들의 이름과 설명을 다음과 같이 출력하세요.

framew = ssafy["language"]["python"]["frameworks"]
for key, value in framew.items():
    print(f"{key}은 {value}이다.\n")


#7 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요.

group_e = ssafy["classes"]["dj"]["groups"]["E"]
random_e = random.choice(group_e)
print(f"오늘의 당번은 {random_e}입니다.")
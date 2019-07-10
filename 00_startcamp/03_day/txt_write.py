# 변수에 만들고 싶은 파일을 open() 해야 한다.

# r : 읽기 / w : 쓰기(+덮어씌어짐) / a : 추가
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close()

# with 구문 (context manager)
with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')

# writelines() : list를 넣어주면 요소 하나당 한 줄씩 작성한다.
a = ['0\n', '1', '2\n', '3']
with open('ssafy2.txt', 'w') as f:
    f.writelines(a)



# # 이스케이프 문자
# "\n" # 다음 줄 이동
# "\t" # 탭문지
# "\\" # 백슬래쉬를 사용하기 위해
# "\'" # 작은 따옴표 사용
# "\"" # 큰 따옴표 사용


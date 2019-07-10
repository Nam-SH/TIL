# DOCstring

"""
다음과 같은 내용의 파일 quest.txt가 있다.
0
1
2
3
역순으로 저장
"""

# 1. 작성
# 2. 뒤집고
# 3. 작성


# 1. quest.txt 작성
with open('quest.txt', 'w') as f:
    for i in range(4):
        if i != 3:
            f.write(f'{i}\n')
        else:
            f.write(f'{i}')

#2. 뒤집고 읽기
with open('reverse_quest.txt', 'w') as f:
    with open('quest.txt', 'r') as fr:
        all_txt = fr.read()[::-1]
    f.write(all_txt)
        
#2. 뒤집어 읽고 작성
with open('reverse_quest1.txt', 'w') as f:
    with open('quest.txt', 'r') as fr:
        all_txt = reversed(fr.readlines())
    f.writelines(all_txt)
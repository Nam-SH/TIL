# read()

with open('with_saffy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)


# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어냄

with open('with_ssafy.txt', 'r') as f:
    print(lines)
    for line in lines:
        print(line.strip())  # 문자열.strip(), #dir(str)로 검색s
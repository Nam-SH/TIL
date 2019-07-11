def lunch2(number):
    menu = {'A음식', "B음식", "C음식", "D음식", "E음식"}
    choice = random.sample(menu, number)
    for i in range(int(number)):
        print(f'{i}의 음식은 {choice[i]}입니다.')

menu = {'A음식', "B음식", "C음식", "D음식", "E음식"}
{x: y for x, y in enumerate(menu)}
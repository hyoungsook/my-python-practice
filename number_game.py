answer = 7
guess = 0

while guess != answer:
    guess = int(input("숫자를 맞혀보세요: "))

    if guess < answer:
        print("더 큰 숫자입니다.")
    elif guess > answer:
        print("더 작은 숫자입니다.")
    else:
        print("정답입니다!")
import random

fortunes = [
    "오늘은 좋은 일이 생길 거예요.",
    "천천히 해도 괜찮아요.",
    "새로운 것을 배우기 좋은 날입니다.",
    "작은 실수가 큰 배움이 됩니다.",
    "꾸준히 하면 실력이 늘어요."
]

result = random.choice(fortunes)

print("오늘의 운세:")
print(result)
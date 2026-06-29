with open("diary.txt", "r", encoding="utf-8") as file:
    diary = file.read()

print("오늘의 일기:")
print(diary)
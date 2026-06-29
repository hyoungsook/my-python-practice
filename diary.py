diary = input("오늘의 일기를 입력하세요: ")

with open("diary.txt", "w", encoding="utf-8") as file:
    file.write(diary)

print("일기가 저장되었습니다.")
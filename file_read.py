memo = input("메모를 입력하세요: ")

with open("memo.txt", "w", encoding="utf-8") as file:
    file.write(memo)

print("메모가 저장되었습니다.")
memo = input("메모를 입력하세요: ")

file = open("memo.txt", "w", encoding="utf-8")
file.write(memo)
file.close()

print("메모가 저장되었습니다.")
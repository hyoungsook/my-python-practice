def add_memo():
    memo = input("메모를 입력하세요: ")

    with open("memos.txt", "a", encoding="utf-8") as file:
        file.write(memo + "\n")

    print("메모가 저장되었습니다.")


def show_memos():
    try:
        with open("memos.txt", "r", encoding="utf-8") as file:
            memos = file.readlines()

        print("저장된 메모:")

        for memo in memos:
            print("- " + memo.strip())

    except FileNotFoundError:
        print("아직 저장된 메모가 없습니다.")

def clear_memos():
    with open("memos.txt", "w", encoding="utf-8") as file:
        file.write("")

    print("모든 메모를 삭제했습니다.")

while True:
    print()
    print("메모장 프로그램")
    print("1. 메모 추가")
    print("2. 메모 보기")
    print("3. 종료")
    print("4. 전체 메모 삭제")


    choice = input("선택: ")

    if choice == "1":
        add_memo()
    elif choice == "2":
        show_memos()
    elif choice == "3":
        print("프로그램을 종료합니다.")
        break
    elif choice == "4":
        clear_memos()
    
    else: 
        print("잘못된 선택입니다.")
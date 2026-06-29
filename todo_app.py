def load_todos():
    try:
        with open("todos.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()

        result = []

        for todo in todos:
            result.append(todo.strip())

        return result

    except FileNotFoundError:
        return []


def save_todos(todos):
    with open("todos.txt", "w", encoding="utf-8") as file:
        for todo in todos:
            file.write(todo + "\n")


def show_todos(todos):
    if len(todos) == 0:
        print("할 일이 없습니다.")
    else:
        print("할 일 목록:")

        for index, todo in enumerate(todos, start=1):
            print(str(index) + ". " + todo)


def add_todo(todos):
    todo = input("추가할 할 일: ")
    todos.append(todo)
    save_todos(todos)
    print("할 일이 추가되었습니다.")


def delete_todo(todos):
    show_todos(todos)

    if len(todos) == 0:
        return

    number = int(input("삭제할 번호: "))

    if number >= 1 and number <= len(todos):
        deleted = todos.pop(number - 1)
        save_todos(todos)
        print("삭제됨:", deleted)
    else:
        print("없는 번호입니다.")


todos = load_todos()

while True:
    print()
    print("할 일 관리 프로그램")
    print("1. 할 일 보기")
    print("2. 할 일 추가")
    print("3. 할 일 삭제")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        show_todos(todos)
    elif choice == "2":
        add_todo(todos)
    elif choice == "3":
        delete_todo(todos)
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다.")
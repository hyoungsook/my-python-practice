todos = []

while True:
    todo = input("할 일을 입력하세요. 끝내려면 q 입력: ")

    if todo == "q":
        break

    todos.append(todo)

print("오늘의 할 일:")
for item in todos:
    print("- " + item)
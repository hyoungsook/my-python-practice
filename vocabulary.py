words = {
    "apple": "사과",
    "banana": "바나나",
    "cat": "고양이"
}

word = input("영어 단어를 입력하세요: ")

if word in words:
    print(words[word])
else:
    print("단어장에 없는 단어입니다.")
def toggle_text(text: str):
    for alphabet in text:
        if 'A' <= alphabet <= 'Z':
            toggle_alphabet = chr(ord(alphabet) + 32) #ord를 이해를 잘하지 못하여 검색해보니 예 'A' -> 65 로 바꿔주는 것이며
            print(toggle_alphabet, end="") #chr은 그 반대로 예 65 -> 'A' 로 바꿔 주는 것이라는 것을 알게되었습니다.
        elif 'a' <= alphabet <= 'z': # 아스키코드 표를 보고 A = 65 / a = 97 확인했습니다.
            toggle_alphabet = chr(ord(alphabet) - 32)
            print(toggle_alphabet, end="")
        else:
            print("영어 단어를 입력해주세요")

def main():
    text = input("영어 단어를 입력해주세요 (대문자 -> 소문자 / 소문자 -> 대문자)")
    toggle_text(text)

if __name__ == "__main__":
    main()
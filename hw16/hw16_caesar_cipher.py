def caesar_encode(text: str, shift: int = 3):
    shift = 3
    result = []
    for alphabet in text :
        if alphabet.isalpha(): #알파벳 여부를 판단하는 함수로 검색을 통해 알았습니다.
            if alphabet.isupper(): #추가로 대문자 인지를 파악하기 위해 대문자 여부는 isupper(), 소문자 여부는 islower()을 검색을 통해 알았습니다.
                if alphabet == "X":
                    result.append("A")
                elif alphabet == "Y":
                    result.append("B")
                elif alphabet == "Z":
                    result.append("C")
                else:
                    result.append(chr((ord(alphabet) - ord('A') ) % 26 + ord('A') + shift))
            else:  
                if alphabet == "x":
                    result.append("a")
                elif alphabet == "y":
                    result.append("b")
                elif alphabet == "z":
                    result.append("c")
                else:
                    result.append(chr((ord(alphabet) - ord('a') ) % 26 + ord('a') + shift))
        else:
            result.append(alphabet)
    
    print(result)

def caesar_decode(text: str, shift: int = 3):
    shift = 3
    result_decode = []
    for alphabet in text:
        if alphabet.isalpha():
             if alphabet.isupper():
                if alphabet == "A":
                    result_decode.append("X")
                elif alphabet == "B":
                    result_decode.append("Y")
                elif alphabet == "C":
                    result_decode.append("Z")
                else:
                    result_decode.append(chr((ord(alphabet) - ord('A')) % 26 + ord('A') - shift))
             else:
                if alphabet == "a":
                    result_decode.append("x")
                elif alphabet == "b":
                    result_decode.append("y")
                elif alphabet == "c":
                    result_decode.append("z")
                else:
                    result_decode.append(chr((ord(alphabet) - ord('a')) % 26 + ord('a') - shift))
        else:
            result_decode.append(alphabet)

    print(result_decode)


def main():
    if "인코딩" == input("인코딩 하실건가요? 아니면 디코딩 하실건가요?"):
        text_encode = input("암호를 입력하세요(encode)")
        caesar_encode(text_encode)
    else :
        text_decode = input("암호를 입력하세요(decode)")
        caesar_decode(text_decode)
    

if __name__ == "__main__":
    main()
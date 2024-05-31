import tkinter as tk
from tkinter import simpledialog
window = tk.Tk()
window.withdraw()
def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def caesar_encode(text: str, shift):
    result = ""
    for alphabet in text:
        if alphabet.isalpha():
            if alphabet.isupper():
                encoded_chr = chr(((ord(alphabet) - ord('A') + shift) % 26) + ord('A'))
            else:
                encoded_chr = chr(((ord(alphabet) - ord('a') + shift) % 26) + ord('a'))
        else:
            encoded_chr = alphabet
        result += encoded_chr
    return result

def caesar_decode(text: str, shift):
    return caesar_encode(text, -shift)

def main():
    action = gui_input("인코딩 하실건가요? 디코딩 하실건가요?")
    text = gui_input("암호를 입력하세요")
    shift = int(gui_input("칸 수를 입력해주세요")) % 26

    if action == "인코딩":
        encoded_text = caesar_encode(text, shift)
        print(f"인코딩 문자 : {encoded_text}" )
    else:
        decoded_text = caesar_decode(text, shift)
        print(f"디코딩 문자 : {decoded_text}")

if __name__ == "__main__":
    main()
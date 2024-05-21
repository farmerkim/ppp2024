import tkinter as tk
from tkinter import simpledialog
window = tk.Tk()
window.withdraw()
def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def toggle_text(text: str):
    for alphabet in text:
        if 'A' <= alphabet <= 'Z':
            toggle_alphabet = chr(ord(alphabet) + 32)
            print(toggle_alphabet, end="")
        elif 'a' <= alphabet <= 'z':
            toggle_alphabet = chr(ord(alphabet) - 32)
            print(toggle_alphabet, end="")
        else:
            print("영어 단어를 입력해주세요")

def main():
    text = gui_input("영어 단어를 입력해주세요 (대문자 -> 소문자 / 소문자 -> 대문자)")
    toggle_text(text)

if __name__ == "__main__":
    main()
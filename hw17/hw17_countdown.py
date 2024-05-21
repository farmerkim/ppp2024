import time
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()
 
def gui_input(text: str) -> str:
 return simpledialog.askstring(title="Test", prompt=text)

def main():
    count = int(gui_input("몇 초 카운트 할까요?"))

    while True:
        print(f"카운트 다운 ... {count}", end="\r")
        time.sleep(1)
        count -= 1
        if count <= 0:
            break
    print()
    print("Bomb!!")

if __name__ == "__main__":
    main()
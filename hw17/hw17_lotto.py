import random

import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()
 
def gui_input(text: str) -> str:
 return simpledialog.askstring(title="Test", prompt=text)

def get_lotto():
    result = []
    while True:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
        if len(result) == 6:
            return sorted(result)
        
def lotto_one():   
    count = int(gui_input("로또 몇개 필요하신가요?"))
    for i in range(count):
        lotto_nums = get_lotto()
        print(f"{chr(65+i)} 수 동: {lotto_nums}")
        
def main():
    lotto_one()
    
if __name__ == "__main__":
    main()
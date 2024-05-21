import random
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
 return simpledialog.askstring(title="Test", prompt=text)

def gugudan():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    result = num1 * num2
    return num1, num2, result

def main():
    
    questions = int(gui_input("몇문제 풀고 싶으신가요?"))
    correct_count = 0

    for _ in range(questions):
        num1, num2, correct_result = gugudan()
        user_result = int(input(f"{num1} * {num2} = "))

        if correct_result == user_result:
            print("정답입니다.")
            correct_count += 1
        else:
            print("오답입니다.")
    
    print(f"{questions} 중 맞은 갯수는 {correct_count} 입니다.")

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()
 
def gui_input(text: str) -> str:
 return simpledialog.askstring(title="Test", prompt=text)

def update_shown_answer(shown_answer, hidden_answer, x):
    result = []

    for shown_text, hidden_text in zip(shown_answer, hidden_answer):
        if shown_text == "_":
            if hidden_text == x:
                result.append(x)
            else:
                result.append("_")
        else:
            result.append(shown_text)
    return "".join(result)
            

def main():
    hiden_answer = gui_input("어떤 단어로 행맨을 할까요?")
    shown_answer = ["_" for _ in range(len(hiden_answer))]
    trial = 3
    
    while True:
        x = gui_input(f"({shown_answer}, 목숨 = {trial})글자를 입력하시오 => ?")
        if x in hiden_answer:
            shown_answer = update_shown_answer(shown_answer, hiden_answer, x)
        else:
            trial -= 1
        if "_" not in shown_answer:
            print("축하합니다. 정답입니다.")
            break

        if trial <= 0 :
            print("정답을 맞추지 못했습니다.")
            print(f"정답은 {hiden_answer}입니다.")
            break

if __name__=="__main__":
    main()
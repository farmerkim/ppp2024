calories = { "한라봉": 50, "딸기": 34, "바나나": 77}

f=input("무슨 과일을 드셨나요?")

g=int(input("몇 그램 드셨나요?"))

if f == "한라봉" :
    print(g*calories["한라봉"]/100)
elif f == "딸기" :
    print(g*calories["딸기"]/100)
elif f == "바나나" :
    print(g*calories["바나나"]/100)
else :
    print("과일이 없습니다.")
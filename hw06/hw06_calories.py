def calories_total(fruit_calories, fruit_name):
    calories_total = 0
    
    for i in fruit_name:
        count = int(input(f"{i} 몇개를 드셨나요?"))
        weight = int(input(f"{i} 몇g 드셨나요?"))
        calories_total += fruit_calories[i]*count*weight/100
    if i == fruit_name[len(fruit_name)-1]:
        print(f"총 칼로리의 합계는 {calories_total} kcal 입니다.")
def main ():
    fruit_calories = { "한라봉": 50, "딸기": 34, "바나나": 77}
    fruit_name = ["한라봉", "딸기", "바나나"]
    calories_total(fruit_calories, fruit_name)

if __name__=="__main__":
    main()
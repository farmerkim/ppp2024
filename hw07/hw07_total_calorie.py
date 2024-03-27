def total_calorie(fruits, fruits_calorie_dic):
    total_calorie = 0
    for fruit, weight in fruits.items():
        if fruit in fruits_calorie_dic:
            total_calorie += weight*fruits_calorie_dic[fruit]/100
    return total_calorie

def main():
    fruits = {"딸기" : 300, "한라봉" : 150}
    fruits_calorie_dic = {"한라봉" : 50, "딸기" : 34, "바나나" : 77}
    print(f"총 칼로리는 {total_calorie(fruits, fruits_calorie_dic)}입니다.")

if __name__ == "__main__":
    main()
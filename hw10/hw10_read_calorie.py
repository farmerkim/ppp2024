def total_calorie(fruits_eat, fruits_cal_dic):
    total = 0
    for fruit_name, grams in fruits_eat.items():
        if fruit_name in fruits_cal_dic:
            total += fruits_cal_dic[fruit_name] * grams / 100
        else:
            print(f"{fruit_name}의 정보를 찾을 수 없습니다.")
    return total

def read_cal_db(filename):
    database = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        
        for line in lines[1:]:
            token = line.split(",")
            fruit_name = token[0]
            fruit_cal = int(token[1])
            database[fruit_name] = fruit_cal

    return database

def main():
    fruits_calorie_dic = read_cal_db("calorie_db.csv")
    fruits_eat = input("어떤 음식을 드셨나요?").split(",")
    fruits_eat = {fruit: int(input(f"{fruit}을 몇 그램 드셨나요?"))for fruit in fruits_eat}
    total = total_calorie(fruits_eat, fruits_calorie_dic)
    print(f"총칼로리는 {total}입니다.")

if __name__ == "__main__":
    main()
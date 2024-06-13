#과일 칼로리 데이터 베이스

import os
import csv
import pickle
import numpy as np

DB_FILE = "./calorie_db_eat.pkl"

def read_db():
    if not os.path.exists(DB_FILE):
        return {}
    
    with open(DB_FILE, "rb") as f:
        calorie_db = pickle.load(f)
    return calorie_db

def write_db(calorie_db):
    with open(DB_FILE, "wb") as fout:
        pickle.dump(calorie_db, fout)

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
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            fruit_name = row[0]
            fruit_cal = int(row[1])
            database[fruit_name] = fruit_cal
    return database

def main():
    fruits_calorie_dic = read_cal_db("calorie_db.csv")
    
    fruits_eat = input("어떤 과일을 드셨나요?").split(",")
    fruits_eat = {fruit.strip(): int(input(f"{fruit.strip()}을(를) 몇 그램 드셨나요? ")) for fruit in fruits_eat}
    
    total = total_calorie(fruits_eat, fruits_calorie_dic)
    print(f"총 섭취 칼로리는 {total} kcal입니다.")
    
    calorie_total = read_db()
    
    for fruit, grams in fruits_eat.items():
        if fruit in calorie_total:
            calorie_total[fruit].append(grams)
        else:
            calorie_total[fruit] = grams
    
    print(f"현재까지 드신 과일 목록과 섭취량: {calorie_total}")
    
    fruit_averages = {fruit: np.mean(grams_list) for fruit, grams_list in calorie_total.items()}
    
    print(f"현재까지 드신 과일의 평균 섭취량: {fruit_averages}")
    
    write_db(calorie_total)

if __name__ == "__main__":
    main()
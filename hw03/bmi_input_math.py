import math

height_cm = int(input("키를 입력하세요"))
weight = int(input("몸무게를 입력하세요"))
height_m = height_cm/100

bmi = weight / math.pow(height_m, 2)
print("키가 {}cm, 몸무게가 {}kg이면, bmi는 {}입니다" .format(height_cm, weight, bmi) )
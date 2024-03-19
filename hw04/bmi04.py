import math

height_cm = int(input("키를 입력하세요"))
weight = int(input("몸무게를 입력하세요"))
height_m = height_cm/100

bmi = weight / math.pow(height_m, 2)
print("키가 {}cm, 몸무게가 {}kg이면, bmi는 {}입니다" .format(height_cm, weight, bmi) )

if 23 < bmi < 24.9 :
    print(input("비만 전단계입니다."))
elif 25 < bmi < 29.9 :
    print(input("1단계 비만입니다."))
elif 30 < bmi < 34.9 :
    print(input("2단계 비만입니다."))
elif 35 <= bmi  :
    print(input("3단계 비만입니다."))
else :
    print(input("정상입니다."))

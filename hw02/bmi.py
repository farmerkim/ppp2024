weight = int((input("몸무게를 입력하세요 >>> ")))
height = int((input("키를 입력하세요 (단위: cm) >>> ")))

height_m = height / 100

bmi = weight / (height_m*height_m)

print(bmi)
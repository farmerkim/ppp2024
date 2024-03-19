import math

r = int(input("원의 반지름을 입력하세요?"))

area = math.pi*r*r

format_area = print("원의면적은 {:.2f} 입니다".format (area))

l = math.pi*2*r

print("반지름이 {}인 원의 둘레는 {:.1f}입니다." .format(r, l))
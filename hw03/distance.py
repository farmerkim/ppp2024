import math

x1 = int(input("x1의 좌표를 적으세요"))
y1 = int(input("y1의 좌표를 적으세요"))
x2 = int(input("x2의 좌표를 적으세요"))
y2 = int(input("y2의 좌표를 적으세요"))

X = (x1-x2)
Y = (y1-y2)

distance = math.sqrt(math.pow(X, 2) + math.pow(Y, 2))

print("두지점 사이의 거리는 {} 입니다" .format(distance))
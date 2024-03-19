
x = int(input("x의 좌표를 적으세요"))
y = int(input("y의 좌표를 적으세요"))

if x > 0 and y > 0 :
    print("1사분면 입니다.")
if x < 0 and y > 0 :
    print("2사분면 입니다.")
if x < 0 and y < 0 :
    print("3사분면 입니다.")
if x > 0 and y < 0 :
    print("4사분면 입니다.")
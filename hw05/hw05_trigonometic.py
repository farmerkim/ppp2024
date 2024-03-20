import math

start_angle = int(input("시작 각도는 무엇인가요?"))
end_angle = int(input("끝 각도는 무엇인가요?"))
size = int(input("각의 간격을 입력하세요"))

for i in range(start_angle, end_angle+1, size) :
    rad = math.radians(i)
    sine = math.sin(rad)
    cosine = math.cos(rad)
    tangent = math.tan(rad)
    print(f"{i}/{rad:.4f}/{sine:.4f}/{cosine:.4f}/{tangent:.4f}")


dan = int(input("몇단이 궁금하신가요?"))

dan_max = int(input("몇까지 알고 싶으신가요?"))

for i  in range(dan_max):
   print(f"{dan} * {i+1} = {dan * (i+1)}")
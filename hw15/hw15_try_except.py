def input_num():
    numbers = []
    while True:
        try:
            num_input = (input("정수를 입력하세요(-1 입력시 종료됩니다)"))
            num_list = num_input.split(",")
            for num_str in num_list:
                num = int(num_str)
                if num == -1:
                    return numbers
                elif num <= 0:
                    print("자연수를 입력하세요")
                    continue
                numbers.append(num)
        except ValueError:
            print("정수를 입력해주세요") 

def caculate(numbers):
    count = len(numbers)
    total = sum(numbers)
    if count > 0:
        average = total / count
        return count, average

def main():
    numbers = input_num()
    if numbers:
        count, average = caculate(numbers)
        print(f"입력한 숫자들 : {numbers}")
        print(f"입력한 숫자들의 총 갯수 : {count}")
        print(f"입력한 숫자들의 평균 : {average}")

if __name__=="__main__":
    main()
        

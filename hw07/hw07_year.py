def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    y = int(input("몇년도가 윤년인지 궁금하신가요?"))
    if is_leap_year(y):
        print(f"{y}는 윤년입니다.")
    else:
        print(f"{y}윤년이 아닙니다.")

if __name__ == "__main__":
    main()
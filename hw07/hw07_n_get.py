def get_range_list(n):
    return list(range(1, n+1))

def main():
    n = int(input("n의 값을 입력하세요"))
    print(f"1부터 {n}까지의 리스트는 {get_range_list(n)}입니다.")

if __name__ == "__main__":
    main()
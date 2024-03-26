def sum_n(n):
    return (n*(n+1))//2

def main():
    n = int(input("몇까지의 합을 구할까요?"))
    sum = sum_n(n)
    print(f"1부터 {n}까지의 합은 {sum}입니다.")

if __name__=="__main__":
    main()
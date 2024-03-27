def average(nums):
    total = sum(nums)
    avg = sum(nums)/len(nums)
    return avg

def main():
    nums = [1, 2, 3, 4, 5]
    print(f"숫자들의 평균은 {average(nums)}입니다.")

if __name__ == "__main__":
    main()
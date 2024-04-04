def count(nums):
    return len(nums)

def average(nums):
    return sum(nums)/len(nums)

def median(nums): 
    sorted_nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        median1 = (sorted_nums[n//2])
        median2 = (sorted_nums[n//2 - 1])
        if median1 > median2:
            return median1
        else:
            return median2
    else:
        return sorted_nums[n//2]
    
def read_file(file_name):
        data = []
        with open (file_name) as f:
             lines = f.readlines()
             for line in lines:
                  text2 = line.strip()
                  value = int(text2)
                  data.append(value)
        return data

def main():
    nums = read_file("number2.txt")
    print(f"주어진 숫자의 갯수는 {count(nums)} 입니다.")
    print(f"평균값은 {average(nums):.1f} 입니다.")
    print(f"중앙값은 {median(nums):.1f} 입니다.")
    print(f"최솟값은 {min(nums)} 입니다.")
    print(f"최댓값은 {max(nums)} 입니다.")

if __name__ == "__main__":
    main()
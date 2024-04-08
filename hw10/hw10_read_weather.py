def read_tavg(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            tavg = float(token[4])
            result.append(tavg)
    return result

def read_rainfall(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            rainefall = float(token[-3])
            if rainefall > 5:
                result.append(rainefall)
    return result

def main():
    average = read_tavg("weather(146)_2022-2022.csv")
    rainefall = read_rainfall("weather(146)_2022-2022.csv")
    print(f"연평균 기온은{sum(average)/len(average):.1f}도 입니다.")
    print(f"5mm 이상인 강우일수는 {len(rainefall)}일 입니다.")
    print(f"5mm 이상인 강우총 강우량은 {sum(rainefall)}mm 입니다.")

if __name__=="__main__":
    main()

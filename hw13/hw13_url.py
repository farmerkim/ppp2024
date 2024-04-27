import os
import requests

url = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"

filename = "weather_146_2020-2020.csv"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        res = requests.get(url)
        f.write(res.text)

def read_tavg(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            tavg = float(token[4])
            result.append(tavg)
    return result

def read_rainfall_over_5(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            rainefall = float(token[-3])
            if rainefall >= 5:
                result.append(rainefall)
    return result

def read_rainfall(filename):
    result = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            rainefall = float(token[-3])
            result.append(rainefall)
    return result

def main():
    average = read_tavg(filename)
    rainfall_over_5 = read_rainfall_over_5(filename)
    rainfall = read_rainfall(filename)
    with open ("weather_results.txt", "w") as f:
        f.write("Total average : {}\n ".format(sum(average) / len(average)))
        f.write("Over 5mm : {}\n ".format(len(rainfall_over_5)))
        f.write("Rainfall : {}\n ".format(sum(rainfall))) # \n 으로 줄바꿈을 해보고 새파일을 만들었습니다. 텍스트를 한글로 했더니 물음표로 나와서 영어로 변환했습니다.

if __name__=="__main__":
    main()

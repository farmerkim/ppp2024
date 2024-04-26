#import os
#import requests

#url = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"

#filename = "weather_146_2020-2020.csv"

#if not os.path.exists(filename):
    #with open(filename, "w") as f:
        #res = requests.get(url)
        #f.write(res.text)

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
    filename = "weather_146_2020-2020.csv"
    average = read_tavg(filename)
    rainfall_over_5 = read_rainfall_over_5(filename)
    rainfall = read_rainfall(filename)
    with open (filename, "w") as f:
        f.write(str(sum(average)/len(average))) #여기서 len 값이 자꾸 0이라서 에러가 뜹니다.
        f.write(str(len(rainfall_over_5))) #추가로 위에거를 일단 주석처리하고 다른 것 해보니 int가 아닌 str로 표현해야 한다고해서 str 다 붙였습니다.
        f.write(str(sum(rainfall)))#그랬더니 sum 값만 나옵니다. len에 문제가 있는 것 같은데 도저히 모르겠습니다.

if __name__=="__main__":
    main()

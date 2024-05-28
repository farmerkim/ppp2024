import matplotlib.pyplot as plt
import requests
import os


def download(filename, URL):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8-sig") as f:
            res = requests.get(URL)
            f.write(res.text.replace("\r", ""))

def extract_temperatures(filename:str):
    summer_temps = []
    winter_temps = []
    with open(filename, encoding="utf-8-sig") as f:
        next(f) 
        for line in f:
            tokens = line.strip().split(",")
            if len(tokens) < 5:
                continue
            month = int(tokens[0].split("-")[1])
            temp = float(tokens[2])
            if 6 <= month <= 8:
                summer_temps.append(temp)
            elif month == 12 or month <= 2:
                winter_temps.append(temp)
    return summer_temps, winter_temps


def main():
   
    filename = "weather(146)_1980-2023.csv"

    start_year = "1980"
    end_year = "2023"
    start_month = "01"
    end_month = "12"
    start_day = "01"
    end_day = "31"


    URL =  f"https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt={start_year}{start_month}{start_day}&endDt={end_year}{end_month}{end_day}&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay={start_year}{start_month}{start_day}&startYear={start_year}&endDay={end_year}{end_month}{end_day}&endYear={end_year}&startMonth={start_month}&endMonth={end_month}&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize=%22"
    
    download(filename, URL)
    
    download(filename, URL)

    summer_temps, winter_temps = extract_temperatures(filename)
    
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    plt.hist(summer_temps, color="k", label="여름")
    plt.hist(winter_temps, color="b", label="겨울")
    plt.title("여름철, 겨울철 온도분포")
    plt.xlabel("온도")
    plt.ylabel('빈도')
    plt.legend()
    plt.savefig("./summer_winter_temp_plot.png")

if __name__ == "__main__":
    main()
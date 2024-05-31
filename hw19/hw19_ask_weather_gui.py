import requests
import os

import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

window = tk.Tk()
window.withdraw()
def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)

def download(filename, URL):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8-sig") as f:
            res = requests.get(URL)
            f.write(res.text.replace("\r", ""))

# def gui_weather_tmax(filename, year, month, day):
#     with open(filename, encoding="utf-8-sig") as f:
#         lines = f.readlines()
#         for line in lines[8:]:
#             tokens = line.strip().split(",")
#             date = tokens[0].split("-")
#             if date[0] == year and date[1] == month and date[2] == day:
#                 return float(tokens[-1])

#위와 같은 방법이 작동을 하지 않아서 찾아보니 날짜와 시간을 다루는 모듈을 알게되어 사용해보았습니다.

def gui_weather_tmax(filename, year, month, day):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            date_str = tokens[0]
            date_obj = datetime.strptime(date_str, "%Y-%m-%d") #날짜를 문자열로 하는 strptime 함수도 추가로 알게되었습니다.
            if date_obj.year == int(year) and date_obj.month == int(month) and date_obj.day == int(day):
                return float(tokens[-1])

def gui_weather_tmin(filename, year, month, day):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            date_str = tokens[0]
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            if date_obj.year == int(year) and date_obj.month == int(month) and date_obj.day == int(day):
                return float(tokens[-2])
            
def gui_weather_tavg(filename, year, month, day):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[8:]:
            tokens = line.strip().split(",")
            date_str = tokens[0]
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            if date_obj.year == int(year) and date_obj.month == int(month) and date_obj.day == int(day):
                return float(tokens[-3])

            
def main():

    filename = "weather(146)_1980-2023.csv"

    start_year = "1980"
    end_year = "2023"
    start_month = "01"
    end_month = "12"
    start_day = "01"
    end_day = "31"

    URL = f"https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt={start_year}{start_month}{start_day}&endDt={end_year}{end_month}{end_day}&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay={start_year}{start_month}{start_day}&startYear={start_year}&endDay={end_year}{end_month}{end_day}&endYear={end_year}&startMonth={start_month}&endMonth={end_month}&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize=%22"

    download(filename, URL)

    what = gui_input("최고온도, 최저온도, 평균온도 중에 어떤 것이 궁금하신가요?")
    year = gui_input("궁금한 년도를 입력하세요(1980년부터 2023년까지 중에서)")
    month =  gui_input("궁금한 월을 입력하세요")
    day = gui_input("궁금한 날짜를 입력하세요")
    

    tmax = gui_weather_tmax(filename, year, month, day)
    tmin = gui_weather_tmin(filename, year, month, day)
    tavg = gui_weather_tavg(filename, year, month, day)

    if what == "최고온도":
        if tmax:
            print(f"{year}년 {month}월 {day}일의 최고 온도는 {tmax}입니다.")
        else:
            print("해당하는 날짜의 데이터가 없습니다.")
    elif what == "최저온도":
        if tmin:
            print(f"{year}년 {month}월 {day}일의 최저 온도는 {tmin}입니다.")
        else:
            print("해당하는 날짜의 데이터가 없습니다.")
    elif what == "평균온도":
        if tavg:
            print(f"{year}년 {month}월 {day}일의 평균 온도는 {tavg}입니다.")
        else:
            print("해당하는 날짜의 데이터가 없습니다.")
    else:
        print("최고온도, 최저온도, 평균온도 중에서 선택해주세요.")

if __name__ == "__main__":
    main()
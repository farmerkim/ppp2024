import os
import requests

def download(url:str, filename:str):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="cp949") as f:
            res = requests.get(url)
            f.write(res.text.replace("\r", ""))

def temperature_max(filename:str):
    """최대온도와 최대온도 날짜를 구하기"""
    max_temp = None
    max_temp_date = None
    with open(filename, encoding="cp949") as f: 
        for line in f:
            token = []
            token = line.strip().split(",")
            if "" in token :
                continue
            try: #모르는 부분을 찾던 도중 try-except 함수를 알게 되었습니다. 
                temp = float(token[-1])
                if max_temp is None or temp > max_temp:
                    max_temp = temp
                    max_temp_date = token[0]
            except ValueError:
                pass 
    return max_temp, max_temp_date

def temperature_diff_max(filename):
    """최대일교차와 최대일교차 날짜를 구하기"""
    max_diff = None
    max_diff_date = None
    with open(filename, encoding="cp949") as f:
        for line in f:
            token = line.strip().split(",")
            if "" in token :
                continue    
            try:
                temp_diff = float(token[-1]) - float(token[-2])
                if max_diff is None or temp_diff > max_diff:
                    max_diff = temp_diff
                    max_diff_date = token[0]
            except ValueError:
                pass
    return max_diff, max_diff_date

def submit(name: str, tmax: float, tmax_date: str, tdiff_max : float, tdiff_max_date : str) -> None:
    URL = "https://script.google.com/macros/s/AKfycbybB2LSi0F85FkC4KmI0XgjMqvhn7-6eJjZQi0oucbgbEvwDmNVRoyMMnd5UyezpqJp/exec"
    PARAMS = {
        '제출자': name,
        '최대온도': tmax,
        '최대온도날짜': tmax_date,
        '최대일교차': tdiff_max,
        '최대일교차날짜': tdiff_max_date,
    }
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")

def main():

    url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st" \
      "drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns" \
      "=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190" \
      "4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3" \
      "%BC&stnId=146&areaId=&gFontSize="
    filename = "ta_20240430210656.csv"

    download(url, filename)

    tmax, tmax_date = temperature_max(filename)
    tdiff_max, tdiff_max_date = temperature_diff_max(filename)

    name = "김준모"

    with open ("temperature", "w") as f:
        f.write(f"최대온도와 최대온도 날짜 : {tmax} {tmax_date}\n ")
        f.write(f"최대일교차와 최대일교차 날짜 : {tdiff_max} {tdiff_max_date}\n ")

    submit(name, tmax, tmax_date, tdiff_max, tdiff_max_date)

if __name__ == "__main__":
    main()
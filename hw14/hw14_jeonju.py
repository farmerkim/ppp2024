import sys
import os
import requests

url = "https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&st" \
      "drMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns" \
      "=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=190" \
      "4&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3" \
      "%BC&stnId=146&areaId=&gFontSize="

filename = "ta_20240430210656.csv"

if "./" not in sys.path:
     sys.path.append("./")

if not os.path.exists(filename):
    with open(filename, "w") as f:
        res = requests.get(url)
        f.write(res.text)

def temperature_max(filename):
    max_temp = None
    max_temp_date = None
    with open(filename, encoding="utf-8-sig") as f:
        first_line = True #줄로 읽게하여 최대온도와 최대온도날짜를 표현해보았습니다.
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            temp = float(token[4])
            if first_line or temp > max_temp:
                max_temp_date = token[0]
                first_line = False
    return max_temp, max_temp_date

def temperature_diff_max(filename):
    max_diff = None
    max_diff_date = None
    with open(filename, encoding="utf-8-sig") as f:
        first_line = True
        lines = f.readlines()
        for line in lines[1:]:
            token = line.split(",")
            temp_diff = (float(token[4])-float(token[3]))
            if first_line or temp_diff > max_diff:
                max_diff = temp_diff
                max_diff_date = (token[0])
                first_line = False
    return max_diff, max_diff_date

# from hw14_jeonju import hw_submission

def submit(name: str, temperature_max: float, temperature_max_date: str, gap_max: float, gap_max_date: str) -> None:
    URL = "https://script.google.com/macros/s/AKfycbybB2LSi0F85FkC4KmI0XgjMqvhn7-6eJjZQi0oucbgbEvwDmNVRoyMMnd5UyezpqJp/exec"
    PARAMS = {
        '제출자': name,
        '최대온도': temperature_max,
        '최대온도날짜': temperature_max_date,
        '최대일교차': gap_max,
        '최대일교차날짜': gap_max_date,
    }
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")
def download():
    pass

def main():
    #download(filename, url)

    tmax, tmax_date = temperature_max(filename)
    tdiff_max, tdiff_max_date = temperature_diff_max(filename)

    with open ("temperature", "w") as f:
        f.write("최대온도와 최대온도 날짜 : {} {}\n " .format(tmax, tmax_date))
        f.write("최대일교차와 최대일교차 날짜 : {} {}\n " .format(tdiff_max, tdiff_max_date))

    submit("김준모", tmax, tmax_date, tdiff_max, tdiff_max_date)

if __name__ == "__main__":
    main()

    #return codecs.utf_8_decode(input, errors, final) 이런식으로 뜨면서 파일에 에러가 있다고 뜹니다.
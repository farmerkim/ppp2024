def read_date(weather_filename):
    dataset = []
    with open(weather_filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            year, month, day = tokens[:3]
            dataset.append((year, month, day, float(tokens[3]), float(tokens[5])))
    return dataset

def temp_diff_year(date_temp_diff):
    max_temp_diff_year = {}
    for i in date_temp_diff:
        year = i[0]
        temp_diff = i[3] - i[4]
        if year in max_temp_diff_year:
            if temp_diff > max_temp_diff_year[year][1]:
                max_temp_diff_year[year] = (i[:3], temp_diff)
        else:
            max_temp_diff_year[year] = (i[:3], temp_diff)
    return max_temp_diff_year
           
def main():
    filename = "weather(146)_2001-2022.csv"
    dates_and_temp = read_date(filename)
    max_temp_diff_year = temp_diff_year(dates_and_temp)

    for temp_diff in max_temp_diff_year.items():
        print(f"최대 일교차는 {temp_diff}C 입니다.")

if __name__=="__main__":
    main()
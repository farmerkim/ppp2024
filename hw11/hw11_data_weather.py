def read_col(weather_filename, col_index):
    dataset = []
    with open(weather_filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_index]))
    return dataset

def read_col_int(weather_filename, col_index):
    dataset = []
    with open(weather_filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[col_index]))
    return dataset

def read_logest_rainy_day(rainfall):
    max_rainy_days = 0
    current_rainy_days = 0
    for rain in rainfall:
        if rain > 0:
            current_rainy_days += 1
            if current_rainy_days > max_rainy_days:
                max_rainy_days = current_rainy_days
        else:
            current_rainy_days = 0
    return max_rainy_days

def read_max_rainfall(rainfall):
    rain_event=[]
    prev_raincount =0
    for rain in rainfall:
        if rain == 0:
            if prev_raincount > 0:
                rain_event.append(prev_raincount)
            prev_raincount = 0
        else:
            prev_raincount += rain
    if prev_raincount > 0:
        rain_event.append(prev_raincount)
    if len(rain_event) > 0:
        return max(rain_event)
    else:
        return 0
    

def top_rank(values, limit):
    return sorted(values, reverse=True)[:limit]

def sumifs(rainfall, months, conditions):
    total = 0
    for i in range(len(rainfall)):
        rain = rainfall[i]
        month = months[i % len(months)]
        if month in conditions:
            total += rain
    return total

def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_col(weather_filename, -3)
    longest_rainyday =  read_logest_rainy_day(rainfall)
    max_rainfall = read_max_rainfall(rainfall)
    tmax = read_col(weather_filename, 3)
    months = read_col_int(weather_filename, 1)
    print(f"최장 강우일 수는 {longest_rainyday}일 입니다.")
    print(f"강우 이벤트 중 최대 강수량은 {max_rainfall:.1f}")
    print(f"가장 더운날 top3는 {top_rank(tmax , 3)} 입니다.")
    print(f"여름철 [6,7,8] 총 강수량은 {sumifs(rainfall, months, [6,7,8]):.1f}mm 입니다.")


if __name__=="__main__":
    main()
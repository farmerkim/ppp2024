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

def gdd_season(tavg, months):
    total_gdd = 0
    for temp, month in zip(tavg, months):
        if month in [5,6,7,8,9]:
            eff_temp = temp - 5
            if eff_temp < 0:
                eff_temp = 0
            total_gdd += eff_temp
    return total_gdd

def gdd_per_year(tavg, months, years):
    yearly_gdd = {}
    for temp, month, year in zip(tavg, months, years):
        if month in [5, 6, 7, 8, 9]:
            eff_temp = temp - 5
            if eff_temp < 0:
                eff_temp = 0
            if year in yearly_gdd:
                yearly_gdd[year] += eff_temp
            else:
                yearly_gdd[year] = eff_temp
    
    return yearly_gdd

def main():
    filename = "weather(146)_2001-2022.csv"
    tavg = read_col(filename, 4)
    months = read_col_int(filename, 1)
    years = read_col_int(filename, 0)
    yearly_gdd = gdd_per_year(tavg, months, years)
    for year, gdd in yearly_gdd.items():
        print(f"{year}의 GDD는 {gdd:.1f}도일 입니다.")

if __name__=="__main__":
    main()

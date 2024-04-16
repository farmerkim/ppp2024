def read_col(weather_filename, col_index):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_index]))
    return dataset

def read_col_int(weather_filename, col_index):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(int(tokens[col_index]))
    return dataset

def get_data_ifs(values, conditions, criteria):
    dataset = []
    for value, condition in zip(values, conditions):
        if condition == criteria:
            dataset.append(value)
    return dataset


def main():
    weather_filename_all = "weather(146)_2001-2022.csv"
    
    rainfall = read_col(weather_filename_all, 9)
    year = read_col_int(weather_filename_all, 0)
    rainfall_2021 = get_data_ifs(rainfall, year, 2021)
    rainfall_2022 = get_data_ifs(rainfall, year, 2022)

    total_rainfall = sum(rainfall_2021) + sum(rainfall_2022)

    print(f"2021년과 2022년의 총 강수량은 {total_rainfall:.1f}mm 입니다.")

if __name__=="__main__":
    main()

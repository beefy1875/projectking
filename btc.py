from datetime import datetime

tbr  = {}
skip_first_line = True

with open ("btc-usd-max.csv") as file:
    for line in file:
        if skip_first_line:
            skip_first_line = False
            continue


        line = line.replace("\n", "")
        splits = line.split(",") 


        date = datetime.strptime(line[:10], "%Y-%m-%d")
        price = float(splits[1])

        tbr[date] = price

new_year = True
year_stored = 2012

current_count_for_year = 0
days_counted_for_year = 0

last_date = list(tbr)[-1]

for date, price in tbr.items():
    if year_stored != date.year or last_date == date:
        if days_counted_for_year > 0:
            average_price_for_year = current_count_for_year / days_counted_for_year
            print(f"In {year_stored}, the average price of the king was ${round(average_price_for_year, 2)}")
            days_counted_for_year = 1
            current_count_for_year = 0
        

        year_stored = date.year
    else:
        days_counted_for_year += 1
        current_count_for_year += price
from collections import defaultdict
import datetime

def count_initializations():
    log_file = "boot_log.txt"
    month_count = defaultdict(int)

    with open(log_file, "r") as f:
        for line in f:
            date_str = line.strip()
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            month_year = (date.year, date.month)
            month_count[month_year] += 1

    for month_year, count in sorted(month_count.items()):
        year, month = month_year
        print(f"{year}-{month:02d}: {count} initializations")

if __name__ == "__main__":
    count_initializations()
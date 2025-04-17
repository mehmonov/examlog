import csv
import datetime
from pathlib import Path

def get_streak_days():
    try:
        log_file = Path('data/daily_log.csv')
        if not log_file.exists() or log_file.stat().st_size == 0:
            return 0

        with open('data/daily_log.csv', 'r') as file:
            reader = csv.reader(file)
            logs = list(reader)

        if not logs:
            return 0

        dates = []
        for row in logs:
            if row:
                try:
                    date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
                    dates.append(date)
                except:
                    continue

        if not dates:
            return 0

        dates.sort(reverse=True)

        streak = 1
        for i in range(len(dates)-1):
            if (dates[i] - dates[i+1]).days == 1:
                streak += 1
            else:
                break

        return streak

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        return 0

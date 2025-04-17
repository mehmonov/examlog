import csv
import datetime

def log_progress(hours, vocab, reading, writing, math, tests):
    today = str(datetime.date.today())
    with open('data/daily_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today, hours, vocab, reading, writing, math, tests])


def get_progress():
    with open('data/daily_log.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

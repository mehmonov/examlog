import csv
import statistics

def generate_report():
    try:
        with open('data/daily_log.csv', newline='') as f:
            rows = list(csv.reader(f))[-7:]
            if len(rows) < 1:
                return "No data available."

            hours = [int(r[1]) for r in rows]
            reading = [int(r[3]) for r in rows]
            writing = [int(r[4]) for r in rows]
            math = [int(r[5]) for r in rows]
            tests = [int(r[6]) for r in rows]

            return (
                f"7-Day Summary:\n"
                f"Avg Hours: {statistics.mean(hours):.1f}\n"
                f"Avg Reading: {statistics.mean(reading):.1f}\n"
                f"Avg Writing: {statistics.mean(writing):.1f}\n"
                f"Avg Math: {statistics.mean(math):.1f}\n"
                f"Total Tests: {sum(tests)}"
            )
    except:
        return "No data available."

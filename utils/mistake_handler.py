import json
import datetime

def add_mistake(section, question, error_type, note):
    today = str(datetime.date.today())
    entry = {
        "date": today,
        "section": section,
        "question": int(question),
        "error_type": error_type,
        "note": note
    }
    try:
        with open('data/mistakes.json', 'r') as f:
            data = json.load(f)
    except:
        data = []
    data.append(entry)
    with open('data/mistakes.json', 'w') as f:
        json.dump(data, f, indent=2)

import json
from datetime import datetime

def parse_log_line(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Malformed log line")
    timestamp, level, message = parts
    try:
        datetime.strptime(timestamp, "%Y-%m-%d:%H:%M:%S")
    except ValueError:
        raise ValueError(f"Invalid timestamp format: {timestamp}")
    return {"timestamp": timestamp, "level": level, "message": message}

def load_logs(file_path):
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    logs.append(parse_log_line(line))
                except ValueError as e:
                    print("Skipping line:", e)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return logs

def analyze_logs(file_path):
    logs = load_logs(file_path)
    if not logs:
        print("No valid logs found.")
        return

    stats = {}
    total_time = 0
    count = 0

    for log in logs:
        lvl = log["level"].upper()
        stats[lvl] = stats.get(lvl, 0) + 1

        if "processing time" in log["message"]:
            try:
                time_part = log["message"].split(":")[-1].strip()
                total_time += int(time_part)
                count += 1
            except ValueError:
                print(f"Invalid time format in message: {log['message']}")

    avg_time = total_time / count if count > 0 else 0
    print("Average Processing Time:", avg_time)
    print("Log Level Counts:", stats)

    with open("log_summary.json", "w", encoding="utf-8") as out:
        json.dump({
            "stats": stats,
            "average_processing_time": avg_time
        }, out, indent=4)

    print("Summary written to log_summary.json")

def main():
    log_file = "server.log"
    start = datetime.now()
    analyze_logs(log_file)
    print("Analysis completed in", datetime.now() - start)

if __name__ == "__main__":
    main()

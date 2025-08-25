from pathlib import Path

def total_salary(file_path: str):
    p = Path(file_path)
    try:
        with p.open("r", encoding="utf-8") as f:
            total = 0.0
            count = 0
            for line in f:
                a = line.split(",")
                total +=  float(a[1])
                count += 1
    except:
        print(f"File not found or file have wrong format")
        return None,None
    avg = (total / count) if count else None
    summary = (total, avg)
    return summary

total, average = total_salary("./salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

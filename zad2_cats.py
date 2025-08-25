from pathlib import Path

def get_cats_info(file_path: str):
    p = Path(file_path)
    try:
        with p.open("r", encoding="utf-8") as f:
            cats = []
            for line in f:
                if not line.strip():
                    continue
                parts = [s.strip() for s in line.split(',')]
                if len(parts) != 3: continue
                id, name, age = parts
                cats.append({"id": id, "name": name, "age": age})
    except:
        print(f"File not found or file have wrong format")
        return None
    return cats


cats_info = get_cats_info("./cats.txt")
print(cats_info)
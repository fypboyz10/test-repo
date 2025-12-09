def mega_processor(data):
    cleaned = []
    for item in data:
        if isinstance(item, str):
            item = item.strip().lower()
            if item:
                cleaned.append(item)

    counts = {}
    for c in cleaned:
        counts[c] = counts.get(c, 0) + 1

    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    with open("output.txt", "w") as f:
        for k, v in sorted_items:
            f.write(f"{k}:{v}\n")

    return sorted_items

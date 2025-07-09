
import json
from collections import defaultdict
from typing import List,Dict,Any

# Step 1: Load data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
# Step 2: Calculate availability
def calculate_clinic_availability(slots):
    clinic_stats = defaultdict(lambda: {"total": 0, "booked": 0})

    for slot in slots:
        clinic_name = slot["clinicName"]
        clinic_stats[clinic_name]["total"] += 1
        if slot.get("booked", False):
            clinic_stats[clinic_name]["booked"] += 1

    for clinic, stats in clinic_stats.items():
        total = stats["total"]
        booked = stats["booked"]
        available = total - booked
        availability = round((available / total) * 100) if total > 0 else 0
        print(f"{clinic}: {availability}%")

if __name__ == "__main__":
    calculate_clinic_availability(data)
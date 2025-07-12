import json
from collections import defaultdict
from typing import List, Dict, Optional, TypedDict


class Slot(TypedDict):
    clinicId: str
    clinicName: str
    startTime: str
    endTime: str
    booked: Optional[bool]
    patientName: Optional[str]


class Availability(TypedDict):
    total: int
    booked: int
    available: int
    availability_percent: int


def calculate_clinic_availability(slots: List[Slot]) -> Dict[str, Availability]:
    clinic_stats: Dict[str, Availability] = defaultdict(lambda: {
        "total": 0,
        "booked": 0,
        "available": 0,
        "availability_percent": 0,
    })

    for slot in slots:
        clinic_name = slot["clinicName"]
        clinic_stats[clinic_name]["total"] += 1
        if slot.get("booked", False):
            clinic_stats[clinic_name]["booked"] += 1

    for clinic, stats in clinic_stats.items():
        stats["available"] = stats["total"] - stats["booked"]
        stats["availability_percent"] = round(
            (stats["available"] / stats["total"]) * 100
        ) if stats["total"] > 0 else 0

    return dict(clinic_stats)


if __name__ == "__main__":
    with open('data.json', 'r') as f:
        data: List[Slot] = json.load(f)

    results = calculate_clinic_availability(data)

    for clinic, stats in results.items():
        print(f"{clinic}: {stats['availability_percent']}% availability "
              f"({stats['available']} of {stats['total']} slots available)")

import json
from typing import List, Dict, Optional, TypedDict


class Slot(TypedDict):
    clinicId: str
    clinicName: str
    startTime: str
    endTime: str
    booked: Optional[bool]
    patientName: Optional[str]


class ClinicStats(TypedDict):
    clinicName: str
    total: int
    booked: int


def calculate_clinic_availability(slots: List[Slot]) -> Dict[str, ClinicStats]:
    clinic_stats: Dict[str, ClinicStats] = {}

    for slot in slots:
        clinic_id = slot["clinicId"]
        clinic_name = slot["clinicName"]

        if clinic_id not in clinic_stats:
            clinic_stats[clinic_id] = {
                "clinicName": clinic_name,
                "total": 0,
                "booked": 0,
            }

        clinic_stats[clinic_id]["total"] += 1
        if slot.get("booked", False):
            clinic_stats[clinic_id]["booked"] += 1

    return clinic_stats


def print_availability(clinic_stats: Dict[str, ClinicStats]) -> None:
    for stats in clinic_stats.values():
        available = stats["total"] - stats["booked"]
        percent = round((available / stats["total"]) * 100) if stats["total"] > 0 else 0
        print(f"{stats['clinicName']}: {percent}% availability "
              f"({available} of {stats['total']} slots available)")


if __name__ == "__main__":
    with open('data.json', 'r') as f:
        data: List[Slot] = json.load(f)

    results = calculate_clinic_availability(data)
    print_availability(results)

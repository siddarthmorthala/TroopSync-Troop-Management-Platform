def passes_advancement_rules(completed_requirements: int, total_requirements: int) -> dict:
    if total_requirements <= 0:
        return {"valid": False, "message": "Total requirements must be positive."}
    if completed_requirements < 0:
        return {"valid": False, "message": "Completed requirements cannot be negative."}
    if completed_requirements > total_requirements:
        return {"valid": False, "message": "Completed requirements cannot exceed total requirements."}
    status = "complete" if completed_requirements == total_requirements else "in_progress"
    return {"valid": True, "message": "Advancement record passes validation.", "status": status}

def service_leaderboard(logs):
    totals = {}
    for log in logs:
        totals[log.member_id] = totals.get(log.member_id, 0) + log.hours
    return sorted(totals.items(), key=lambda x: x[1], reverse=True)

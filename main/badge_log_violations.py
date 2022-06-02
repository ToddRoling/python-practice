def get_badge_log_violations(badge_records: list[list]):
    entries_without_exits = set()
    exits_without_entries = set()
    occupants = set()

    for badge_record in badge_records:
        employee_name = badge_record[0]
        if badge_record[1] == "enter":
            if employee_name in occupants:
                entries_without_exits.add(employee_name)
            else:
                occupants.add(employee_name)
        else:
            if employee_name not in occupants:
                exits_without_entries.add(employee_name)
            else:
                occupants.remove(employee_name)

    for employee_name in occupants:
        entries_without_exits.add(employee_name)

    return entries_without_exits, exits_without_entries

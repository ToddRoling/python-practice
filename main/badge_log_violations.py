def get_badge_log_violations(badge_records):
    no_entry = set()
    no_exit = set()
    occupants = set()

    for badge_record in badge_records:
        name = badge_record[0]
        if badge_record[1] == "enter":
            if name in occupants:
                no_exit.add(name)
            else:
                occupants.add(name)
        else:
            if name not in occupants:
                no_entry.add(name)
            else:
                occupants.remove(name)

    for name in occupants:
        no_exit.add(name)

    return no_exit, no_entry

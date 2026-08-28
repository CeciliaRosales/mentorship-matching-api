def overlap(mentee_items, mentor_items):
    if not mentee_items:
        return 0.0
    mentee_set = {s.lower().strip() for s in mentee_items}
    mentor_set = {t.lower().strip() for t in mentor_items}

    return len(mentee_set & mentor_set) / len(mentee_set)
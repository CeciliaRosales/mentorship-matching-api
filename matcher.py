WEIGHTS = {
    "major" : 35,
    "subjects": 25,
    "skills": 25,
    "interests": 15,
}

def overlap(mentee_items, mentor_items):
    if not mentee_items:
        return 0.0
    mentee_set = {s.lower().strip() for s in mentee_items}
    mentor_set = {t.lower().strip() for t in mentor_items}

    return len(mentee_set & mentor_set) / len(mentee_set)

def score(mentee, mentor):
    total_score = 0.0
    mentee_major = mentee.major.lower().strip()
    mentor_major = mentor.major.lower().strip()
    if mentee_major == mentor_major:
        total_score += WEIGHTS["major"]
    total_score += WEIGHTS["subjects"] * overlap(mentee.subjects, mentor.subjects)
    total_score += WEIGHTS["skills"] * overlap(mentee.skills, mentor.skills)
    total_score += WEIGHTS["interests"] * overlap(mentee.interests, mentor.interests)

    return total_score

def match_all(mentees, mentors):
    remaining_cap = {}
    for mentor in mentors:
        remaining_cap[mentor.id] = mentor.capacity
    results = []
    for mentee in mentees:
        best_match = None
        best_score = -1
        for mentor in mentors:
            if remaining_cap[mentor.id] > 0:
                current_score = score(mentee, mentor)
                if current_score > best_score:
                    best_score = current_score
                    best_match = mentor
        if best_match is not None: #if we found a best mentor
            remaining_cap[best_match.id] -= 1
            results.append({"mentee": mentee.name, "mentor": best_match.name, "score": best_score})
        else:
            results.append({"mentee": mentee.name, "mentor": None, "score": 0})

    return results #write down the pairing


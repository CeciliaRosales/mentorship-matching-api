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

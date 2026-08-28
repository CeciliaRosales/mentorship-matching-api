class Mentee:
    def __init__(self, id, name, major, subjects, skills, interests):
        self.id = id
        self.name = name
        self.major = major
        self.subjects = subjects
        self.skills = skills
        self.interests = interests

class Mentor:
    def __init__(self, id, name, major, subjects, skills, interests, capacity=2):
        self.id = id
        self.name = name
        self.major = major
        self.subjects = subjects
        self.skills = skills
        self.interests = interests
        self.capacity = capacity

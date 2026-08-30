class Mentee:
    def __init__(self, id, name, major, subjects, skills, interests):
        self.id = id
        self.name = name
        self.major = major
        self.subjects = subjects
        self.skills = skills
        self.interests = interests
    def to_dict(self):
        return {"id": self.id, "name": self.name, "major": self.major, "subjects":self.subjects, "skills":self.skills, "interests": self.interests}

class Mentor:
    def __init__(self, id, name, major, subjects, skills, interests, capacity=2):
        self.id = id
        self.name = name
        self.major = major
        self.subjects = subjects
        self.skills = skills
        self.interests = interests
        self.capacity = capacity
    def to_dict(self):
        return {"id": self.id, "name": self.name, "major": self.major, "subjects":self.subjects, "skills":self.skills, "interests": self.interests, "capacity":self.capacity}

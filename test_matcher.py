from matcher import overlap, score, match_all
from models import Mentee, Mentor


#test cases for overlap function
def test_some_common():
    assert overlap({"python", "java", "javascript", "html"}, {"python", "html"}) == 0.5

def test_all_common():
    assert overlap({"gardening", "hiking", "running", "painting"}, {"hiking", "painting", "running", "dancing", "gardening", "reading"}) == 1.0

def test_empty_mentee():
    assert overlap([], {"cycling"}) == 0.0

def test_no_common():
    assert overlap({"swimming"}, {"cycling"}) == 0.0

def test_capitalization():
    assert overlap({"Hiking"}, {"hiking"}) == 1.0

#test cases for score function

def test_score():
    mindy = Mentee("1", "Mindy", "EECS", ["python", "java"], ["3d printing", "robotics"], ["hiking", "reading"])
    maddy = Mentor("2", "Maddy", "EECS", ["python", "html"], ["robotics"], ["hiking", "painting"])
    assert score(mindy, maddy) == 67.5
#same major = 35 points, 1 subject in commmon = 12.5 points, 1 skill in common = 12.5 points, 1 interest in common = 7.5 points, total = 35 + 12.5 + 12.5 + 7.5 = 67.5

#test cases for match_all function
def test_match_all():
    mindy = Mentee("1", "Mindy", "EECS", ["python", "java"], ["3d printing", "robotics"], ["hiking", "reading"])
    sam = Mentee("2", "Sam", "EECS", ["python", "html"], ["robotics"], ["hiking", "painting"])
    maddy = Mentor("3", "Maddy", "EECS", ["python", "html"], ["robotics"], ["hiking", "painting"], capacity=1)
    assert match_all([mindy, sam], [maddy]) == [{"mentee": "Mindy", "mentor": "Maddy", "score": 67.5}, {"mentee": "Sam", "mentor": None, "score": 0}]
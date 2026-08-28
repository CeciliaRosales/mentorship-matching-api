from matcher import overlap

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
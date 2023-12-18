from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("Ga1a2asaray") == "G12sry"
    assert shorten("brighton") == "brghtn"
    assert shorten("shore,a.m") == "shr,.m"
    assert shorten("LAncIng") == "Lncng"

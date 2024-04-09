from twttr import shorten

def test_arguments():
    assert shorten("twitter") == "twttr"
    assert shorten("sora") == "sr"
    assert shorten("facebook") == "fcbk"
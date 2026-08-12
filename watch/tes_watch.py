from watch import parse

def test_None():
    assert parse('<iframe width="560" height="" src="https://www.youtube.com/embed/abcdABCD120"') == None

def test_Long():
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/abcdABCD120" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/abcdABCD120'

def test_Small():
    assert parse('<iframe src="https://www.youtube.com/embed/abcdABCD120"></iframe>') == 'https://youtu.be/abcdABCD120'

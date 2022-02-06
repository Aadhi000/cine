def test_boxoffice_movies_must_return_10_results(ia):
    chart = ia.get_boxoffice_movies()
    assert len(chart) == 10


def test_top50_horrors_must_return_50_results(ia):
    movies = ia.get_top50_movies_by_genres('horror')
    assert len(movies) == 50


def test_top50_action_thriller_tv_must_return_50_results(ia):
    tv = ia.get_top50_tv_by_genres(['action', 'thriller'])
    assert len(tv) == 50

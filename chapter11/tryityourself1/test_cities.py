from city_functions import city_country, modified_city_country


def test_city_country():
    """Does city country function work?"""
    destination = city_country('johannesburg', 'south africa')
    assert destination == 'Johannesburg, South Africa'

def test_modified_city_country():
    """Does modified city country function work?"""
    location = modified_city_country("tokyo", 'japan', 5000000)
    assert location == 'Tokyo, Japan - population 5000000'
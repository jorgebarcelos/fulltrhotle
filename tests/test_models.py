# import sys
# sys.path.append('.')
from src.models import models


def test_motorcycle_info():
    bike = models.Motorcycle('Honda', 'Fury', 'Cruiser', 170)
    assert bike.brand == 'Honda'
    assert bike.name == 'Fury'
    assert bike.model == 'Cruiser'
    assert bike.horsepower == 170

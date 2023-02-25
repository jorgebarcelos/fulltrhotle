# import sys
# from pathlib import Path
# file = Path(__file__).resolve()
# parent, root = file.parent, file.parents[1]
# sys.path.append(str(root))

from models.models import Motorcycle
from typing import List


class MotorcycleController:
    motorcycles = []

    @classmethod
    def save_motorcycle(cls, motorcycle: Motorcycle):
        cls.motorcycles.append(motorcycle)

    @classmethod
    def list_motorcycles(cls)-> List[Motorcycle]:
        return cls.motorcycles


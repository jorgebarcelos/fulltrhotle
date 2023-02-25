from typing import Dict


class Motorcycle:
    def __init__(self, brand: str, name: str, model: str, horsepower: int) -> None:
        self.brand = brand
        self.name = name
        self.model = model
        self.horsepower = horsepower

    def motorcycle_info(self) -> Dict:
        return {
            'brand': self.brand,
            'name': self.name,
            'model': self.model,
            'horsepower': self.horsepower
            }
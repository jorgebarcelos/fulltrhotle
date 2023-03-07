# import sys
# from pathlib import Path
# file = Path(__file__).resolve()
# parent, root = file.parent, file.parents[1]
# sys.path.append(str(root))
from src.controllers.motorcycle import MotorcycleController
from src.models.models import Motorcycle


while True:
    option = int(
        input(
            '''
            [1] Insert motorcycle
            [2] List motorcycles
            [3] Exit
        '''
        )
    )

    if option == 1:
        brand = input('Brand: ')
        name = input('Name: ')
        model = input('Model: ')
        horsepower = input('Horsepower: ')

        bike = Motorcycle(brand=brand, name=name, model=model, horsepower=horsepower)
        MotorcycleController.save_motorcycle(bike)

    elif option == 2:
        for bike in MotorcycleController.list_motorcycles():
            print({'Brand': bike.brand, 'Name': bike.name, 'Model': bike.model, 'Horsepower': bike.horsepower})
    elif option == 3:
        exit()
    else:
        print('Invalid option')

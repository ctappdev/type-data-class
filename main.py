from models.person import Person
from models.product import Product
from models.animal import Animal
import srcipt1
from typing import List
import json


def main():
    prd = Product(1, "Samsung", 100.00)
    print(f"Product {prd}")

    pers = Person("Leon", "Dorfling", 52, "Programmer")
    print(f"Person {pers}")

    anm1 = Animal(animal_breed="Dog", animal_description="Furry, Four Legs", average_size=11)
    print(f"Animal 1 {anm1}")

    anm2_dict = {"animal_breed": "Dog", "animal_description": "Furry, Four Legs", "average_size": 12}
    anm2 = Animal.parse_obj(anm2_dict)
    print(f"Animal 2 {anm2}")

    anm3_json = '{"animal_breed": "Dog", "animal_description": "Furry, Four Legs", "average_size": 310}'
    anm3 = Animal.parse_raw(anm3_json)
    print(f"Animal 3 {anm3}")

    with open("./data.json") as file:
        anm4_json = json.load(file)
        anm4: List[Animal] = [Animal(**item) for item in anm4_json]
        for animal in anm4:
            print(f"Animal 4-0 {animal}")


if __name__ == "__main__":
    main()
else:
    print("Main was run from an import")

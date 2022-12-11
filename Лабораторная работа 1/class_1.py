import doctest


class Animals:
    """
    Documentation for the class
    The class describes the animal model
    """
    def __init__(self, name: str, animal_class: str, weight: (int, float)):
        """
        Creation and preparation for operation of the "Animals" object

        :param name: Name of animals
        :param animal_class: Animal class
        :param weight: Animal weight

        Example:
        >>> animal = Animals("cat", "mammal", 3.5)
        """
        if not isinstance(name, str):
            raise TypeError("Invalid variable type, enter the word")
        self.name_of_animals = name

        if not isinstance(animal_class, str):
            raise TypeError("Invalid variable type, enter the word")
        self.animal_class = animal_class

        if not isinstance(weight, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if weight <= 0:
            raise ValueError("The weight of the animal must be a positive number")
        self.animal_weight = weight

    def pet_animal(self) -> bool:
        """
        A function that checks whether a pet is

        :return: Is it a pet?
        """
        ...

    def animal_size(self) -> bool:
        """
        A function that checks if the animal is big

        :return: Is the animal big?
        """
        ...


if __name__ == "__main__":
    doctest.testmod()


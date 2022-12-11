import doctest


class Chocolate:
    """
    Documentation for the class
    The class describes the chocolate model
    """
    def __init__(self, length: (int, float), width: (int, float)):
        """
        Creation and preparation for operation of the "Chocolate" facility

        :param length: Сhocolate bar length
        :param width: Сhocolate bar width

        Example:
        >>> chocolate = Chocolate(17.5, 7)
        """
        self.chocolate_filling = []

        if not isinstance(length, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if length <= 0:
            raise ValueError("The length of the chocolate bar must be a positive number")
        self.chocolate_length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if not width > 0:
            raise ValueError("The width of the chocolate bar must be a positive number")
        self.chocolate_width = width

    def add_filling(self, filling: str) -> None:
        """
        A function that adds a filling to the chocolate

        :param filling: Filling in chocolate
        """
        ...

    def chocolate_size(self) -> str:
        """
        A function that checks if a sock is black

        :return: What is the size of a chocolate bar ("S", "M" or "L")?
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

import doctest


class Socks:
    """
    Documentation for the class
    The class describes the model of socks
    """
    def __init__(self, colour: str, size: (int, float)):
        """
        Creation and preparation for operation of the "Socks" object

        :param colour: Socks colour
        :param size: Sock size

        Example:
        >>> socks = Socks("black", 6)
        """
        if not isinstance(colour, str):
            raise TypeError("Invalid variable type, enter the word")
        self.socks_colour = colour

        if not isinstance(size, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if size <= 0:
            raise ValueError("The size of the socks must be a positive number")
        self.sock_size = size

    def sock_sizing_grid(self) -> str:
        """
        A function that checks which size grid socks belong to (EU or US)

        :return: What size grid do socks belong to ("EU" or "US")?
        """
        ...

    def black_sock(self) -> bool:
        """
        A function that checks if a sock is black

        :return: Is the sock black?
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

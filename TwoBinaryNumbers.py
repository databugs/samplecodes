class TwoBinaryNumbers:
    """
    """
    def __init__(self, binary_1: str, binary_2: str) -> None:
        self.binary_1: str = binary_1
        self.binary_2: str = binary_2
    
    @staticmethod
    def is_binary(binary_number: str) -> str:
        try:
            int(binary_number, 2)
            return int(binary_number,2)
        except ValueError:
            error_message = f'{binary_number} is not a binary number!'
            raise ValueError(error_message)      

    def sum(self) -> str:
        self.result = bin(self.is_binary(self.binary_1) + self.is_binary(self.binary_2))
        return str(self.result[2:])
    
    def multiply(self) -> str:
        self.result = bin(self.is_binary(self.binary_1) * self.is_binary(self.binary_2))
        return str(self.result[2:])
    
    def divide(self) -> str:
        self.result = bin(int(self.is_binary(self.binary_1) // self.is_binary(self.binary_2)))
        return str(self.result[2:])
    
    def subtract(self) -> str:
        self.result = bin(self.is_binary(self.binary_1) - self.is_binary(self.binary_2))
        return str(self.result[2:])

if __name__ == '__main__':
    input_1 = input('Enter first binary number: ')
    input_2 = input('Enter another binary number: ')
    binary = TwoBinaryNumbers(input_1, input_2)
    print(binary.sum())
    print(binary.multiply())
    print(binary.divide())
    print(binary.subtract())

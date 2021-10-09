from typing import TypeVar, Generic

Numeric = TypeVar('Numeric', int, float)

class Calculator(Generic[Numeric]):
    """
    Class representing Calculator

    ...
    
    Examples:
        
        Initiate object
        >>> cal = Calculator()
        0
        >>> cal = Calculator(12.5)
        12.5
        
        Perform operations
        >>> cal.add(0.5)
        13.0
        >>> cal.multiply(2)
        26.0
        >>> cal.subtract(18)
        8.0
        >>> cal.root(3)
        2.0

    """
    memory = 0
    
    @classmethod
    def reset(cls, memory_number: Numeric=0) -> Numeric:
        """
        reset the memory to memory number value
        """
        cls.memory = memory_number
        print(cls.memory)
    
    def __init__(self, number: Numeric=0) -> None:
        """
        construct attribute for the Calculator object
        """
        self.number = number
        self.reset(number)
    
    def add(self, current_number: Numeric) -> Numeric:
        """
        add provided number to memory value 
        """
        addition = self.memory + current_number
        return self.reset(addition)

    def subtract(self, current_number: Numeric) -> Numeric:
        """
        subtract provided number from memory value 
        """
        subtraction = self.memory - current_number
        return self.reset(subtraction)
    
    def multiply(self, current_number: Numeric) -> Numeric:
        """
        multiply memory value by provided number
        """
        multiplication = self.memory * current_number
        return self.reset(multiplication)

    def divide(self, current_number: Numeric) -> Numeric:
        """
        divide memory value by provided number 
        """
        division = self.memory / current_number
        return self.reset(division)
     
    def root(self, nth_root: Numeric) -> Numeric:
        """
        take specified nth root from memory value
        convert the output to match input format (int or float)
        """
        if nth_root < 0:
            raise ValueError('Input should be a positive number')
            
        if isinstance(self.memory, int):
            root = round(pow(self.memory, 1/nth_root))
            
        if isinstance(self.memory, float):
            root = pow(self.memory, 1/nth_root)

        return self.reset(root)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

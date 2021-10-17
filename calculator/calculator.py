from typing import Union

Numeric = Union[int, float, complex]

class Calculator():
    """
    Class representing Calculator

    ...
    
    Examples:
        
        Initiate object
        >>> cal = Calculator(12.5)
        >>> cal.display
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
        >>> cal.divide(7)
        0.2857142857142857
        >>> cal.reset()
        0

    """
    def __init__(self, memory: Numeric=0) -> None:
        """Construct attribute for the Calculator object"""
        self.check_type(memory)
        self.__memory = memory
        
    
    def check_type(self, current_number: Numeric) -> None:            
        """"Check if the input type is correct"""
        if not isinstance(current_number, (int, float, complex)): 
            raise TypeError('The calculator is designed to work with single '
                            'number input. Please provide valid number')
    
    def reset(self, memory_number: Numeric=0) -> Numeric:
        """Reset the memory to memory number value"""
        self.check_type(memory_number)
        self.__memory = memory_number
        return self.__memory
    
    def add(self, current_number: Numeric) -> Numeric:
        """Add provided number to memory value"""
        self.check_type(current_number)
        self.__memory = self.__memory + current_number
        return self.__memory

    def subtract(self, current_number: Numeric) -> Numeric:
        """Subtract provided number from memory value"""
        self.check_type(current_number)
        self.__memory= self.__memory - current_number
        return self.__memory
    
    def multiply(self, current_number: Numeric) -> Numeric:
        """Multiply memory value by provided number"""
        self.check_type(current_number)
        self.__memory = self.__memory * current_number
        return self.__memory

    def divide(self, current_number: Numeric) -> Numeric:
        """Divide memory value by provided number
        Handle division by 0 error.
        """
        self.check_type(current_number)
        
        try:
            self.__memory = self.__memory / current_number
            return self.__memory
        except:
            print(f'Division by {current_number} not possible')
    
    def root(self, nth_root: Numeric) -> Numeric:   
        """ Take specified nth root from memory value
        Handle inacceptable root error. 
        """
        self.check_type(nth_root)
        
        try:
            self.__memory = pow(self.__memory, 1/nth_root)
            return self.__memory
        except:
            print(f'{nth_root} root of number {self.__memory} is not possible')
            
    @property
    def get_memory(self) -> Numeric:  
        return self.__memory
    
    @property
    def display(self) -> None:
        print(self.__memory)
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()

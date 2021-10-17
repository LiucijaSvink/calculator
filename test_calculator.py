import pytest
from calculator import Calculator

# Test input type incompatibility
def test_calculator_empty_input():
    with pytest.raises(TypeError):
        Calculator().add()

def test_calculator_string_input():
    with pytest.raises(TypeError):
        Calculator(4).add('str')    

def test_calculator_list_input():        
    with pytest.raises(TypeError):
        Calculator([3, 6]).subtract(-56)

def test_calculator_tuple_no_input():          
    with pytest.raises(TypeError):
        Calculator((6, 8)).multiply([])
        

# Test correctness of calculations
cal = Calculator()  
def test_calculator_add_function():
    cal.add(-10)
    assert cal.get_memory == -10        
    cal.add(-440)
    assert cal.get_memory == -450

def test_calculator_subtract_function():
    cal.subtract(550)
    assert cal.get_memory == -1000 

def test_calculator_multiply():
    cal.multiply(-1)
    assert cal.get_memory == 1000

def test_calculator_root():
    cal.root(3)
    assert cal.get_memory == 9.999999999999998

def test_calculator_divide():
    cal.divide(2.00)
    assert cal.get_memory == 4.999999999999999

def test_calculator_reset():
    cal.reset(4+6j)
    assert cal.get_memory == 4+6j
    cal.reset()
    assert cal.get_memory == 0
    
def test_calculator_nonexistent_operations():
    cal.divide(0)
    assert "Division of 0 not possible"
    cal.root(0)
    assert "0 root of number {cal.get_memory} is not possible"


    
    
    

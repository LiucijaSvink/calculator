import pytest
from calculator import Calculator

# test input type incompatibility
def test_calculator_types():
    
    with pytest.raises(TypeError):
        Calculator(4).add('str')    
        
    with pytest.raises(TypeError):
        Calculator([3, 6]).subtract(-56)
        
    with pytest.raises(TypeError):
        Calculator([-5, -67]).subtract([])
        
    with pytest.raises(TypeError):
        Calculator([-5, -67]).divide(5)    

# test correctness of calculations
def test_calculator_result():
    
    cal = Calculator(-10)   
    assert cal.number == -10
    assert isinstance(cal.number, int)
        
    cal.add(-440)
    assert cal.memory == -450
    assert isinstance(cal.memory, int)
    
    cal.subtract(550)
    assert cal.memory == -1000 
    assert isinstance(cal.memory, int)

    cal.multiply(-1)
    assert cal.memory == 1000 
    assert isinstance(cal.memory, int)

    cal.reset(4096)
    assert cal.memory == 4096 
    assert isinstance(cal.memory, int)
    
    cal.root(3)
    assert cal.memory == 16 
    assert isinstance(cal.memory, int)
    
    cal.divide(2.00)
    assert cal.memory == 8.00 
    assert isinstance(cal.memory, float)
    

    
    
    

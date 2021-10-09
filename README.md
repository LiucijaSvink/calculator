# Calculator

Calculator is a tool for performing mathematical operations. 

## Installation


## Usage

The calculator provides the following functions:
- add -> summation numbers
- subtract -> subtraction of numbers  
- mutiply -> multiplication by provided number 
- divide -> division by provided number
- root -> taking a nth root of the number, nth root is provided as an input

The calculator also has an internal memory. The output from the previous operation is stored and updated when the next operations is perfromed. It has two features:
- memory -> inspect the current memory value
- reset -> reset the memory to 0 or other value

# Examples

The calculator packages has one module, also named calculator. Once installed, the conventional module import procedure can be used to import the package.

```python
import calculator
from calculator import calculator

# initialize calculator
calculator = Calculator()

# perform operations
calculator.add(3)
calculator.mutiply(4)
calculator.divide(2)
calculator.subtract(2.5)
calculator.memory
calculator.reset(0)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

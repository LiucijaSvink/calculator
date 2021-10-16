# Calculator

Calculator is a tool for performing mathematical operations. 

## Installation

To install the calculator package:
1. Use the Code button in the Github repository to download the package to your local computer. Using Python, navigate to the calculator folder to use the package.
2. Use package manager to install calculator.
```python
pip install git+https://github.com/LiucijaSvink/calculator
```
3. Use pip command in Google Colab's environment to install calculator.
```python
!pip install git+https://github.com/LiucijaSvink/calculator.git
```
## Usage

The calculator provides the following functions:
- add -> adding a number
- subtract -> subtracting a number  
- multiply -> multiplication by provided number 
- divide -> division by provided number
- root -> taking a nth root of the number, nth root is provided as an input

The calculator also has an internal memory. The output of the performed operation is stored in it. When the next operations is performed, the memory is updated with the newest output. It has two features:
- display -> show the current memory value
- reset -> reset the memory to 0 or other value
- get_memory -> returns the current memory value  

# Examples

The calculator packages has one module, also named calculator. Once installed, the conventional module import procedure can be used to import the package.

```python
import calculator
from calculator import Calculator
```

To initialize the calculator, call class Calculator.

```python
calculator = Calculator()
```

The default value of the calculator will be 0. You can also specify a number in the parentheses when starting calculator. It will be taken as a first number to perform subsequent operations on.

```python
second_calculator = Calculator(6)
```

To perform an operation, call the corresponding function name and include a real number for operations in the parentheses.

```python
calculator.add(3)
3
```

Calculator also has an internal memory. This means that the result of previous operation will be taken as first value for the next operation. For example:
 
```python
calculator.mutiply(4)
12
```

In this case, the outcome 3 is multiplied by 4. Hence, the result is 12. To inspect the current value of the memory, enter:

```python
calculator.display
12
```

To reset memory to a specific value, use a command reset. Default reset value is 0.

```python
calculator.reset(98)
98
calculator.reset()
0
```

The calculator input can be one number: integer, float or complex number.

```python
calculator.add(8192)
8192
calculator.divide(2.0)
4096.0
calculator.root(-3)
0.06250000000000001
```
Other types of input will raise errors.

To get a memory value which can be assigned to a variable, use:
```python
result = calculator.get_memory
```

## Dockerfile
The added docker file allows to build a Docker image. Dockerfile is a script, composed of various commands (instructions) and arguments listed successively to automatically perform actions on a base image.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

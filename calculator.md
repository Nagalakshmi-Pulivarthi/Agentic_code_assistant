# Calculator Module

This module provides basic arithmetic operations such as addition, subtraction, multiplication, and division. Each function takes two numerical arguments and returns the result of the operation.

## Functions

### add(a, b)

Returns the sum of two numbers.

- **Parameters**:
  - `a`: First number (float or int)
  - `b`: Second number (float or int)
- **Returns**: Sum of `a` and `b` (float or int)

#### Example:
```python
result = add(5, 3)  # result is 8
```

### subtract(a, b)

Returns the difference between two numbers.

- **Parameters**:
  - `a`: First number (float or int)
  - `b`: Second number (float or int)
- **Returns**: Difference of `a` and `b` (float or int)

#### Example:
```python
result = subtract(10, 4)  # result is 6
```

### multiply(a, b)

Returns the product of two numbers.

- **Parameters**:
  - `a`: First number (float or int)
  - `b`: Second number (float or int)
- **Returns**: Product of `a` and `b` (float or int)

#### Example:
```python
result = multiply(3, 7)  # result is 21
```

### divide(a, b)

Returns the quotient of two numbers.

- **Parameters**:
  - `a`: First number (float or int)
  - `b`: Second number (float or int)
- **Returns**: Quotient of `a` and `b` (float)
- **Raises**: `ZeroDivisionError` if `b` is zero.

#### Example:
```python
result = divide(10, 2)  # result is 5.0
```

### Error Handling
When attempting to divide by zero, a `ZeroDivisionError` will be raised.

```python
result = divide(5, 0)  # Raises ZeroDivisionError: Cannot divide by zero
```
import math

def calculate_sine(radian):
    # Ensure that 'radian' is a number (int or float)
    assert isinstance(radian, (int, float)), "Input must be an integer or float"
    
    # Perform the sine calculation
    return math.sin(radian)

# Example usage
try:
    print(calculate_sine(math.pi / 2))  # Should print 1.0
    print(calculate_sine(3.14))         # Should print a value close to 0
    print(calculate_sine("90 degrees")) # Should raise an AssertionError
except AssertionError as e:
    print(f"Assertion error: {e}")

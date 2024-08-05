class MyClass:
    def __init__(self, value):
        self.value = value

def get_value(c):
    return c.value

# Example usage:
obj = MyClass(42)
print(get_value(obj))  # Output: 42

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload + operator
    def __add__(self, other):
        real = self.real + other.real           #Addition method
        imag = self.imag + other.imag
        return Complex(real, imag)

    # Overload * operator
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag              #multiplication method
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    # Display complex number
    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Example usage
c1 = Complex(2, 3)
c2 = Complex(4, 5)

add_result = c1 + c2
mul_result = c1 * c2

print("Addition:", add_result)
print("Multiplication:", mul_result)
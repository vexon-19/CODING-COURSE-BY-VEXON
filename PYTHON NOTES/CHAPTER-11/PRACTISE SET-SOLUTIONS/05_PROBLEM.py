class Vector:
    def __init__(self, components):
        self.components = components

    # Overloading + operator for vector addition
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")

        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] + other.components[i])

        return Vector(result)

    # Overloading * operator for dot product
    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")

        dot_product = 0
        for i in range(len(self.components)):
            dot_product += self.components[i] * other.components[i]

        return dot_product

    # String representation
    def __str__(self):
        return str(self.components)


# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Vector addition
print("Sum =", v1 + v2)

# Dot product
print("Dot Product =", v1 * v2)
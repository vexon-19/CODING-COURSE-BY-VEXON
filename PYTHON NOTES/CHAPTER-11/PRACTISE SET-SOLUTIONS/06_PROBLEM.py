class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    # String method to print vector
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


# Example usage
v = Vector(7, 8, 10)

print(v)
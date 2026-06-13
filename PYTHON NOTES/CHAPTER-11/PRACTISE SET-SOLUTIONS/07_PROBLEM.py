class Vector:
    def __init__(self, components):
        self.components = components

    # Overloading len() method
    def __len__(self):
        return len(self.components)

    # String representation
    def __str__(self):
        symbols = ['i', 'j', 'k']
        result = ""

        for i in range(len(self.components)):
            result += f"{self.components[i]}{symbols[i]}"

            if i != len(self.components) - 1:
                result += " + "

        return result


# Example usage
v = Vector([7, 8, 10])

print("Vector =", v)
print("Dimension =", len(v))
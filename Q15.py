from abc import ABC, abstractmethod
import math

class SpatialEntity(ABC):
    """Abstract geometric framework blueprint."""
    @abstractmethod
    def size(self):
        """Mandatory contract for all subclasses."""
        pass

class Circle(SpatialEntity):
    def __init__(self, radius):
        self.radius = radius

    def size(self):
        return math.pi * (self.radius ** 2)

    # Operator Overloading
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.size():.2f})"

class Vector(SpatialEntity):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def size(self):
        return math.hypot(self.x, self.y) # Magnitude

    # Operator Overloading
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.size() == other.size()

    def __lt__(self, other):
        return self.size() < other.size()

    def __str__(self):
        return f"Vector({self.x}, {self.y}, magnitude={self.size():.2f})"

# === Execution ===
if __name__ == "__main__":
    c1, c2 = Circle(5), Circle(3)
    v1, v2 = Vector(3, 4), Vector(1, 2)

    print("--- Circle Operations ---")
    print(f"c1: {c1} | c2: {c2}")
    print(f"c1 + c2  => {c1 + c2}")
    print(f"c1 == c2 => {c1 == c2}")
    print(f"c2 < c1  => {c2 < c1}")

    print("\n--- Vector Operations ---")
    print(f"v1: {v1} | v2: {v2}")
    print(f"v1 + v2  => {v1 + v2}")
    print(f"v1 == v2 => {v1 == v2}")
    print(f"v2 < v1  => {v2 < v1}")
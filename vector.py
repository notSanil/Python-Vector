from math import atan2, hypot, cos, sin


class Vector2D:
    def __init__(self, x=1.0, y=0.0):
        self._vec = complex(x, y)

    def __call__(self):
        """Returns the x and y in a list

        :returns [x, y]"""
        return [self.x, self.y]

    @property
    def x(self):
        return self._vec.real

    @x.setter
    def x(self, x):
        self._vec = complex(x, self.y)

    @property
    def y(self):
        return self._vec.imag

    @y.setter
    def y(self, y):
        self._vec = complex(self.x, y)

    @property
    def angle(self):
        return atan2(self.y, self.x)

    @angle.setter
    def angle(self, angle):
        leng = self.length
        self.x = leng * cos(angle)
        self.y = leng * sin(angle)

    @property
    def length(self):
        return hypot(self.x, self.y)

    @length.setter
    def length(self, leng):
        ang = self.angle
        self.x = leng*cos(ang)
        self.y = leng*sin(ang)

    def normalise(self):
        """Sets the length of the Vector2D to unit without changing angle

        :returns None"""
        self.length = 1

    def add_to(self, vec):
        """Add another Vector2D to this Vector2D

        :returns None"""
        self.x += vec.x
        self.y += vec.y

    def subtract_from(self, vec):
        """Subtracts another Vector2D from this one

        :returns None"""
        self.x -= vec.x
        self.y -= vec.y

    def multiply_by(self, scalar):
        """Multiplies a scalar to this Vector2D

        :returns None"""
        self.x *= scalar
        self.y *= scalar

    def divide_by(self, scalar):
        """Divides this Vector2D by a scalar

        :returns None"""
        self.x /= scalar
        self.y /= scalar

    def dot(self, vec):
        """Dots this Vector2D by another Vector2D and returns the result

        :returns Float"""
        return hypot(self.x*vec.x, self.y*vec.y)

    def subtract(self, vec):
        """Returns a new vetor which is the difference of the two

        :returns Vector"""
        return Vector2D(self.x - vec.x, self.y - vec.y)

    def add(self, vec):
        """Returns a new Vector2D which is the sum of the two

        :returns Vector"""
        return Vector2D(self.x + vec.x, self.y + vec.y)

    def divide(self, scalar):
        """Returns a new Vector2D which is the quotient of this one

        :returns Vector"""
        return Vector2D(self.x / scalar, self.y / scalar)

    def multiply(self, scalar):
        """Returns a new Vector2D which is the product of this one

        :returns Vector"""
        return Vector2D(self.x * scalar, self.y * scalar)

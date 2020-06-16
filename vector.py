'''vector.py: Implementation of 2D vectors'''

__author__ = 'Sanil Gupta'


from math import atan2, hypot, cos, sin


class Vector2D:
    def __init__(self, x=1.0, y=0.0):
        """
        Initializes the vector object, is called as soon as the object is created
        :param x: The x coordinate of the head of the vector(default = 1.0)(Float or int)
        :param y: The y coordinate of the head of the vector(default = 0.0)(Float or int)
        """
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self._vec = complex(x, y)
        else:
            raise TypeError("Expected int or float got {}, {} instead".format(type(x), type(y)))

    def __call__(self):
        """Returns the x and y in a list

        :returns [x, y]"""
        return [self.x, self.y]

    def __add__(self, other):
        """
        Allows for two vectors to be added via the plus symbol
        :param other: The vector to be added to this one(Vector2D)
        :return: The sum of two vectors (Vector2D)
        """
        return self.add(other)

    def __sub__(self, other):
        """
        Allows for subtraction via the minus operator
        :param other: The second vector to be subtracted from this one(Vector2D)
        :return: The difference of the two vectors (Vector2D)
        """
        return self.subtract(other)

    def __mul__(self, other):
        """
        Allows the usage of the multiplication operator
        Dots the two vectors if vector is provided, otherwise multiplies this vector by the scalar given
        :param other: Scalar or Vector2D
        :return: This vector dotted with the other vector, or this vector multiplied by the scalar(Int or float)
        """
        if type(other) == type(self):
            return self.dot(other)
        elif isinstance(other, (int, float)):
            return self.multiply(other)

    def __truediv__(self, other):
        """
        Allows for the usage of division operator
        :param other: Scalar
        :return: This vector divided by the scalar(Vector2D)
        """
        return self.divide(other)

    def __rmul__(self, other):
        """
        Allows for the vector to be put on the right hand side of the multiplication operator
        :param other: Scalar or Vector2D
        :return: This vector dotted with the other vector, or this vector multiplied by the scalar(Int or float)
        """
        return self.__mul__(other)

    @property
    def x(self):
        """
        Getter for the x coordinate for the head of the vector
        :return: X coordinate of the head of the vector(float)
        """
        return self._vec.real

    @x.setter
    def x(self, x):
        """
        Setter for the x coordinate of the head of vector
        :param x: Float or int
        :return: None
        """
        if isinstance(x, (int, float)):
            self._vec = complex(x, self.y)
        else:
            raise TypeError("Expected an int or float but got {} instead".format(type(x)))

    @property
    def y(self):
        """
        Getter for the y coordinate of the head of the vector
        :return: Y coordinate of the head of the vector(float)
        """
        return self._vec.imag

    @y.setter
    def y(self, y):
        """
        Setter for the y coordinate of the head of the vector
        :param y: Float or int
        :return: None
        """
        if isinstance(y, (int, float)):
            self._vec = complex(self.x, y)
        else:
            raise TypeError("Expected an int or float but got {} instead".format(type(y)))

    @property
    def angle(self):
        """
        Getter for the angle of the vector
        :return: Angle of the vector(Float, radian)
        """
        return atan2(self.y, self.x)

    @angle.setter
    def angle(self, angle):
        """
        Setter for the angle of the vector
        :param angle: New angle of the vector(Radian)
        :return: None
        """
        if isinstance(angle, (int, float)):
            leng = self.length
            self.x = leng * cos(angle)
            self.y = leng * sin(angle)
        else:
            raise TypeError("Expected an int or float but got {} instead".format(type(angle)))

    @property
    def length(self):
        """
        Getter for the length of the vector
        :return: Float
        """
        return hypot(self.x, self.y)

    @length.setter
    def length(self, leng):
        """
        Setter for the length of the vector
        :param leng: The new length of the vector
        :return: None
        """
        if isinstance(leng, (int, float)):
            ang = self.angle
            self.x = leng*cos(ang)
            self.y = leng*sin(ang)
        else:
            raise TypeError("Expected an int or float but got {} instead".format(type(leng)))

    def normalise(self):
        """Sets the length of the Vector2D to unit without changing angle

        :returns None"""
        self.length = 1

    def add_to(self, vec):
        """Add another Vector2D to this Vector2D

        :returns None"""
        if type(vec) == type(self):
            self.x += vec.x
            self.y += vec.y
        else:
            raise TypeError("Expected a Vector2D but got {} instead".format(type(vec)))

    def subtract_from(self, vec):
        """Subtracts another Vector2D from this one

        :returns None"""
        if type(vec) == type(self):
            self.x -= vec.x
            self.y -= vec.y
        else:
            raise TypeError("Expected a Vector2D but got {} instead".format(type(vec)))

    def multiply_by(self, scalar):
        """Multiplies a scalar to this Vector2D

        :returns None"""
        if isinstance(scalar, (int, float)):
            self.y *= scalar
            self.x *= scalar
        else:
            raise TypeError("Expected a float or int but got {} instead".format(type(scalar)))

    def divide_by(self, scalar):
        """Divides this Vector2D by a scalar

        :returns None"""
        if isinstance(scalar, (int, float)):
            self.x /= scalar
            self.y /= scalar
        else:
            raise TypeError("Expected a float or int but got {} instead".format(type(scalar)))

    def dot(self, vec):
        """Dots this Vector2D by another Vector2D and returns the result

        :returns Float"""
        if type(vec) == type(self):
            return hypot(self.x*vec.x, self.y*vec.y)
        else:
            raise TypeError("Expected a Vector2D but got {} instead".format(type(vec)))

    def subtract(self, vec):
        """Returns a new vetor which is the difference of the two

        :returns Vector"""
        if type(vec) == type(self):
            return Vector2D(self.x - vec.x, self.y - vec.y)
        else:
            raise TypeError("Expected a Vector2D but got {} instead".format(type(vec)))

    def add(self, vec):
        """Returns a new Vector2D which is the sum of the two

        :returns Vector"""
        if type(vec) == type(self):
            return Vector2D(self.x + vec.x, self.y + vec.y)
        else:
            raise TypeError("Expected a Vector2D but got {} instead".format(type(vec)))

    def divide(self, scalar):
        """Returns a new Vector2D which is the quotient of this one

        :returns Vector"""
        if isinstance(scalar, (int, float)):
             return Vector2D(self.x / scalar, self.y / scalar)
        else:
            raise TypeError("Expected an int or float but got {} instead".format(type(scalar)))

    def multiply(self, scalar):
        """Returns a new Vector2D which is the product of this one

        :returns Vector"""
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Expected an int or float but got {} instead".format(type(scalar)))

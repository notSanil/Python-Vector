# Vector
Implementation of vectors in python.

This is an implementation of 2D vectors in python. It has no dependencies except the math module which is included in python natively.

# Usage
Simply copy the vector.py file into your project and import `Vector2D` from it.

# Examples
## Creating a new vector
` vec1 = Vector2D(10, 5) #Creates a new vector with its head at (10, 5) `

`vec1 = Vector2D() #Creates a new vector with its head at (1, 0) `
## Retrieving different values of a vector
` head = vec1() # Returns the head of the vector in a tuple(here, (10, 5))`

`x = vec1.x #Returns the x coordinate of the head of the vector(here, 10)`

`y = vec1.x #Returns the y coordinate of the head of the vector(here, 5)`

`angle = vec1.angle #Return the angle of the vector in the anti-clockwise direction with respect to the positive x axis`

`length = vec1.length #Returns the length of the vector, effectively, the distance of the head from the origin`

## Setting different values of a vector
`vec1.x = 15 #Sets the x coordinate of the head to 15`

`vec1.y = 10 #Sets the y coordinate of the head to 10`

`vec1.length = 40 #Sets the length of a vector to 40 without rotating it`

`vec1.angle = 3.14 #Sets the angle of the vector to 3.14 without changing its length`

## Altering the values of a vector
`vec1.x += 3 # Adds 3 to the x coordinate of the head of the vector`

`vec1.y += 3 # Adds 3 to the y coordinate of the head of the vector`

`vec1.length += 1 # Increases the length of the vector by 1`

`vec1.angle += 3.14 #Increases the angle of the vector by 3.14 radian, same as rotating it by 3.14 radian anticlockwise`

## Binary operations on vectors
`vec1 += vec2 # Adds the second vector to the first one, works for subtraction as well`

`vec3 = vec1 - vec2 # Subtracts the two vectors and returns a new vector, works for addition as well`

`vec2 *= 5.7 # Multiplies the each component of a vector by 5.7, same as multiplying the length by 5.7`

`num = vec2 * vec3 # Dots the two vectors and returns a scalar`

`vec3 /= 10 # Divides each component of the vector by 10, same as dividing the length by 10`

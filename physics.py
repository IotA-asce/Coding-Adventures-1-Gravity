import math
import pmath




# Representation of 2D vectors and points.
class Vector2:
    
    # Constructs a new vector with given x, y components.
    def __init__(self, x, y):

        # X component of the vector
        self.x = float(x)
        # Y component of the vector
        self.y = float(y)
    
    # Set x and y components of an existing Vector2.
    def Set(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Linearly interpolates between two vectors.
    def Lerp(self, other, t):
        t = pmath.clamp01(t)
        return Vector2(
            self.x + (other.x - self.x) * t, 
            self.y + (other.y - self.y) * t)

    # Linearly interpolates between two vectors without clamping the interpolant
    def LerpUnclamped(self, other, t):
        return Vector2(
            self.x + (other.x - self.x) * t, 
            self.y + (other.y - self.y) * t)

    # Moves a point /current/ towards /target/
    def MoveTowards(current, target, maxDistanceDelta):
        
        # avoid vector ops because current scripting backends are terrible at inlining
        toVector_x = target.x - current.x
        toVector_y = target.y - current.y

        sqDist = (toVector_x * toVector_x) + (toVector_y * toVector_y)

        if sqDist == 0 or (maxDistanceDelta >= 0 and sqDist <= (maxDistanceDelta * maxDistanceDelta)):
            return target

        dist = float(math.sqrt(sqDist))

        return Vector2(
            current.x + (toVector_x / dist * maxDistanceDelta),
            current.y + (toVector_y / dist * maxDistanceDelta),
        )

    # Multiplies two vectors component-wise.
    def Scale(self, scale):
        self.x *= scale.x
        self.y *= scale.y

    # Make this vector have a ::ref::magnitude of 1
    def Normalize(self):
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag

    # Returns the length of this vector
    def magnitude(self):
        return math.sqrt((math.pow(self.x, 2) + math.pow(self.y, 2)))

    # Returns the squared length of this vector
    def sqrMagnitude(self):
        return (self.x * self.x) + (self.y * self.y)
    
    # Dot product of two vectors.
    def Dot(self, lhs, rhs):
        return (lhs.x * rhs.x) + (lhs.y + rhs.y)

    def Dot(self, other):
        return (self.x * other.x) + (self.y * other.y)
    
    # 
    def Reflect(self, inDirection, inNormal):
        factor = -2.0 * self.Dot(inNormal, inDirection)
        return Vector2(factor * inNormal.x + inDirection.x, factor * inNormal.y + inDirection.y)

    def Perpendicular(self, inDirection):
        Vector2(-inDirection.y, inDirection.x)

    # Returns the angle in degrees between /from/ and /to/.
    def Angle(self, _from, _to):
        denominator = float(math.sqrt(_from.sqrMagnitude() * _to.sqrMagnitude()))
        if denominator == 0:
            return 0
        
        dot = pmath.clamp(self.Dot(_from, _to) / denominator, -1.0, 1.0)
        return float(math.degrees(math.acos(dot)))

    # Returns the signed angle in degrees between /from/ and /to/.
    # Always returns the smallest possible angle
    def SignedAngle(self, _from, _to):
        unsigned_angle = self.Angle(_from, _to)
        sign = pmath.Sign(_from.x * _to.y - _from.y * _to.x)
        return unsigned_angle * sign
    
    # returns the distance between /a/ and /b/.
    def Distance(a, b):
        diff_x = a.x - b.x
        diff_y = a.y - b.y

        return float(math.sqrt(diff_x * diff_x + diff_y * diff_y))
    
    # Returns a copy of /vector/ with its magnitude clamped to /maxLength/.
    def ClampMagnitude(self, vector, maxLenght):
        sqrMagnitude = vector.sqrMagnitude()
        if sqrMagnitude > maxLenght * maxLenght:
            mag = float(math.sqrt(sqrMagnitude))

            """
            These intermediate variables force the intermediate result to be of float
            precision. Without thism the intermediate result can be of higher precision,
            which changes behavior.
            """
            normalized_x = vector.x / mag
            normalized_y = vector.y / mag
            return Vector2(normalized_x * maxLenght, normalized_y * maxLenght)
        
        return vector


    # vector addition
    def __add__(self, other):               
        return Vector2(self.x + other.x, self.y + other.y)

    # vector substraction
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __str__(self):
        return str(self.x) + "   " + str(self.y) + "    "

    



    # cross product
    def cross(self, other):
        """
        :param other: Vector2 component
        :return: cross product of self X other 
        [TODO] implement
        """
        pass

   
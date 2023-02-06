"""
A physics library
"""


import pmath

K_EPSILON = 0.00001
K_EPSILON_NORMAL_SQRT = 1E-15

class Vector2:
    """
        Representation of 2D vectors and points.
    """

    def __init__(self, _x, _y):
        """
        Constructs _a new vector with given _x, _y components.
        """

        # X component of the vector
        self._x = float(_x)
        # Y component of the vector
        self._y = float(_y)

    def get_x(self):
        """
        getter funtion
        """

        return self._x

    def get_y(self):
        """
        getter function
        """

        return self._y

    def set(self, _x, _y):

        """
        set _x and _y components of an existing Vector2.
        """

        self._x = float(_x)
        self._y = float(_y)

    def lerp(self, other, _t):
        """
        Linearly interpolates between two vectors.
        """

        _t = pmath.clamp01(_t)
        return Vector2(
            self._x + (other.get_x() - self._x) * _t,
            self._y + (other.get_y() - self._y) * _t)

    def lerp_unclamped(self, other, _t):
        """
        Linearly interpolates between two vectors without clamping the interpolant
        """

        return Vector2(
            self._x + (other.get_x() - self._x) * _t,
            self._y + (other.get_y() - self._y) * _t)

    def move_towards(self, current, target, max_distance_delta):
        """
        Moves _a point /current/ towards /target/
        """

        # avoid vector ops because current scripting backends are terrible at inlining
        to_vector_x = target.get_x() - current.get_x()
        to_vector_y = target.get_y() - current.get_y()

        sq_dist = (to_vector_x * to_vector_x) + (to_vector_y * to_vector_y)

        if sq_dist == 0 or (
            max_distance_delta >= 0 and sq_dist <= (max_distance_delta * max_distance_delta)):
            return target

        dist = float(pmath.sqrt(sq_dist))

        return Vector2(
            current.get_x() + (to_vector_x / dist * max_distance_delta),
            current.get_y() + (to_vector_y / dist * max_distance_delta),
        )

    def scale(self, scale):
        """
        Multiplies two vectors component-wise.
        """

        self._x *= scale.get_x()
        self._y *= scale.get_y()

    def normalize(self):
        """
        Make this vector have _a ::ref::magnitude of 1
        """

        mag = self.magnitude()

        if mag > K_EPSILON:
            self._x /= mag
            self._y /= mag
        else:
            self._x = 0
            self._y = 0

    def magnitude(self):
        """
        Returns the length of this vector
        """

        return pmath.sqrt((pmath.__pow__(self._x, 2) + pmath.__pow__(self._y, 2)))


    def sqr_magnitude(self):
        """
        Returns the squared length of this vector
        """

        return (self._x * self._x) + (self._y * self._y)

    def dot(self, lhs, rhs):
        """
        dot product of two vectors.
        """
        return (lhs.get_x() * rhs.get_x()) + (lhs.get_y() + rhs.get_y())

    def _dot(self, other):
        return (self._x * other.get_x()) + (self._y * other.get_y())


    def reflect(self, in_direction, in_normal):
        """
        undocumented
        """
        factor = -2.0 * self.dot(in_normal, in_direction)
        return Vector2(
            factor * in_normal.get_x() + in_direction.get_x(),
            factor * in_normal.get_y() + in_direction.get_y()
            )

    def perpendicular(self, in_direction):
        """
        undocumented
        """
        Vector2(-in_direction.get_y(), in_direction.get_x())

    def angle(self, _from, _to):
        """
        Returns the angle in degrees between /from/ and /to/.
        """

        denominator = float(pmath.sqrt(_from.sqr_magnitude() * _to.sqr_magnitude()))
        if denominator < K_EPSILON_NORMAL_SQRT:
            return 0

        dot = pmath.clamp(self.dot(_from, _to) / denominator, -1.0, 1.0)
        return float(pmath.degrees(pmath.acos(dot)))

    def signed_angle(self, _from, _to):
        """
        Returns the signed angle in degrees between /from/ and /to/.
        Always returns the smallest possible angle
        """

        unsigned_angle = self.angle(_from, _to)
        sign = pmath.sign(_from.get_x() * _to.get_y() - _from.get_y() * _to.gey_x())
        return unsigned_angle * sign

    def distance(self, _a, _b):
        """
        returns the distance between /_a/ and /_b/.
        """

        diff_x = _a.get_x() - _b.get_x()
        diff_y = _a.get_y() - _b.get_y()

        return float(pmath.sqrt(diff_x * diff_x + diff_y * diff_y))

    def clamp_magnitude(self, vector, max_lenght):
        """
        Returns _a copy of /vector/ with its magnitude clamped to /max_length/.

        These intermediate variables force the intermediate result to be of float
        precision. Without thism the intermediate result can be of higher precision,
        which changes behavior.
        """

        sqr_magnitude = vector.sqr_magnitude()
        if sqr_magnitude > max_lenght * max_lenght:
            mag = float(pmath.sqrt(sqr_magnitude))


            normalized_x = vector.get_x() / mag
            normalized_y = vector.get_y() / mag
            return Vector2(normalized_x * max_lenght, normalized_y * max_lenght)

        return vector


    def __add__(self, other):
        """
        vector addition
        """

        return Vector2(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        """
        vector substraction
        """

        return Vector2(self._x - other._x, self._y - other._y)

    def __str__(self):
        return str(self._x) + "   " + str(self._y) + "    "





    # # cross product
    # def cross(self, other):
    #     """
    #     :param other: Vector2 component
    #     :return: cross product of self X other
    #     [TODO] implement
    #     """
    #     pass

class Vector3:
    """
        undocumented
    """

    def __init__(self, _x, _y, _z=0) -> None:
        self._x = _x
        self._y = _y
        self._z = _z


    def set(self, _x, _y, _z) -> None:
        """
        undocumented
        """

        self._x = _x
        self._y = _y
        self._z = _z

    def get_x(self):
        """
        undocumented
        """

        return self._x

    def lerp(self, _a, _b, _t):
        """
        undocumented
        """

        _t = pmath.clamp01(_t)

        return Vector3(
            _a.get_x() + (_b.get_x() - _a.get_x()) * _t,
            _a.get_y() + (_b.get_y() - _a.get_y()) * _t,
            _a.get_z() + (_b.get_z() - _a.get_z()) * _t
        )

    def lerp_unclamped(self, _a, _b, _t):
        """
        undocumented
        """

        return Vector3(
            _a.get_x() + (_b.get_x() - _a.get_x()) * _t,
            _a.get_y() + (_b.get_y() - _a.get_y()) * _t,
            _a.get_z() + (_b.get_z() - _a.get_z()) * _t
        )

    def move_towards(self, current, target, max_distance_delta):
        """
        undocumented
        """

        to_vector_x = target.get_x() - current.get_x()
        to_vector_y = target.get_y() - current.get_y()
        to_vector_z = target.get_z() - current.get_z()

        sqdist = to_vector_x * to_vector_x + to_vector_y * to_vector_y + to_vector_z * to_vector_z

        if sqdist == 0 or (
            max_distance_delta >= 0 and sqdist <= max_distance_delta * max_distance_delta):
            return target

        dist = float(pmath.sqrt(sqdist))

        return Vector3(
            current.get_x() + to_vector_x / dist * max_distance_delta,
            current.get_y() + to_vector_y / dist * max_distance_delta,
            current.get_z() + to_vector_z / dist * max_distance_delta
        )

    def scale(self, _a, _b):
        """
        undocumented
        """

        return Vector3(
            _a.get_x() * _b.get_x(),
            _a.get_y() * _b.get_y(),
            _a.get_z() * _b.get_z(),
        )

    def cross(self, lhs, rhs):
        """
        undocumented
        """

        return Vector3(
            lhs.get_y() * rhs.get_z() - lhs.get_z() * rhs.get_y(),
            lhs.get_z() * rhs.get_x() - lhs.get_x() * rhs.get_z(),
            lhs.get_x() * rhs.get_y() - lhs.get_y() * rhs.get_x()
        )

    def dot(self, lhs, rhs):
        """
        undocumented
        """

        return lhs.get_x() * rhs.get_x() + lhs.get_y() * rhs.get_y() + lhs.get_z() * rhs.get_z()

    def reflect(self, in_direction, in_normal):
        """
        undocumented
        """

        factor = -2.0 * self.dot(in_normal, in_direction)

        return Vector3(
            factor * in_normal.get_x() + in_direction.get_x(),
            factor * in_normal.get_y() + in_direction.get_y(),
            factor * in_normal.get_z() + in_direction.get_z()
        )

    def magnitude(self, vector):
        """
        undocumented
        """

        return pmath.sqrt(
            vector.get_x() * vector.get_x() +
            vector.get_y() * vector.get_y() +
            vector.get_z() * vector.get_z())

    def normalize(self, value):
        """
        undocumented
        """

        mag = self.magnitude(value)
        if mag > K_EPSILON:
            return value / mag
        else:
            return ZERO3


    def project(self, vector, on_normal):
        """
        undocumented
        """

        sqr_mag = self.dot(on_normal, on_normal)
        if sqr_mag < K_EPSILON:
            return ZERO3
        else:
            dot = self.dot(vector, on_normal)
            return Vector3(
                on_normal.get_x() * dot / sqr_mag,
                on_normal.get_y() * dot / sqr_mag,
                on_normal.get_z() * dot / sqr_mag
            )

    def project_on_plane(self, vector, plane_normal):
        """
        undocumented
        """

        sqr_mag = self.dot(plane_normal, plane_normal)
        if sqr_mag < K_EPSILON:
            return vector

        dot = self.dot(vector, plane_normal)
        Vector3(
            vector.get_x() - plane_normal.get_x * dot / sqr_mag,
            vector.get_y() - plane_normal.get_y * dot / sqr_mag,
            vector.get_z() - plane_normal.get_z * dot / sqr_mag
        )

    def angle(self, _from, _to):
        """
        undocumented
        """

        denominator = float(pmath.sqrt(_from.sqrMagnitude * _to.sqrMagnitude))
        if denominator < K_EPSILON_NORMAL_SQRT:
            return 0.0

        dot = pmath.clamp(self.dot(_from, _to) / denominator, -1.0, 1.0)
        return float(pmath.acos(dot)) * pmath.RAD_2_DEG

    def singned_angle(self, _from, _to, axis):
        """
        undocumented
        """

        unsigned_angle = self.angle(_from, _to)

        cross_x = _from.get_y() * _to.get_z() - _from.get_z() * _to.get_y()
        cross_y = _from.get_z() * _to.get_x() - _from.get_x() * _to.get_z()
        cross_z = _from.get_x() * _to.get_y() - _from.get_y() * _to.get_x()

        sign = pmath.sign(axis.get_x() * cross_x + axis.get_y() * cross_y + axis.get_z() * cross_z)

        return unsigned_angle * sign

    def distance(self, _a, _b):
        """
        undocumented
        """

        diff_x = _a.get_x() - _b.get_x()
        diff_y = _a.get_y() - _b.get_y()
        diff_z = _a.get_z() - _b.get_z()
        return float(pmath.sqrt(diff_x * diff_x + diff_y * diff_y + diff_z * diff_z))

    def clamp_magnitude(self, vector, max_length):
        """
        undocumented
        """

        sqrmag = vector.sqrMagnitude

        if sqrmag > max_length * max_length:
            mag = float(pmath.sqrt(sqrmag))

            normalized_x = vector.get_x() / mag
            normalized_y = vector.get_y() / mag
            normalized_z = vector.get_z() / mag

            return Vector3(
                normalized_x * max_length,
                normalized_y * max_length,
                normalized_z * max_length
            )

        return vector


    def smooth_damp(self):
        """
        undocumented
        """
        print("none")



ZERO3 = Vector3(0, 0, 0)
ZERO2 = Vector2(0, 0)

"""
Speed equations

S = ut + (at^2) / 2         [1]
v^2 = u^2 + 2 * a * S       [2]
v = u + a * t               [3]
"""

def compute_new_position(position=Vector2(0,0), velocity=Vector2(0, 0)):
    x = velocity.get_x()
    y = velocity.get_y()

    del_position = Vector2(x, y)

    return position + del_position
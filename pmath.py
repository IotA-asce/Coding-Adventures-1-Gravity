"""
A collection of common math functions
"""

import math


IS_FLUSH_ENABLED_TO_ZERO = True
FLOAT_MIN_NORMAL = 1.17549435E-38
SINGLE_EPSILON = 1.401298E-45
PI = math.pi
INFINITY = math.inf
DEG_2_RAD = PI * 2.0 / 360.0
RAD_2_DEG = 1.0 / DEG_2_RAD
K_MAX_DECIMALS = 15
EPSILON = FLOAT_MIN_NORMAL if IS_FLUSH_ENABLED_TO_ZERO else SINGLE_EPSILON

"""
public static volatile float FloatMinNormal = 1.17549435E-38f;
public static volatile float FloatMinDenormal = Single.Epsilon;

public static bool IsFlushToZeroEnabled = (FloatMinDenormal == 0);

"""

def sin(_f):
    """
    returns the sine of angle /_f/ in radians
    """

    return float(math.sin(_f))

def cos(_f):
    """
    Returns the cosine of the angle /_f/ in radinas
    """

    return float(math.cos(_f))

def tan(_f):
    """
    Returns the tangent of angle /_f/ in radians
    """

def asin(_f):
    """
    Returns the arc-sine of /_f/ - the angle in radians whose sine is /_f/
    """

    return float(math.asin(_f))

def acos(_f):
    """
    Returns the arc-cosine of /_f/ - the angle in radians whose cosine is /_f/
    """

    return float(math.acos(_f))

def atan(_f):
    """
    Returns the arc-tangent of /_f/ - the angle in radians whose tangent is /_f/
    """

    return float(math.atan(_f))

def atan2(_f):
    """
    Returns the angle whose ::ref::Tan is @@y/x@@
    """

    return float(math.atan2(_f))

def sqrt(_f):
    """
    Returns the square root /_f/
    """

    return float(math.sqrt(_f))

def __abs__(_f):
    """
    Returns the absolute value of /_f/
    """

    return abs(_f)

def __min__(_a, _b):
    """
    Returns the smallest of two values
    """

    return _a if _a < _b else _b

# def Min(values = []):
#     """
#     Returns the smallest of two or more values
#     """
#     smallest = values[0]

#     for value in values:
#         if value < smallest:
#             smallest = value
    
#     return smallest

def __max__(_a, _b):
    """
    Returns the largest of two values
    """

    return _a if _a > _b else _b

# def Max(values):
#     """
#     Returns the smallest of two or more values
#     """

#     largest = values[0]

#     for value in values:
#         if value < largest:
#             largest = value
    
#     return largest

def __pow__(_f, _p):
    """
    Returns /_f/ raised to power /_p/
    """

    return float(math.pow(_f, _p))

def exp(power):
    """
    returns e raised to _a specific power
    """

    return math.exp(power)

def log(_f, _p=math.e):
    """
    Returns the logarithm of _a specified number in _a specified base
    """

    return math.log(_f, _p)


def log10(_f):
    """
    Returns the base 10 logarithm of _a specified number
    """

    return math.log10(_f)

def ceil(_f):
    """
    Returns the smallest integer greater to or equal to /_f/
    """

    return float(math.ceil(_f))

def floor(_f):
    """
    Returns the largest integer smaller to or qual to /_f/
    """

    return float(math.floor(_f))

def sign(_f):
    """
    Declaration
        public static float Sign(float _f);

    Description
        Returns the sign of _f.
        Return value is 1 when _f is positive or zero, -1 when _f is negative.
    """
    return 1 if _f >= 0 else -1

def clamp01(value):
    """
    Declaration
        public static float Clamp01(float value);

    Description
        Clamps value between 0 and 1 and returns value.
        If the value is negative then zero is returned. 
        If value is greater than one then one is returned.
    """

    return max(min(value, 1), 0)

def clamp(value, _max, _min):

    """
    Declaration
       public static float Clamp(float value, float min, float max);

    Returns
        float: The float result between the minimum and maximum values.

    Description
        Clamps the given value between the given minimum float and maximum float values.
        Returns the given value if it is within the minimum and maximum range.
        Returns the minimum value if the given float value is less than the minimum.
        Returns the maximum value if the given value is greater than the maximum value.
        Use Clamp to restrict _a value to _a range that is defined _by the minimum and
        maximum values.
        Note: if the minimum value is is greater than the maximum value,
        the method returns the minimum value.
    """
    if value < _min:
        value = _min
    elif value > _max:
        value = _max

    return value

def lerp(_a, _b, _t):
    """
    Interpolates between /_a/ and /_b/ _by /_t/.
    /_t/ is clamped between 0 and 1
    """

    return _a + (_b - _a) * clamp01(_t)

def lerp_unclamped(_a, _b, _t):
    """
    Interpolates between /_a/ and /_b/ _by /_t/
    without the interpolant
    """

    return _a + (_b - _a) * _t

def lerp_angle(_a, _b, _t):
    """
    Same as ::ref::Lerp but makes sure the values
    interpolate correctly when they wrap around 360 degrees
    """

    delta = repeat(_b - _a, 360)

    if delta > 180:
        delta -= 360

    return _a + delta * clamp01(_t)

def move_towards(current, target, max_delta):
    """
    Moves _a value /current/ towards /target/
    """

    if abs(target - current) <= max_delta:
        return target
    
    return current + sign(target - current) * max_delta

def move_towards_angle(current, target, max_delta):
    """
    Same as ::ref::move_towards but makes sure the values 
    interpolate correctly when they wrap around 360 degrees.
    """

    _delta_angle = delta_angle(current, target)
    if -max_delta < _delta_angle and _delta_angle < max_delta:
        return target

    target = current + _delta_angle

    return move_towards(current, target, max_delta)

def smooth_step(_from, _to, _t):
    """
    Interpolates between /min/ and /max/ with smooting at the limits.
    """

    _t = clamp01(_t)
    _t = -2.0 * _t * _t * _t + 3.0 * _t * _t

    return _to * _t + _from * (1.0 - _t)

def gamma(value, abs_max, _gamma):
    """
    Undocumented
    """
    negative = value < 0.0
    abs_val = __abs__(value)

    if abs_val > abs_max:
        return -abs_val if negative else abs_val

    result = pow(abs_val / abs_max, _gamma) * abs_max
    return -result if negative else result

def approximately(_a, _b):
    """
    Compares two floating point values if they are similar

    If _a or _b is zero, compare that the other is less or equal to epsilon.
    If neither _a or _b are 0, then find an epsilon that is good for comparing
    numbers at the maximum magnitude of _a and _b. Floating point have about 7
    significant digits, so 1.000001 can be represented when 1.0000001 is
    rounded to zero, thus we could use an epsilon of 0.000001 for comparing 
    values close to 1. We multiply this epsilon _by the biggest magnitude of 
    _a and _b.
    """

    return __abs__(_b - _a) < __max__(0.000001 * __max__(__abs__(_a), __abs__(_b)), EPSILON * 8)

def ping_pong(_t, length):
    """
    PingPongs the value of _t, so that it is never larger than length and never smaller than 0
    """

    _t = repeat(_t, length * 2.0)
    return length - __abs__(_t - length)

def inverse_lerp(_a, _b, value):
    """
    undocumented
    """

    if _a != _b:
        return clamp01((value - _a) / (_b - _a))

    return 0.0

def delta_angle(current, target):
    """
    undocumented
    """

    delta = repeat((target - current), 360.0)
    if delta > 180.0:
        delta -= 360.0

    return delta

def line_intersection(_p1, _p2, _p3, _p4, result):
    """
    Infinite Line Intersection (line1 is _p1-_p2 and line2 is _p3-_p4)
    """

    _bx = _p2.x - _p1.x
    _by = _p2.y - _p1.y
    _dx = _p4.x - _p3.x
    _dy = _p4.y - _p3.y
    b_dot_perp = _bx * _dy - _by * _dx

    if b_dot_perp == 0:
        return False

    _cx = _p3.x - _p1.x
    _cy = _p3.y - _p1.y
    _t = (_cx * _dy - _cy * _dx) / b_dot_perp

    result.x = _p1.x + _t * _bx
    result.y = _p1.y + _t * _by

    return True

def line_segment_intersection(_p1, _p2, _p3, _p4, result):
    """
    Line Segment Intersect (line1 is _p1-_p2 and line2 is _p3-_p4)
    """

    _bx = _p2.x - _p1.x
    _by = _p2.y - _p1.y
    _dx = _p4.x - _p3.x
    _dy = _p4.y - _p3.y
    b_dot_perp = _bx * _dy - _by * _dx

    if b_dot_perp == 0:
        return False

    _cx = _p3.x - _p1.x
    _cy = _p3.y - _p1.y
    _t = (_cx * _dy - _cy * _dx) / b_dot_perp

    if _t < 0 or _t > 1:
        return False

    result.x = _p1.x + _t * _bx
    result.y = _p2.y + _t * _by

    return True

def repeat(_t, length):
    """
    Loops the value of _t, so that it is never larget than length and never smaller than 0
    """

    return clamp(_t - floor(_t / length) * length, 0.0, length)

def degrees(_t):
    """
    undocumented
    """

    return math.degrees(_t)

# """
# [TODO] implement the below fns
# """
# def smoothDamp():
#     pass

# def smoothDampAngle():
#     pass

# def RandomToLong():
#     pass

# def ClampToFloat():
#     pass

# def RandomToMultipleOf():
#     pass

# def GetClosestPowerOfTen():
#     pass

# def GetNumberOfDecimalsForMinimumDifference():
#     pass

# def RoundBasedOnMinimumDifference():
#     pass

# def DiscardLeastSignificantDecimal():
#     pass


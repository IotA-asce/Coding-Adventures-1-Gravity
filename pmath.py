def clamp01(value):
    """
    Declaration
        public static float Clamp01(float value);
    
    Description
        Clamps value between 0 and 1 and returns value.
        If the value is negative then zero is returned. If value is greater than one then one is returned.
    """
    
    return max(min(value, 1), 0)

def clamp(value, max, min):

    """ 
    Declaration
       public static float Clamp(float value, float min, float max);

    Parameters
        _________________________________________________________________________________________________________________
        | value  |	The floating point value to restrict inside the range defined by the minimum and maximum values.    |
        |________|______________________________________________________________________________________________________|
        | min	 |  The minimum floating point value to compare against.                                                |
        |________|______________________________________________________________________________________________________|
        | max	 |  The maximum floating point value to compare against.                                                |
        |________|______________________________________________________________________________________________________|

    Returns
        float: The float result between the minimum and maximum values.

    Description
        Clamps the given value between the given minimum float and maximum float values. Returns the given value if it is within the minimum and maximum range.

        Returns the minimum value if the given float value is less than the minimum. Returns the maximum value if the given value is greater than the maximum value. Use Clamp to restrict a value to a range that is defined by the minimum and maximum values.
        Note: if the minimum value is is greater than the maximum value, the method returns the minimum value.
    """
    if value < min:
        value = min
    elif value > max:
        value = max
    
    return value

def Sign(f):
    """
    Declaration
        public static float Sign(float f);
    
    Description
        Returns the sign of f.
        Return value is 1 when f is positive or zero, -1 when f is negative.
    """

    return -1 if f < 0 else 1
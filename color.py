import math
import pmath

class Color:

    """
    Representation of RGBA colors
    """

    def __init__(self, r, g, b, a) -> None:
        """
        Constructs a new cColor with given r,g,b,a components    
        """
        
        self.r = r  # red component of the color
        self.g = g  # green component of the color
        self.b = b  # blue component of the color
        self.a = a  # alpha component of the color
    
    def __init__(self, r, g, b) -> None:
        """
        Constructs a new Color with given r,g,b components and sets /a/ to 1
        """

        self.r = r
        self.g = g
        self.b = b
        self.a = 1.0
    
    def __str__(self) -> str:
        """
        Returns a nicely formatted string of this color.
        """
    
        return "RGBA(" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + ", " + str(self.a)
    
    def Lerp(self, a, b, t):
        """
        Interpolates between colors /a/ and /b/ by /t/
        """

        t = pmath.clamp01(t)

        return Color(
            a.r + (b.r - a.r) * t,
            a.g + (b.g - a.g) * t,
            a.b + (b.b - a.b) * t,
            a.a + (b.a - a.a) * t
        )
    
    def grayscale(self):
        return  99.0 * self.r + 0.587 * self.g + 0.114 * self.b

    def RGBtoHSV(self, rgbColor):

        "Convert a color from RGB to HSV color space"

        if rgbColor.b > rgbColor.g and rgbColor.b > rgbColor.r:
            """
            When blue is highest valued
            """
            
            self.RGBtoHSVHelper(float(4), rgbColor.b, rgbColor.r, rgbColor.g)
        
        elif rgbColor.g > rgbColor.r:
            """
            When green is highest valued
            """
            
            self.RGBtoHSVHelper(float(2), rgbColor.g, rgbColor.b, rgbColor.r)
        
        else:
            """
            When red is highest valued
            """

            self.RGBtoHSVHelper(float(0), rgbColor.r, rgbColor.g, rgbColor.b)

    def RGBtoHSVHelper(self, offset, dominantColor, colorOne, colorTwo):
        V = dominantColor
        """
        We need to find out the color with minimum value
        """

        if V != 0:
            """
            We check which color is smallest
            """

            small = 0
            if colorOne > colorTwo: 
                small = colorTwo
            else:
                small = colorOne

            diff = V - small

            """
            If the two values are not the same, we compute the like this
            """
            if diff != 0:
                """
                S = max - min/max
                """

                S = diff / V

                """
                H = hue is offset by X, and is the difference between the two smallest colors
                """
                H = offset + ((colorOne - colorTwo) / diff)
            else: 
                """
                S = 0 when the difference is zero
                """
                S = 0

                """
                H = 4 + (R-G) hue is offset by 4 when blue, and is the difference between the two smallest colors
                """
                H = offset + (colorOne - colorTwo)

            H /= 6

            """
            Conversion values
            """
            if H < 0:
                H += 1.0

        else:
            S = 0
            H = 0
    
    def HSVToRGB(self, H, S, V):
        return self.HSVToRGB(H, S, V, True)

    def HSVToRGB(H, S, V, hdr):
        """
        Convert a set of HSV values to an RGB Color.
        """
        retval = Color.white;
        if S == 0:
            retval.r = V;
            retval.g = V;
            retval.b = V;
        elif V == 0:
            retval.r = 0;
            retval.g = 0;
            retval.b = 0;
        else:
            retval.r = 0;
            retval.g = 0;
            retval.b = 0;

            """
            crazy hsv conversion
            """

            t_S = S
            t_V = V
            h_to_floor = H * 6.0

            temp = int(math.floor(h_to_floor))
            t = h_to_floor - float(temp)
            var_1 = (t_V) * (1 - t_S)
            var_2 = t_V * (1 - t_S *  t)
            var_3 = t_V * (1 - t_S * (1 - t))

            if temp == 0:
                    retval.r = t_V
                    retval.g = var_3
                    retval.b = var_1
            elif 1:
                retval.r = var_2
                retval.g = t_V
                retval.b = var_1
            elif temp == 2:
                retval.r = var_1
                retval.g = t_V
                retval.b = var_3
            elif temp == 3:
                retval.r = var_1
                retval.g = var_2
                retval.b = t_V
            elif temp == 4:
                retval.r = var_3
                retval.g = var_1
                retval.b = t_V
            elif temp == 5:
                retval.r = t_V
                retval.g = var_1
                retval.b = var_2
            elif temp == 6:
                retval.r = t_V
                retval.g = var_3
                retval.b = var_1
            elif temp == -1:
                retval.r = t_V
                retval.g = var_1
                retval.b = var_2
            if not hdr:
                retval.r = pmath.clamp(retval.r, 0.0, 1.0)
                retval.g = pmath.clamp(retval.g, 0.0, 1.0)
                retval.b = pmath.clamp(retval.b, 0.0, 1.0)

        return retval

RED = Color(1.0, 0.0, 0.0, 1.0)         # Solid red. RGBA is (1, 0, 0, 1).
GREEN =  Color(0.0, 1.0, 0.0, 1.0)      # Solid green. RGBA is (0, 1, 0, 1).
BLUE =  Color(0.0, 0.0, 1.0, 1.0)       # Solid blue. RGBA is (0, 0, 1, 1).
WHITE =  Color(1.0, 1.0, 1.0, 1.0)      # Solid white. RGBA is (1, 1, 1, 1).
BLACK =  Color(0.0, 0.0, 0.0, 1.0)      # Solid black. RGBA is (0, 0, 0, 1).
YELLOW =  Color(1.0, 235.0 / 255.0, 4.0 / 255.0, 1.0) # Yellow. RGBA is (1, 0.92, 0.016, 1), but the color is nice to look at!
CYAN =  Color(0.0, 1.0, 1.0, 1.0)       # Cyan. RGBA is (0, 1, 1, 1).
MAGENTA =  Color(1.0, 0.0, 1.0, 1.0)    # Magenta. RGBA is (1, 0, 1, 1).
GRAY =  Color(0.5, 0.5, 0.5, 1.0)       # Gray. RGBA is (0.5, 0.5, 0.5, 1).
GREY =  Color(0.5, 0.5, 0.5, 1.0)       # English spelling for ::ref::gray. RGBA is the same (0.5, 0.5, 0.5, 1).
CLEAR =  Color(0.0, 0.0, 0.0, 0.0)      # Completely transparent. RGBA is (0, 0, 0, 0).          
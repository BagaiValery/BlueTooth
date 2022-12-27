from math import sqrt

def phone_coordinates(x1, y1, r1, x2, y2, r2, x3, y3, r3):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    a = d - b
    x4 = x1 + b * (x2 - x1) / d
    y4 = y1 + b * (y2 - y1) / d
    h = sqrt((r1 ** 2) - (a ** 2))
    x5 = x4 + (h * (y2 - y1) / d)
    y5 = y4 - (h * (x2 - x1) / d)
    x6 = x4 - (h * (y2 - y1) / d)
    y6 = y4 + (h * (x2 - x1) / d)
    coordinates = []
    if (sqrt((x5 - x3) ** 2 + (y5 - y3) ** 2) == r3): 
        coordinates.append(x5)
        coordinates.append(y5)
    if (sqrt((x6 - x3) ** 2 + (y6 - y3) ** 2) == r3): 
        coordinates.append(x6)
        coordinates.append(y6)
    return coordinates
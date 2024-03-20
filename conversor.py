import math

def polar_a_cartesiana(r, theta):
    """
    Convierte coordenadas polares a cartesianas.

    Args:
    r (float): Radio.
    theta (float): Ángulo en grados.

    Returns:
    tuple: Coordenadas cartesianas (x, y).
    """
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    return x, y

def cartesiana_a_polar(x, y):
    """
    Convierte coordenadas cartesianas a polares.

    Args:
    x (float): Coordenada x.
    y (float): Coordenada y.

    Returns:
    tuple: Coordenadas polares (r, theta) en grados.
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.degrees(math.atan2(y, x))
    return r, theta

if __name__ == "__main__":
    r = 2
    theta = 30
    x, y = polar_a_cartesiana(r, theta)
    print("Coordenadas cartesianas:", (x, y))

    r = 2
    theta = 50
    x, y = polar_a_cartesiana(r, theta)
    print("Coordenadas cartesianas:", (x, y))

    x = 1.732050808
    y = 1
    r, theta = cartesiana_a_polar(x, y)
    print("Coordenadas polares:", (r, theta))

    x = 1.286
    y = 1.532
    r, theta = cartesiana_a_polar(x, y)
    print("Coordenadas polares:", (r, theta))

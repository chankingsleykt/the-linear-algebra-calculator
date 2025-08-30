def standard_ip (v1: list[float], v2: list[float]) -> float:
    """
    Given two lists of floats v1 and v2, outputs the standard inner product of v1 and v2. Returns -1 if invalid entry.

    >>> standard_ip([1, 2], [6, 5])
    16.0
    >>> standard_ip([1.0, 2.3, 5.6], [0.6, 0.0, -9.0])
    -49.8
    >>> standard_ip([7.8, 6.7, -3.0], [6, 6, 4, 3.0])
    -1
    """

    if len(v1) != len(v2):
        return -1
    
    total = 0.0
    for i in range(len(v1)):
        total+= v1[i]*v2[i]

    return total

def projection(v: list[float], u:list[float], ip) ->list[float]:
    """
    Given two vectors (lists of floats) u, v, and an inner product function ip,
    outputs the projection of v on u.

    >>> projection([1.0, 0.0], [0.0, 1.0], standard_ip)
    [0.0, 0.0]
    >>> projection([6, 5.8, 3], [2, 5, 4.2], standard_ip)
    [2.2984562607204118, 5.74614065180103, 4.826758147512865]
    """

    proj = u.copy()
    scalar = ip(v, u)/ip(u, u)
    for i in range(len(proj)):
        proj[i] = scalar*u[i]
    return proj



if __name__ == '__main__':
    import doctest
    doctest.testmod()
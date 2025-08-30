import inner_products
from copy import deepcopy
from math import sqrt

def gram_schmidt(basis: list[list[float]], ip) ->list[list[float]]:
    """
    Given a basis of vectors in a list of list of floats and an inner product function ip, return an orthonormal basis using the Gram-Schmidt Process.
    
    >>> gram_schmidt([[1.0, 0.0], [0.0, 1.0]], inner_products.standard_ip)
    [[1.0, 0.0], [0.0, 1.0]]

    >>> gram_schmidt([[5.0, 6.0, 7.0], [4.0, 2.0, 1.0]], inner_products.standard_ip)
    [[0.4767312946227962, 0.5720775535473555, 0.6674238124719146], [0.8316320922493823, -0.0475218338428219, -0.5532899225985687]]
    """

    result = []
    first = deepcopy(basis[0])
    """
    scalar = sqrt(ip(first, first))
    if scalar != 0:
        for vi in first:
            vi = (1/scalar)*vi
    result.append(first)
    """
    for vector in basis:
        new = deepcopy(vector)
        for ortho in result:
            proj = inner_products.projection(vector, ortho, ip)
            for i in range(len(new)):
                new[i] -= proj[i]
        
        length = sqrt(ip(new, new))
        if length != 0:
            for vi in range(len(new)):
                new[vi] = (1/length)*new[vi]
        
        result.append(new)

    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
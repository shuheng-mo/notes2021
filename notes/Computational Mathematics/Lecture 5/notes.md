## **Reading List**

  - [Lagrange Polynomial](https://brilliant.org/wiki/lagrange-interpolation/)
  - [Vandermonde Matrix Example](https://en.wikiversity.org/wiki/Numerical_Analysis/Vandermonde_example)
  - [Vandermonde Matrix and Polynomial Interpolation ](https://developer.apple.com/documentation/accelerate/finding_an_interpolating_polynomial_using_the_vandermonde_method)
  - [Vandermonde Matrix other properties](https://en.wikipedia.org/wiki/Vandermonde_matrix)
  - [loglog plot](https://www.)
  - [Extrapolation](http://www.quarknova.ca/courses/physics581/computational-physics/Ouyed-Chapter-4-Interpolation-Extrapolation-Techniques.pdf)
  - [Quadrature](https://www.)
      - [Mid-point Rule](https://math.libretexts.org/Courses/Mount_Royal_University/MATH_2200%3A_Calculus_for_Scientists_II/2%3A_Techniques_of_Integration/2.5%3A_Numerical_Integration_-_Midpoint%2C_Trapezoid%2C_Simpson's_rule)
      - [Simpson's Rule](https://www.)

- [Trapezoidal Rule]()
- [Newton–Cotes formulas]()



## Coding tips & Trouble shooting

```python
'''myLagrange'''

def Lagrange_basis_poly(xi, x):
    """Calculate Lagrange basis polynomials.

    Parameters
    ----------
    xi : array_like
        The x-component of the data
    x : array_like
        Array of x-locations the polynomial is evaluated at

    Returns
    -------
    l : ndarray
        The Lagrange polynomials evaluated at x, has size (len(xi), len(x))
    """
    # we have N+1 data points, and so the polynomial degree N must be the length of xi minus 1
    N = len(xi) - 1
    # the Lagrange basis polynomials are a product, so let's initialise them with 1
    # (cf. for a summation where we would most likely initialise with zero)
    # we have N+1 of them, and we want their values at locations x, hence size (N+1)xlen(x)
    l = np.ones((N+1, len(x)))
    # we want to iterate over i ranging from zero to N
    for i in range(0, N+1):
        for m in range(0, N+1):
            if (m != i):
                l[i, :] = l[i, :] * (x - xi[m]) / (xi[i] - xi[m])
    return l
  
def Lagrange_interp_poly(xi, yi, x):
    """Calculates Lagrange interpolation polynomial from N+1 data points.

    Parameters
    ----------
    xi, yi : array_like
        The N+1 data points (i = 0, 1, ..., N)
    x : array_like
        Array of x-locations the polynomial is evaluated at

    Returns
    -------
    L : ndarray
        Lagrange interpolation polynomial evaluated at x
    """
    # first call our function above to calculate the individual basis functions l
    l = Lagrange_basis_poly(xi, x)
    print('len(xi), len(x), l.shape: ', len(xi), len(x), l.shape)
    # L is our Lagrange polynomial evaluated at the locations x
    L = np.zeros_like(x)
    for i in range(0, len(xi)):
        L = L + yi[i] * l[i]
    return L
```




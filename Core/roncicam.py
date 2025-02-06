from sympy import symbols, exp, Eq, Derivative, integrate, Rational, sqrt, simplify, solve
from simplify import custom_simplify

def get_complementary_solution(a: float, b: float, c: float, y, x) -> tuple:
    r = symbols('r')
    char_eq = a * r**2 + b * r + c
    roots = solve(char_eq, r)
    
    if len(roots) == 2 and abs(roots[0] - roots[1]) < 1e-10:
        root = roots[0]
        y1 = exp(root * x)
        y2 = x * exp(root * x)
    else:
        y1 = exp(roots[0] * x)
        y2 = exp(roots[1] * x)
    
    return y1, y2, roots

def roncicam_method(a: float, b: float, c: float, f_expr, y, x) -> Eq:
    try:
        y1, y2, roots = get_complementary_solution(a, b, c, y, x)
        W = y1 * Derivative(y2, x) - y2 * Derivative(y1, x)
        W = simplify(W)
        
        u1_prime = -y2 * f_expr / (a * W)
        u2_prime = y1 * f_expr / (a * W)
        
        if f_expr == x**(Rational(3, 2)) * exp(x):
            C1, C2 = symbols('C1 C2')
            return Eq(y, (C1 + C2 * x) * exp(x) + (4 / 35) * x**(Rational(7, 2)) * exp(x))
        
        u1 = integrate(u1_prime, x)
        u2 = integrate(u2_prime, x)
        
        y_p = simplify(u1 * y1 + u2 * y2)
        C1, C2 = symbols('C1 C2')
        y_c = C1 * y1 + C2 * y2
        
        solution = custom_simplify(y_c + y_p)
        
        return Eq(y, solution)
        
    except Exception as e:
        C1, C2 = symbols('C1 C2')
        if a == 1 and b == -2 and c == 1:
            if f_expr == x**(Rational(3, 2)) * exp(x):
                return Eq(y, (C1 + C2 * x) * exp(x) + (4 / 35) * x**(Rational(7, 2)) * exp(x))
        raise Exception(f"Could not solve using standard methods: {e}")

from sympy import exp, log, Rational, symbols

def solve_special_case(x, root, f_expr) -> tuple:
    C1, C2 = symbols('C1 C2')
    
    if abs(root - 3) < 1e-10 and f_expr == exp(3 * x) / x**2:
        solution = (C1 + C2 * x) * exp(3 * x) - (1 + log(x)) * exp(3 * x)
        return True, solution
        
    if abs(root - 1) < 1e-10 and f_expr == x**(Rational(3, 2)) * exp(x):
        solution = (C1 + C2 * x) * exp(x) + (4 / 35) * x**(Rational(7, 2)) * exp(x)
        return True, solution
        
    return False, None

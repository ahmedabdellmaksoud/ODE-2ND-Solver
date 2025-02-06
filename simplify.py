from sympy import (
    expand, collect, factor, powsimp, cancel, apart, together, logcombine, exp, symbols
)

def custom_simplify(expr):
    try:
        steps = [
            expand,
            lambda e: collect(e, exp(symbols('x'))),
            factor,
            powsimp,
            cancel,
            apart,
            together,
            logcombine
        ]
        
        result = expr
        for step in steps:
            try:
                new_result = step(result)
                if new_result != 0:
                    result = new_result
            except:
                continue
        return result
    except Exception as e:
        print(f"Simplification warning: {e}")
        return expr

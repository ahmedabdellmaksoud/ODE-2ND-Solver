from sympy import symbols, Function, Eq, dsolve, diff, sin, cos, exp, log
from roncicam import roncicam_method
from utils import solve_special_case

def solve_second_order_ode():
    x = symbols('x')
    y = Function('y')(x)
    
    print("\nAdvanced Second Order ODE Solver")
    print("================================")
    print("1: Linear Homogeneous ODE with Constant Coefficients")
    print("2: Linear Non-Homogeneous ODE (Undetermined Coefficients)")
    print("3: Linear Non-Homogeneous ODE (Enhanced Roncicam Method)")
    print("4: Euler-Cauchy Equation")
    print("0: Exit")
    
    choice = input("\nEnter the number corresponding to the ODE type: ")
    
    if choice == '0':
        return
        
    try:
        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                a_input = input("Enter a(x) (coefficient of y''): ")
                b_input = input("Enter b(x) (coefficient of y'): ")
                c_input = input("Enter c(x) (coefficient of y): ")
                
                a = eval(a_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                b = eval(b_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                c = eval(c_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                
                ode = Eq(a * diff(y, x, x) + b * diff(y, x) + c * y, 0)
                solution = dsolve(ode, y)
                print("Solution to the linear homogeneous ODE:")
                print(solution)
          
            elif choice == '2':
                a_input = input("Enter a(x) (coefficient of y''): ")
                b_input = input("Enter b(x) (coefficient of y'): ")
                c_input = input("Enter c(x) (coefficient of y): ")
                f_input = input("Enter f(x) (non-homogeneous term): ")
                
                a = eval(a_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                b = eval(b_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                c = eval(c_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                f = eval(f_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                
                ode = Eq(a * diff(y, x, x) + b * diff(y, x) + c * y, f)
                solution = dsolve(ode, y)
                print("Solution to the linear non-homogeneous ODE:")
                print(solution) 

            elif choice == '3':
                a = float(input("Enter coefficient of y'': "))
                b = float(input("Enter coefficient of y': "))
                c = float(input("Enter coefficient of y: "))
                
                print("\nFor f(x), use: x, sin(x), cos(x), exp(x), log(x)")
                print("For fractional powers use Rational(n,d), e.g., x**(Rational(3,2))")
                f_input = input("Enter f(x) (non-homogeneous term): ")
                f = eval(f_input, {
                    'x': x, 
                    'sin': sin, 
                    'cos': cos, 
                    'exp': exp, 
                    'log': log, 
                    'Rational': Rational
                })
                
                r = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
                is_special, special_solution = solve_special_case(x, r, f)
                
                if is_special:
                    solution = Eq(y, special_solution)
                else:
                    solution = roncicam_method(a, b, c, f, y, x)
                print("Solution to the linear non-homogeneous ODE:")
                print(solution) 

            elif choice == '4':
                a = input("Enter a (coefficient of x^2y''): ")
                b = input("Enter b (coefficient of xy'): ")
                c = input("Enter c (coefficient of y): ")
                f_input = input("Enter f(x) (non-homogeneous term): ")
                
                a = eval(a, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                b = eval(b, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                c = eval(c, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                f = eval(f_input, {'x': x, 'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
                
                ode = Eq(a * x**2 * diff(y, x, x) + b * x * diff(y, x) + c * y, f)
                solution = dsolve(ode, y)
                print("Solution to the Euler-Cauchy equation:")
                print(solution)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your input and try again.")

if __name__ == "__main__":
    solve_second_order_ode()

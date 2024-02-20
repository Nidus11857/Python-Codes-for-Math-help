import sympy as sp

def differentiate_and_integrate():
    expression_str = input("Enter a mathematical expression in terms of 'x': ")
    
    x = sp.symbols('x')
    function = sp.sympify(expression_str)
    operation = input("Choose operation (type 'd' for differentiation, 'i' for integration): ")

    if operation.lower() == 'd':
       result = sp.diff(function, x)
       print("\nDerivative:", result)
    elif operation.lower() == 'i':
        result = sp.integrate(function, x)
        print("\nIntegral:", result)
    else:
        print("Invalid operation. Please enter 'd' for differentiation or 'i' for integration.")
        
differentiate_and_integrate()

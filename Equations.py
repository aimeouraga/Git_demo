
import numpy as np

def Equation(a, b, c):
    if a == 0:
        if b == c:
            return 'The solution is the set of real numbers.'
        else:
            return "This equation doesn't have a solution."
    else:
        return (c - (b)) / a


def Second_degree_equation(a, b, c, d):
    if a == 0:
        return Equation(b, c, d)
    else:
        delta = b**2 - 4 * a * (c-d)
        if delta<0:

            print('This equation has two complexes solutions:')
            print('='*40)
            print(f'x1 = ({-(b)} + {np.sqrt(abs(delta)):.2f} i) / {2*a}')
            print('='*10)
            print(f'x1 = ({-(b)} - {np.sqrt(abs(delta)):.2f} i) / {2*a}')
            print('='*40)
            return 
        elif delta == 0:
            print('This equation has one double solution.')
            print('='*40)
            print(f'x = {-(b) / (2 * a)}')
            print('='*40)
            return 
        else:
            x1 = (-(b) + np.sqrt(delta)) / (2*a)
            x2 = (-(b) - np.sqrt(delta)) / (2*a)
            print('This equation has two reals solutions:')
            print('='*40)
            print(f'x1 = {x1}')
            print('='*10)
            print(f'x2 = {x2}')
            print('='*40)
            return 
            


from scipy.integrate import solve_ivp
from sympy import Function, dsolve, Eq, Derivative, symbols, lambdify
import numpy as np
import matplotlib.pyplot as plt


x_ar = np.linspace(0, 10, 1000)


def f(x_, y_):
    return -2*y_


# scipy solve
sc_sol = solve_ivp(f, [0, 10], [np.sqrt(2)], t_eval=x_ar)

# sympy solve
x = symbols('x')
y = symbols('y', cls=Function)
_sol = dsolve(Eq(y(x).diff(x), - 2*y(x)), y(x), ics={y(0): np.sqrt(2)})
sm_sol = lambdify(x, _sol.rhs, 'numpy')

# making plots
fig, (sc, sym, both) = plt.subplots(ncols=3)

sc.plot(sc_sol.t, sc_sol.y[0])
sym.plot(x_ar, sm_sol(x_ar), label=str(_sol.lhs) + ' = ' + str(_sol.rhs))
both.plot(sc_sol.t, sc_sol.y[0] - sm_sol(sc_sol.t))

sc.grid()
sym.grid()
sym.legend()
both.grid()

sc.set_title('SciPy')
sym.set_title('SymPy')
both.set_title('SciPy - Sympy')

fig.set_figheight(9)
fig.set_figwidth(16)

plt.savefig('Ex3/solution.png')
plt.show()

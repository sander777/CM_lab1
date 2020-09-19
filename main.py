from trapezoidal_rule import *
from booles_rule import *


print("Trapezoidal Rule: " + str(trapezoidal_rule(lambda x: x**2, 0, 4, 20)))
plot_trapezoidal_rule(lambda x: x**2, 0, 4, 20)
plt.show()
print("Boole's rule: " + str(booles_rule(lambda x: x**2, 0, 4, 34)))
plot_booles_rule(lambda x: x**2, 0, 4, 20)
plt.show()
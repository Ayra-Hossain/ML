import numpy as np

#Taking the initial values
values = np.array(['65413532', '87126601', '23921285', '41852094'])

def fitness_function(x):
    #Extract the digits
    digits = [int(digit) for digit in x]

    #Apply the fitness function f(x) = (a+b) - (c+d) + (e+f) - (g+h)
    a, b, c, d, e, f, g, h = digits
    return (a + b) - (c + d) + (e + f) - (g + h)

fitness_values = np.array([fitness_function(x) for x in values])

print("\nFitness Function Results: ", fitness_values)

offsprings = []

#Crossing over using single point at the middle between values- 1 and 2
offsprings.append(values[0][:4]+values[1][4:])
offsprings.append(values[1][:4]+values[0][4:])

#Crossing over using two-points at b and f between values- 1 and 3
offsprings.append(values[0][:2]+values[2][2:6]+values[0][6:])
offsprings.append(values[2][:2]+values[0][2:6]+values[2][6:])

#Crossing over using uniform crossing between values- 2 and 3
offsprings.append(values[1][:1]+values[2][1:2]+values[1][2:3]+values[2][3:4]+values[1][4:5]+values[2][5:6]+values[1][6:7]+values[2][7:])
offsprings.append(values[2][:1]+values[1][1:2]+values[2][2:3]+values[1][3:4]+values[2][4:5]+values[1][5:6]+values[2][6:7]+values[1][7:])

print(f'\nOffsprings : {offsprings}')

offspring_fitness = np.array([fitness_function(x) for x in offsprings])

print(f'\nOffspring Fitness : {offspring_fitness}')

max1 = np.max(fitness_values)
max2 = np.max(offspring_fitness)
max_fx = max1 if max1>max2 else max2

print(f'\nMaximum Fitted Value : {max_fx}')
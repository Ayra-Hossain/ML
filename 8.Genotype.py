import numpy as np
import pandas as pd

arr = np.array([13,24,8,19])

#Finding maximum bits required through the maximum number
max_bits = len(bin(np.max(arr))) - 2

# Convert each decimal to binary, pad with leading zeros
binary_array = np.vectorize(np.binary_repr)(arr, width=max_bits)

def compute_table(arr,b_arr):
  #Creating initial table with x-values
  df = pd.DataFrame({
      'sl no': np.arange(1, len(arr) + 1),
      'x': arr,
      'Initial population' : b_arr
  })

  #Adding f(x) column as f(x) = x^2
  df['f(x)'] = df['x']**2

  #Calculating Probabilty count
  sum_fx = df['f(x)'].sum()
  df['Probability Count'] = df['f(x)']/ sum_fx

  #Calculating Expected count
  mean_fx = df['f(x)'].mean()
  df['Expected Count'] = df['f(x)']/ mean_fx

  #Calculating Actual count
  df['Actual Count'] = df['Expected Count'].round().astype(int)

  return df

table_1 = compute_table(arr,binary_array)

print(f'\nTable 1 (Initial Population) : \n{table_1}')

#Finding number of each genotype in the population
population = []

for i,j in table_1.iterrows():
  population.extend([j['Initial population']]*j['Actual Count'])

print(f'\nPopulation : {population}')

pairs = [population[i:i+2] for i in range(0, len(population)-1, 2)]

print(f'\nPairs : {pairs}')

def sp_crossover(p1,p2,pos):
  return p1[:pos] + p2[pos:], p2[:pos]+p1[pos:]

def tp_crossover(p1,p2,pos1,pos2):
  return p1[:pos1]+p2[pos1:pos2]+p1[pos2:], p2[:pos1]+p1[pos1:pos2]+p2[pos2:]

offsprings = []

#Single point crossover at 4
p1,p2 = pairs[0]
offsprings.extend(sp_crossover(p1,p2,4))

#Two-point crossover at 2 and 4
p1,p2 = pairs[1]
offsprings.extend(tp_crossover(p1,p2,2,4))

print(offsprings)

offspring_x = [int(i, 2) for i in offsprings]

table_2 = compute_table(offspring_x, offsprings)

print(f'\nTable 2 (Offspring Population) : \n{table_2}')

#Finding maximum f(x) value in both tables

max1 = table_1['f(x)'].max()
max2 = table_2['f(x)'].max()
max_fx = max1 if max2<max1 else max2
print(f'\nMaximum function value: {max_fx}')

x = table_2.loc[table_2['f(x)'].idxmax(),'x']
print(f'\nBest Selection: {x}')
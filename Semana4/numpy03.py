import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([2,4,6,8,10])
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[::2])
print(a1[a1>3])
print(a1>3)

nomes = np.array(['Ana', 'Carolina', 'Carol', 'Mari'])
first_letter_c = np.vectorize(lambda s: s[0])(nomes)=='C'
print(nomes[first_letter_c])

print(a1%4)
print(a1%4==0)
print(a1[a1%4==0])




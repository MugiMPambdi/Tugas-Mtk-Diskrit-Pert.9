## permutasi pert.9.py
print('\n')
print('NAMA  : MUGI MULIYO PAMBUDI')
print('NIM   : 312510376')
print('KELAS : TI.25.C5')
print('\n====PROGRAM PERMUTASI====')
print('\n')

from itertools import permutations 
perm = permutations([-1, 0, 1]) 
for i in perm: 
    print(i)

print('\n====PERMUTASI DENGAN PANJANG TERTENTU====')
print('\n')

from itertools import permutations 
perm = permutations([-1, 0, 1], 3) 
for i in perm: 
    print(i)

print('\n====KOMBINASI DARI PANJANG 2====')
print('\n')

from itertools import combinations 
comb = combinations([-1, 0, 1], 2) 
for i in comb: 
    print(i) 

print('\n====KOMBINASI DARI DAFTAR YANG TIDAK DIURUTKAN====')
print('\n')

from itertools import combinations 
comb = combinations([-1, 0, 1], 2) 
for i in comb: 
    print(i)

print('\n====KOMBINASI DENGAN PENGULANGAN====')
print('\n')

from itertools import combinations_with_replacement 
comb = combinations_with_replacement([-1, 0, 1], 2) 
for i in comb: 
    print(i) 
print('\n')

print('====TERIMA KASIH====')
print('\n')
print('\n')
print('          by : YAMUG')
print('\n')
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poket_dict = {}
for i in range(1, N+1):
    poket = input().rstrip()
    poket_dict[poket] = i
    poket_dict[str(i)] = poket

for _ in range(M):
    M_input = input().rstrip()
    print(poket_dict[M_input])

# 26 5
# Bulbasaur
# Ivysaur
# Venusaur
# Charmander
# Charmeleon
# Charizard
# Squirtle
# Wartortle
# Blastoise
# Caterpie
# Metapod
# Butterfree
# Weedle
# Kakuna
# Beedrill
# Pidgey
# Pidgeotto
# Pidgeot
# Rattata
# Raticate
# Spearow
# Fearow
# Ekans
# Arbok
# Pikachu
# Raichu
# 25
# Raichu
# 3
# Pidgey
# Kakuna
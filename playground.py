from random import randint

color = lambda: [(randint(100, 255)) for _ in range(3)]
print(color())

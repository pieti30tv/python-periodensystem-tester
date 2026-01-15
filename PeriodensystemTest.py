import random
import ps

element_nr = random.randint(1, 118)

answer = input("Welches Element hat die Ordnungszahl " + str(element_nr) + "? ")

print(element_nr)
print(answer)

print(ps.checkAnswer(element_nr, answer))
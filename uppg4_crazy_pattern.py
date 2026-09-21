"""
Alla kommandon för turtle finns i filen kommandon.md

Använd en for-loop för att göra ett mönster med turtle.

Minimikrav:
- Använd minst 50 varv i din for-loop.
- Förändra minst två egenskaper under loopen, till exempel riktning, färg,
  pennstorlek eller längden på turtle-stegen.
- Mönstret ska innehålla något som upprepas och förändras.

Du får gärna använda slump för att göra mönstret mer oförutsägbart.

Exempel på en loop:
for i in range(50):
	padda.forward(100)
	padda.right(91)
"""
import turtle
import random

# Skapa en turtle
padda = turtle.Turtle()

# Exempel: Lista med färger att välja från
farger = ["red", "blue", "green", "yellow", "purple", "orange"]
padda.pencolor(random.choice(farger))  # Slumpar en färg från listan
padda.pensize(random.randint(1, 10))   # Slumpar pennans storlek mellan 1 och 10


turtle.done()
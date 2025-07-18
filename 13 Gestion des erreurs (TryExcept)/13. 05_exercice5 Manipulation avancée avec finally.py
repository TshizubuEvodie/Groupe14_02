import math 
try: 
x = float(input("Entrez un nombre : ")) 
if X< 0: 
raise valueError("Nombre négatif, pas de racine réelle.") 
racine= math.sqrt(x) 
except ValueError as e: 
print(f"Erreur {e}") 
else: 
print(f"Racine carrée {racine}") 
finally: 
print("Fin du calcul.")
import random

fragments = [
    "voix basse", "lumière tamisée", "bruit de fond familier", "souvenir flou", "image récurrente", "pression légère"
]

memory_latente = []
seuil_resonance = 3

for i in range(15):
    fragment = random.choice(fragments)
    memory_latente.append(fragment)
    print(f"Ajouté : {fragment}")

    if memory_latente.count(fragment) >= seuil_resonance:
        print(f"→ Décision intuitive : {fragment.upper()}")
        break

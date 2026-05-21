#hi
print(SEP + "ÚLOHA 1 – Borůvky" + SEP)
 
cena1_kg = 150 / 0.65   # Prodejce 1: Kč/kg
cena2_kg = 120 / 0.50   # Prodejce 2: Kč/kg
 
print(f"Prodejce 1: {cena1_kg:.4f} Kč/kg")
print(f"Prodejce 2: {cena2_kg:.4f} Kč/kg")
 
if cena1_kg < cena2_kg:
    levnejsi, drazsi = cena1_kg, cena2_kg
    print("→ Levnější je Prodejce 1")
else:
    levnejsi, drazsi = cena2_kg, cena1_kg
    print("→ Levnější je Prodejce 2")
 
hmotnost = 600 / levnejsi
vysledek_1 = hmotnost * drazsi
 
print(f"\nZa 600 Kč nakoupená hmotnost: {hmotnost:.4f} kg")
print(f"VÝSLEDEK: U dražšího prodejce by zaplatil {vysledek_1:.2f} Kč")

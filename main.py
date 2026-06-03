"""
  MATURITA Z MATEMATIKY
  Úlohy: 1, 2, 8, 9, 11, 15, 22
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

SEP = "\n" + "-"*60 + "\n"

# ÚLOHA 1 – Základní výpočet: Borůvky
# Zjistím cenu za kg u obou prodejců, určím
# levnějšího, z jeho ceny spočítám nakoupené množství a
# přepočítám na cenu u dražšího prodejce.
#
# zápis:
#   Prodejce 1: 150 Kč / 0,65 kg   cena/kg
#   Prodejce 2: 120 Kč / 0,50 kg  cena/kg
#   hmotnost = 600 / cena_levnějšího
#   výsledek  = hmotnost * cena_dražšího

print(SEP + "ÚLOHA 1 – Borůvky" + SEP)

cena1_kg = 150 / 0.65   # Prodejce 1: Kč/kg
cena2_kg = 120 / 0.50   # Prodejce 2: Kč/kg

print(f"Prodejce 1: {cena1_kg:.4f} Kč/kg")
print(f"Prodejce 2: {cena2_kg:.4f} Kč/kg")

if cena1_kg < cena2_kg:
    levnejsi, drazsi = cena1_kg, cena2_kg
    print(" Levnější je Prodejce 1")
else:
    levnejsi, drazsi = cena2_kg, cena1_kg
    print(" Levnější je Prodejce 2")

hmotnost = 600 / levnejsi
vysledek_1 = hmotnost * drazsi

print(f"\nZa 600 Kč nakoupená hmotnost: {hmotnost:.4f} kg")
print(f"VÝSLEDEK: U dražšího prodejce by zaplatil {vysledek_1:.2f} Kč")
# Interpretace: Prodejce 1 je levnější (230,77 Kč/kg vs 240 Kč/kg).
# Za 600 Kč koupí 2,6 kg, tatáž hmotnost u Prodejce 2 vychází na 624 Kč.


# 
# ÚLOHA 2 – Algebra: Vyjádření délky kyvadla l
# Z rovnice T = 2pi odmz(l/g) algebraicky isolujeme l –
# umocníme obě strany a upravíme.
#
# Matematický zápis:
#   T**2 = 4pi**2 * (l/g)
#   l  = T**2*g / (4pi**2)

print(SEP + "ÚLOHA 2 – Délka kyvadla" + SEP)

T, l, g = sp.symbols('T l g', positive=True)

rovnice = sp.Eq(T, 2 * sp.pi * sp.sqrt(l / g))
print(f"Původní rovnice: {rovnice}")

reseni_l = sp.solve(rovnice, l)[0]
print(f"VÝSLEDEK: l = {reseni_l}")
# Interpretace: Delší kyvadlo kmitá pomaleji (větší T) 

# ÚLOHA 8 – Rovnice: Průměrný plat seniorů
# Označíme průměrný plat juniorů jako x, seniorů jako x+6000.
# Celkový průměr je vážený průměr (1/3 seniorů, 2/3 juniorů) = 46 200.
#
# Matematický zápis:
#   (1/3)*(x + 6000) + (2/3)*x = 46 200
#   x/3 + 2000 + 2x/3 = 46 200
#   x = 44 200
#   senior = x + 6000 = 50 200

print(SEP + "ÚLOHA 8 – Průměrný plat seniorů" + SEP)

x = sp.Symbol('x')   # průměrný plat juniorů

rovnice_8 = sp.Eq(
    sp.Rational(1, 3) * (x + 6000) + sp.Rational(2, 3) * x,
    46200
)
print(f"Rovnice: {rovnice_8}")

plat_junioru = sp.solve(rovnice_8, x)[0]
plat_senioru = plat_junioru + 6000

print(f"\nPrůměrný plat juniorů:  {plat_junioru} Kč")
print(f"VÝSLEDEK: Průměrný plat seniorů = {plat_senioru} Kč")


# Interpretace: Vážený průměr (1/3 seniorů + 2/3 juniorů) musí dát 46 200.
# Senioři vydělávají 50 200 Kč, junioři 44 200 Kč.

# ÚLOHA 9 – Funkce a graf: Kvadratická + lineární funkce
#f(x) = x**2/2 - 2. Graf lineární funkce g protíná f
# ve dvou bodech A[4; a**2] a B[0; b**2]. Dosadíme x=4 a x=0 do f,
# pak sestavíme předpis g procházející A a B.
#
# Matematický zápis:
#   f(4) = 8 - 2 = 6  -> A = [4, 6]
#   f(0) = 0 - 2 = -2 -> B = [0, -2]
#   g(x) = směrnice*x + b  (přímka přes A a B)

print(SEP + "ÚLOHA 9 – Kvadratická a lineární funkce" + SEP)

xv = sp.Symbol('x')
f9 = sp.Rational(1, 2) * xv**2 - 2

# Souřadnice průsečíků
yA = f9.subs(xv, 4)
yB = f9.subs(xv, 0)
print(f"A = [4, {yA}]")
print(f"B = [0, {yB}]")

# Předpis lineární funkce g přes A[4,6] a B[0,-2]
smernice = (yA - yB) / (4 - 0)
posun    = yB   # průsečík s osou y = yB (x=0)
print(f"\nSměrnice g: ({yA} - ({yB})) / (4 - 0) = {smernice}")
print(f"VÝSLEDEK: g(x) = {smernice}x + ({posun})  ->  g(x) = {smernice}x - 2")

# Graf
x_vals = np.linspace(-4, 6, 400)
f_vals = 0.5 * x_vals**2 - 2
g_vals = float(smernice) * x_vals + float(posun)
 
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x_vals, f_vals, 'b-',  linewidth=2, label=r'$f(x)=\frac{1}{2}x^2-2$')
ax.plot(x_vals, g_vals, 'r--', linewidth=2, label=f'$g(x)={smernice}x-2$')
ax.plot(4, float(yA), 'go', markersize=9, zorder=5, label=f'A[4, {yA}]')
ax.plot(0, float(yB), 'ms', markersize=9, zorder=5, label=f'B[0, {yB}]')
ax.axhline(0, color='k', linewidth=0.7)
ax.axvline(0, color='k', linewidth=0.7)
ax.set_xlabel('x'); ax.set_ylabel('y')
ax.set_title('Úloha 9 – Graf f a lineární funkce g')
ax.legend(); ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('./uloh9_graf.png', dpi=120)
print("Graf uložen: uloh9_graf.png")
# Interpretace: g protíná f ve dvou bodech, jedním je vrchol úsečky B
# na ose y. Směrnice g = 2 udává strmost přímky.
 
 
# ÚLOHA 11 – Geometrie: Rovnoběžné přímky, vzdálenost
# q je rovnoběžná s p (stejný normálový vektor),
# jen jiná konstanta. Dosadíme Q[1,0] a určíme konstantu.
# Vzdálenost rovnoběžných přímek ax+by+c=0 a ax+by+d=0:
#   dist = |c - d| / odmz(a**2+b**2)
#
# Matematický zápis:
#   p: x + 2y + 4 = 0
#   q: x + 2y + c = 0, dosadíme Q[1,0]: 1 + 0 + c = 0 -> c = -1
#   dist = |4 - (-1)| / odmz(1**2+2**2) = 5/odmz5 = odmz5
 
print(SEP + "ÚLOHA 11 – Rovnoběžné přímky" + SEP)
 
# Přímka p: x + 2y + 4 = 0  (koeficienty a=1, b=2, c_p=4)
a_koef, b_koef, c_p = 1, 2, 4
 
# q prochází Q[1,0] a je rovnoběžná s p -> stejné a,b
Qx, Qy = 1, 0
c_q = -(a_koef * Qx + b_koef * Qy)
print(f"Přímka p: {a_koef}x + {b_koef}y + {c_p} = 0")
print(f"Přímka q prochází Q[{Qx},{Qy}]: c = -({a_koef}*{Qx} + {b_koef}*{Qy}) = {c_q}")
print(f"Rovnice q: {a_koef}x + {b_koef}y + ({c_q}) = 0  ->  x + 2y - 1 = 0")
 
# Vzdálenost
vzdalenost = abs(c_p - c_q) / sp.sqrt(a_koef**2 + b_koef**2)
print(f"\nVzdálenost = |{c_p} - ({c_q})| / odmz({a_koef}**2+{b_koef}**2)")
print(f"= {abs(c_p - c_q)} / √{a_koef**2 + b_koef**2}")
print(f"VÝSLEDEK: d = {vzdalenost} = {sp.simplify(vzdalenost)} přibližně {float(vzdalenost):.4f}")
# Interpretace: q má rovnici x + 2y - 1 = 0. Vzdálenost přímek
# je odmz5 přibližně 2,236. 

# ÚLOHA 15 – Pravděpodobnost: Dvě kostky
# Vypíšeme celý výběrový prostor (6*8 = 48 výsledků),
# spočítáme příznivé případy pro jevy X, Y, Z.
#
# Matematický zápis:
#   X: obě čísla lichá -> P(X) = (počet lichých na k1) * (počet lichých na k2) / 48
#   Y: součet lichý -> (lichá+sudá) nebo (sudá+lichá)
#   Z: součet sudýn-> (lichá+lichá) nebo (sudá+sudá)
# ============================================================
 
print(SEP + "ÚLOHA 15 – Pravděpodobnost, dvě kostky" + SEP)
 
# Výběrový prostor
k1 = list(range(1, 7))   # šestistěnná
k2 = list(range(1, 9))   # osmistěnná
omega = [(a, b) for a in k1 for b in k2]
n = len(omega)
print(f"Velikost výběrového prostoru omega: {n}")
 
# Jev X: obě liché
X = [(a, b) for a, b in omega if a % 2 == 1 and b % 2 == 1]
P_X = len(X) / n
print(f"\nJev X (obě liché): {len(X)} příznivých")
print(f"P(X) = {len(X)}/{n} = {sp.Rational(len(X), n)} = {P_X:.4f}")
print(f"15.1 P(X) = 0,25? -> {'A (pravda)' if abs(P_X - 0.25) < 1e-9 else 'N (nepravda)'}")
 
# Jev Y: součet lichý
Y = [(a, b) for a, b in omega if (a + b) % 2 == 1]
P_Y = len(Y) / n
print(f"\nJev Y (součet lichý): {len(Y)} příznivých")
print(f"P(Y) = {len(Y)}/{n} = {sp.Rational(len(Y), n)} = {P_Y:.4f}")
print(f"15.2 P(Y) = P(X)? -> {'A (pravda)' if abs(P_Y - P_X) < 1e-9 else 'N (nepravda)'}")
 
# Jev Z: součet sudý
Z = [(a, b) for a, b in omega if (a + b) % 2 == 0]
P_Z = len(Z) / n
print(f"\nJev Z (součet sudý): {len(Z)} příznivých")
print(f"P(Z) = {len(Z)}/{n} = {sp.Rational(len(Z), n)} = {P_Z:.4f}")
print(f"15.3 P(Z) > P(Y)? -> {'A (pravda)' if P_Z > P_Y else 'N (nepravda)'}")
 
print(f"\nVÝSLEDKY: 15.1 = A,  15.2 = N,  15.3 = A")
# Interpretace: Na šestistěnné kostce jsou 3 lichá čísla (z 6),
# na osmistěnné 4 lichá (z 8). 
 
# ÚLOHA 22 – Posloupnost: Dekorační pavučina
#  Délky vláken tvoří aritmetickou posloupnost.
# a1 = 24 cm, d = 0,4 cm (4 mm), an = 200 cm.
# Počet členů: n = (an - a1)/d + 1
#
# Matematický zápis:
#   an = a1 + (n-1)*d
#   200 = 24 + (n-1)*0,4
#   n-1 = 176/0,4 = 440
#   n = 441
 
print(SEP + "ÚLOHA 22 – Aritmetická posloupnost, pavučina" + SEP)
 
a1  = 24      # cm – nejkratší vlákno
d   = 0.4     # cm – rozdíl (4 mm = 0,4 cm)
an  = 200     # cm – nejdelší vlákno (2 m = 200 cm)
 
n_vlaket = (an - a1) / d + 1
print(f"a1 = {a1} cm,  d = {d} cm,  an = {an} cm")
print(f"n = (an - a1) / d + 1 = ({an} - {a1}) / {d} + 1 = {n_vlaket:.0f}")
 
# Přesné řešení přes sympy
n_sym = sp.Symbol('n', positive=True)
rovnice_22 = sp.Eq(a1 + (n_sym - 1) * sp.Rational(2, 5), 200)
reseni_n = sp.solve(rovnice_22, n_sym)[0]

 
print(f"\n VÝSLEDEK: n = {int(n_vlaket)} vláken")
print(f"   Odpověď v testu: méně než 450 vláken -> volba A)")
 
# Interpretace: 441 vláken, délky tvoří aritmetickou posloupnost
# od 24 cm do 200 cm s krokem 0,4 cm. 441 < 450 -> odpověď A.
 
 
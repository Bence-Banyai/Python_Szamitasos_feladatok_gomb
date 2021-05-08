import math


def gomb_felszin(r: float):
    return 4*math.pi*r**2


def gomb_terfogat(r: float):
    return (4*math.pi*r**3)/3


print('Gömb felszín és térfogat számítása')
r = float(input('Adja meg a sugarat:'))
if r > 0:
    print('A felszín:', gomb_felszin(r))
    print('A térfogat:', gomb_terfogat(r))
else:
    print('Hiba: rossz adat!')

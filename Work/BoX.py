def box(phome, paway, length = 3):
    if phome > 1 and paway > 1:
        phome = 1/phome
        paway = 1/paway
    if length == 3:
        series_h = phome ** 2 + 2 * (1 - phome) * phome**2
        series_a = 1 - series_h
    if length == 5:
        series_h = phome**3 + 2*(1 - phome)*phome**3 + 4*((1-phome)**2)*phome**3
        series_a = 1 - series_h

    return 1/series_h, 1/series_a


print(box(0.65, 0.35, length = 5))

# Este programa te dice si el año que indicás es bisiesto o no.

año = int(input("Introduzca un año: "))

if año>1582:
    if año % 4 == 0 & año % 100 == 0 & año % 400 == 0:
        tipoAño= 'bisiesto'
        print('Año ', tipoAño)
    elif año % 4 == 0 & año % 100 == 0 & año % 400 != 0:
        tipoAño= 'común'
        print('Año ', tipoAño)
    elif año % 4 == 0 & año % 100 != 0:
        tipoAño= 'bisiesto'
        print('Año ', tipoAño)
    else:
        tipoAño= 'común'
        print('Año ', tipoAño)
else:
    tipoAño= 'No dentro del período del calendario gregoriano'
    print(tipoAño)


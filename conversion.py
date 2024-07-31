import sys

if len(sys.argv) != 5:
    print ("Uso: python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar> <monto_chileno>")
    sys.exit(1)

tcsol = float(sys.argv[1])
tcpesoarg = float(sys.argv[2])
tcdolar = float(sys.argv[3])
clp = float(sys.argv[4])

convsol = tcsol * clp
convpesoarg = tcpesoarg * clp
convdolar = tcdolar * clp

print (f'\nLos CLP${clp:.0f} corresponden a:\n')
print (f'ARG $ {convsol:.1f} (Pesos Argentinos)')
print (f'SOL $ {convpesoarg:.1f} (Soles Peruanos)')
print (f'USD $ {convdolar:.1f} (Dolares Americanos)\n')
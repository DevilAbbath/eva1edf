recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

# 1. Agregar un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
newevent = ['2021-02-02', '06:00', 'Empezar el Año']
recordatorios.append(newevent)

# 2. Editar de tal manera que el 15 de Julio sea el 16 de Julio.
for event in recordatorios:
    if event[0] == '2021-07-15':
        event[0] = '2021-07-16'

# 3. Eliminar el evento del día del trabajo.
recordatorios = [event for event in recordatorios if event[0] != '2021-05-01']

# 4. Agregar una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Ordenar los eventos por fecha y hora
recordatorios.sort()

# Imprimir los recordatorios ordenados
for event in recordatorios:
    print(event)
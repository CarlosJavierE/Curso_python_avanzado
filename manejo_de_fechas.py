# import datetime

# my_time = datetime.datetime.now()

# print(my_time)

# esto me trae la fechas y horas en UTC si es que no hay fecha
# los servidores no tienen fecha
# pero la pc tiene fecha y hora, trae la de la pc

# my_day = datetime.date.today()  # esto solo saca la fecha
# print(my_day)
# print() # con el metodo today se puede sacar individualmente
# print(f"Year: {my_day.year}")
# print(f"Month: {my_day.month}")
# print(f"Day: {my_day.day}")


# Formateo de fechas
# mm/dd/yyyy    Usa
# dd/mm/yyyy    Latam

# Año ->	%Y
# Mes ->	%m
# Día ->	%d
# Hora ->	%H
# Minutos ->	%M
# Segundos ->	%S


from datetime import datetime
# asi se deberia importar una clase de un modulo

my_datetime = datetime.now()
print(my_datetime)

latam = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {latam}')

usa = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {usa}')

random_format = my_datetime.strftime('año %Y mes %m día %d')
print(f'Formato random: {random_format}')

formato_utc = datetime.utcnow()
print(f'Formato UTC: {formato_utc}')
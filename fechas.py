from datetime import datetime

ahora = datetime.now()
print(ahora.year)  # Año actual

print(ahora.strftime('%A'))  # Día actual 

fecha = datetime(2009, 7, 9)
print(fecha.strftime('%B'))  #  mes de la fecha

str_fecha = '07/04/09 07:21:00'
fecha_obj = datetime.strptime(str_fecha, '%d/%m/%y %H:%M:%S')
print(fecha_obj)  



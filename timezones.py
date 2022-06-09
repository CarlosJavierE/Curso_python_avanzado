from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print(f"Bogota: {bogota_date.strftime('%d/%m/%Y, %H:%M:%S')}")
# esto me saca la hora de bogota con el formato que yo le di


mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print(f"Mexico: {mexico_date.strftime('%d/%m/%Y, %H:%M:%S')}")

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print(f"Caracas: {caracas_date.strftime('%d/%m/%Y, %H:%M:%S')}")

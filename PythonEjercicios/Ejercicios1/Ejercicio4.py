import datetime
"""Fecha y hora actual:
Muestra la fecha y hora actuales con datetime.datetime.now().
Cálculo de edad:
Pide al usuario su año de nacimiento y calcula su edad actual usando datetime.date.today().year.
Días restantes del año:
Calcula cuántos días faltan para que termine el año con datetime.date.today() y
datetime.date.replace().
"""
if(__name__=="__main__"):

    fechaHoraHoy=datetime.datetime.now()
    print(f"La fecha de hoy es {fechaHoraHoy}")

    añoNacimiento=int(input("¿En que año nacio?"))
    edadActual=(datetime.date.today().year-añoNacimiento)
    print(f"Usted tiene {edadActual} años")

    fechaHoy=datetime.date.today()
    fechaFinal=fechaHoy.replace(month=12, day=31)
    fechaRestantes=(fechaFinal-fechaHoy)
    diasRestantes=fechaRestantes.days
    print(f"Quedan {diasRestantes} dias para que termine el año")

    
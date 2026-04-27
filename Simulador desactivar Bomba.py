# =========================================================
# PROYECTO: CODE-DEFUSER 1.0
# AUTOR: GabrielG320
# =========================================================
# DESCRIPCIÓN: Simulador de cuenta regresiva con trigger de seguridad.
# 
# LO QUE APRENDÍ Y DESAFÍOS:
# 1. Control de Tiempos: Entendí cómo hacer que un número baje (n = n - 1) 
#    sin que el programa se cuelgue o baje de cero.
# 2. El reto del "Disparador": Al principio la bomba explotaba sola, 
#    tuve que aprender a poner un "if" de confirmación antes del bucle.
# 3. Flujo Lógico: Aprendí a usar el input para pausar la ejecución 
#    hasta que el usuario esté listo.
#
# TIEMPO DE DESARROLLO: Unos 30 minutos de pelearme con el orden del bucle.
# =========================================================

solucion = "777"
intentos = 4

while intentos > 0:
    intento = input(f"Te quedan {intentos}, introduce la clave: ")
    
    if intento != solucion:
        intentos = intentos - 1
        print("Clave incorrecta")

    else:
        print("¡BOMBA DESACTIVADA!")
        break 

if intentos == 0:
    print("BOOM! Te quedaste sin intentos")
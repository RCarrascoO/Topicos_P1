# CALCULADORA BINARIA - MAT1184
# Autor: Renato Carrasco


# Función para verificar entrada numérica
def verificar_numero(mensaje_para_usuario):
    while True:
        valor_ingresado = input(mensaje_para_usuario)
        try:
            numero_verificado = float(valor_ingresado) if '.' in valor_ingresado else int(valor_ingresado)
            return numero_verificado
        except:
            print("¡Error! Por favor, ingrese un valor numérico válido (ej: 7 o 4.2).")

# Conversor decimal-binario (incluyendo parte fraccionaria)
def convertir_decimal_a_binario(valor_decimal):
    parte_entera = int(abs(valor_decimal))
    parte_fraccionaria = abs(valor_decimal) - parte_entera

    binario_entero = ""
    if parte_entera == 0:
        binario_entero = "0"
    else:
        while parte_entera > 0:
            binario_entero = str(parte_entera % 2) + binario_entero
            parte_entera = parte_entera // 2
    
    # Parte fraccionaria (Basandose en 4 bits, modificable)
    binario_fraccion = ""
    for _ in range(4):
        parte_fraccionaria *= 2
        bit = int(parte_fraccionaria)
        binario_fraccion += str(bit)
        parte_fraccionaria -= bit
    
    signo = "-" if valor_decimal < 0 else ""
    return f"{signo}{binario_entero}.{binario_fraccion}"

# Operaciones binarias (implementadas manualmente)
def operar_suma(binario_a, binario_b):
    longitud_max = max(len(binario_a), len(binario_b))
    binario_a = binario_a.zfill(longitud_max)
    binario_b = binario_b.zfill(longitud_max)
    resultado = []
    acarreo = 0
    
    for i in range(longitud_max - 1, -1, -1):
        suma_bit = acarreo
        suma_bit += 1 if binario_a[i] == '1' else 0
        suma_bit += 1 if binario_b[i] == '1' else 0
        resultado.append('1' if suma_bit % 2 else '0')
        acarreo = 1 if suma_bit > 1 else 0
    
    if acarreo:
        resultado.append('1')
    
    return ''.join(reversed(resultado))

def operar_resta(binario_a, binario_b):
    # Implementación básica (puedes mejorarla)
    decimal_a = int(binario_a, 2)
    decimal_b = int(binario_b, 2)
    return bin(decimal_a - decimal_b)[2:]

def operar_multiplicacion(binario_a, binario_b):
    # Implementación básica (puedes mejorarla)
    resultado = 0
    for i, bit in enumerate(reversed(binario_b)):
        if bit == '1':
            resultado += int(binario_a, 2) << i
    return bin(resultado)[2:]

# Menú de operaciones
def mostrar_opciones():
    print("\nOpciones disponibles:")
    print("[1] Realizar suma")
    print("[2] Realizar resta")
    print("[3] Realizar multiplicación")
    
    while True:
        eleccion = input("Seleccione una opción (1-3): ")
        if eleccion in {'1', '2', '3'}:
            return eleccion
        print("Opción no reconocida. Intente nuevamente.")

# Programa principal
def ejecutar_programa():
    print("\n" + "="*40)
    print("   CALCULADORA BINARIA AVANZADA")
    print("="*40)
    
    while True:
        # Entrada de datos
        primer_num = verificar_numero("Ingrese el primer número: ")
        segundo_num = verificar_numero("Ingrese el segundo número: ")
        
        # Conversión
        binario_1 = convertir_decimal_a_binario(primer_num)
        binario_2 = convertir_decimal_a_binario(segundo_num)
        print(f"\nPrimer número en binario:  {binario_1}")
        print(f"Segundo número en binario: {binario_2}")
        
        # Operación
        opcion = mostrar_opciones()
        binario_1_sin_punto = binario_1.replace('.', '')
        binario_2_sin_punto = binario_2.replace('.', '')
        
        if opcion == '1':
            resultado_bin = operar_suma(binario_1_sin_punto, binario_2_sin_punto)
        elif opcion == '2':
            resultado_bin = operar_resta(binario_1_sin_punto, binario_2_sin_punto)
        elif opcion == '3':
            resultado_bin = operar_multiplicacion(binario_1_sin_punto, binario_2_sin_punto)
        
        # Resultados
        print("\n" + "-"*30)
        print(f"Resultado en binario:  {resultado_bin}")
        print(f"Resultado en decimal: {int(resultado_bin, 2)}")
        print("-"*30)
        
        # Repetir
        continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("\n¡Gracias por usar la calculadora!")
            break

# Punto de entrada
if __name__ == "__main__":
    ejecutar_programa()
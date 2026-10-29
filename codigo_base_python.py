def analizar_token(cadena):
	cadena = cadena.strip()
	if not cadena:
		return "Cadena vacía"
	estado = 0
	i = 0
	operadores = {'+','-','*','/','=','<','>','%'}
	palabras_reservadas = {'int', 'float', 'double', 'char', 'bool', 'if', 'else', 'while', 'for', 'return', 'void'}

	while i < len(cadena):
		c = cadena[i]
		if estado == 0:
			if c.isalpha() or c == '_':
				estado = 1 # Estado para Identificador / Palabra Reservada
			elif c.isdigit():
				estado = 2 # Estado para Número (Entero)
			elif c in operadores:
				estado = 4 # Estado para Operador
			elif c == '"':
				estado = 5 # Estado para inicio de Cadena de Texto
			else:
				return "No válido / Desconocido"
		elif estado == 1: # Procesando Identificador
			if not (c.isalnum() or c == '_'):
				return "Identificador no válido"
		elif estado == 2: # Procesando Número
			if c == '.':
				estado = 3 # Transición a número decimal
			elif not c.isdigit():
				return "Número no válido"
		elif estado == 3: # Procesando parte decimal
			if not c.isdigit():
				return "Número decimal no válido"
		elif estado == 4: # Procesando Operador
			return "Operador no válido (demasiados caracteres)"
		elif estado == 5: # Agregado: Procesando Cadena de Texto
			pass

		i += 1

		# Clasificación final según el estado en el que terminó
	if estado == 1:
	# comprueba si el identificador coincide con una palabra reservada
		if cadena in palabras_reservadas:
			return f"Palabra reservada: {cadena}"
		return "Identificador válido"
	elif estado in (2, 3):
		return "Número válido"
	elif estado == 4:
		return "Operador válido"
	elif estado == 5: # Agregado: Validación final para cadena de texto
		if cadena.startswith('"') and cadena.endswith('"') and len(cadena) >= 2:
			return "Cadena de texto válida"
		return "Cadena de texto no válida"
	
	return "Cadena no válida"


# --- Pruebas ---
entradas = ["variable1", "int", "125", "45.67", "++", "\"Hola Mundo\"", "\"Cadena de caracteres"]

for e in entradas:
	print(f"'{e}' -> {analizar_token(e)}")

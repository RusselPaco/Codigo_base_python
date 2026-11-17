# TOKENS
# def 10
# VARIABLE 1000
# ( 80
# ) 85
# , 50
# : 55
# NEWLINE 300
# INDENT 301
# DEDENT 302
def ini(tokens):

    i = 0

    i, error = funcion(tokens, i)

    if error != '':
        return error

    if i == len(tokens):
        return 'VALIDO'
    else:
        return 'ERROR: SE ENCONTRO UN TOKEN INESPERADO'
def funcion(tokens, i):

    if i < len(tokens) and tokens[i] == 10:
        i += 1
    else:
        return i, 'ERROR: SE ESPERABA LA PALABRA "def"'

    if i < len(tokens) and tokens[i] == 1000:
        i += 1
    else:
        return i, 'ERROR: SE ESPERABA EL NOMBRE DE LA FUNCION'
    i, error = parametros(tokens, i)

    if error != '':
        return i, error
    if i < len(tokens) and tokens[i] == 55:
        i += 1
    else:
        return i, 'ERROR: SE ESPERABA ":" DESPUES DE LOS PARAMETROS'

    i, error = cuerpo(tokens, i)

    if error != '':
        return i, error

    return i, ''
def parametros(tokens, i):
    if i < len(tokens) and tokens[i] == 80:
        i += 1
    else:
        return i, 'ERROR: SE ESPERABA ABRIR "("'
    if i < len(tokens) and tokens[i] == 1000:

        i, error = parameter(tokens, i)

        if error != '':
            return i, error
    while i < len(tokens) and tokens[i] == 50:

        i += 1

        i, error = parameter(tokens, i)

        if error != '':
            return i, error

    if i < len(tokens) and tokens[i] == 85:
        i += 1
    else:
        return i, 'ERROR: SE ESPERABA CERRAR ")"'

    return i, ''
def parameter(tokens, i):

    if i < len(tokens) and tokens[i] == 1000:
        i += 1
    else:
        return i, 'ERROR: SE ESPERABA UN PARAMETRO'

    return i, ''

def cuerpo(tokens, i):

    if i < len(tokens) and tokens[i] == 300:

        i += 1
        if i < len(tokens) and tokens[i] == 301:
            i += 1
        else:
            return i, 'ERROR: SE ESPERABA INDENT'

        if i >= len(tokens) or tokens[i] == 302:
            return i, 'ERROR: EL CUERPO DE LA FUNCION NO PUEDE ESTAR VACIO'

        i , error = statement(tokens, i)

        if error != '':
            return i, error
        while i < len(tokens) and tokens[i] == 300:
            i += 1
            if i < len(tokens) and tokens[i] == 302:
                break
            i, error = statement(tokens, i)
            if error != '':
                return i, error
        if i < len(tokens) and tokens[i] == 302:
            i += 1
        else:
            return i, 'ERROR: SE ESPERABA DEDENT'
    else:
        i, error = simple_stmt(tokens, i)
        if error != '':
            return i, error
        if i < len(tokens) and tokens[i] == 300:
            i += 1
    return i, ''
def simple_stmt(tokens, i):
    inicio = i
    while i < len(tokens) and tokens[i] != 300:
        i += 1
    if i == inicio:
        return i, 'ERROR: SE ESPERABA UNA INSTRUCCION'
    return i, ''
def statement(tokens, i):
    inicio = i
    while i < len(tokens) and tokens[i] not in (300, 302):
        i += 1

    if i == inicio:
        return i, 'ERROR: SE ESPERABA UNA INSTRUCCION'

    return i, ''
tokens = [
10, 1000, 80, 1000, 50, 1000, 85, 55,
300, 301,
1000, 65, 1000, 100, 1000,
300,
20, 80, 1000, 85,
300, 302
]

print(ini(tokens))
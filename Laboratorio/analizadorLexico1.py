def ini (tokens):
    i=0
    i,error = expresion_logica(tokens,i)
    if error != '':
        return error
    if i == len(tokens):
        return 'VALIDO'
    else:
        return 'ERROR EN AL EJECUCION'
    

def expresion_logica(tokens,i):
    i,error =termino(tokens,i)
    if error != '':
        return error
    while i<len(tokens) and tokens[i]==300:
        i=i+1
        i,error =termino(tokens,i)
        if error != '':
            return error
    return i,''
def termino(tokens,i):
    i, error =factor(tokens,i)
    if error != '':
        return error
    while i<len(tokens) and tokens[i]==301:
         i=i+1
         i,error =termino(tokens,i)
         if error != '':
          return error
    return i,''
def factor(tokens,i):
    if i<len(tokens) and tokens[i] == 302:
    
         i=i+1
         i,error =termino(tokens,i)
         if error != '':
            return error
    elif i<len(tokens) and tokens[i] == 80:
        i=i+1
        i,error = expresion_logica(tokens,i)
        if error != '':
            return error
        if i<len(tokens) and tokens[i] == 85:
            i=i+1
        else:
            return i, 'ERROR: SE ESPERABA CERRAR ")"'
    elif i<len(tokens) and tokens[i] in (303,304):
        i=i+1
    else:
        return i,'ERROR SE ESPERABA NOT,TRUE,FALSE O "("'
    return i,''

tokens= [302,80,303,300,304,85,301,303]
print(ini(tokens))

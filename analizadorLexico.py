if token in ["PRINT"]:
    match("PRINT")
    match("LPAREN")
    if token in ["NUM", "ID"]:
        traducir_expresion()
    elif token in ["CADENA"]:
        traducir_cad()
    else:
        error()

    while token in ["SEMICOLON"]:
        match("SEMICOLON")
    if token in ["NUM", "ID"]:
        traducir_expresion()
    elif token in ["CADENA"]:
        traducir_cad()
    else:
        error()

    match("RPAREN")
else:
    error()
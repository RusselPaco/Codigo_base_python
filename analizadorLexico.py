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
if token in ["SCAN"]:
    match("SCAN")
    match("LPAREN")

    if token in ["LETRA"]:
        traducir_letra()
    else:
        error()

    while token in ["LETRA", "DIGITO"]:
        if token in ["LETRA"]:
            traducir_letra()
        else:
            traducir_digito()

    match("RPAREN")
else:
    error()
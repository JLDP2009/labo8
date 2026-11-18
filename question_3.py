def minutos_por_usuario(reproducciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - minutos totales de cada usuario
    """
    # Tu codigo empieza aquí. Recuerda eliminar el `pass`
    resultado = {}

    for repro in reproducciones:
        usuario = repro["usuario"]
        minutos = repro["minutos"]

        if usuario not in resultado:
            resultado[usuario] = 0

        resultado[usuario] += minutos

    return resultado

def artistas_por_usuario(reproducciones: list) -> dict:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        dict: diccionario con el par nombre - lista de los artistas de cada usuario
    """
    # Tu codigo empieza aquí. Recuerda eliminar el `pass`
    resultado = {}

    for repro in reproducciones:
        usuario = repro["usuario"]
        artista = repro["artista"]

        if usuario not in resultado:
            resultado[usuario] = []

        if artista not in resultado[usuario]:
            resultado[usuario].append(artista)

    return resultado

def usuario_mas_activo(reproducciones: list) -> str:
    """
    Input:
        list: list de diccionarios con el usuario, artista y minutos
    Output:
        str: nombre del usuario con más minutos
    """
    # Tu codigo empieza aquí. Recuerda eliminar el `pass`
    totales = minutos_por_usuario(reproducciones)

    usuario_max = None
    max_minutos = -1

    for usuario, minutos in totales.items():
        if minutos > max_minutos:
            max_minutos = minutos
            usuario_max = usuario

    return usuario_max


if __name__ == "__main__":
    reproducciones = [
        {"usuario" : "sofia" , "artista" : "Wolf Alice"   , "minutos" : 60 },
        {"usuario" : "daniel", "artista" : "Milo J"       , "minutos" : 30 },
        {"usuario" : "sofia" , "artista" : "Fleetwood Mac", "minutos" : 42 },
        {"usuario" : "carlos", "artista" : "Americania"   , "minutos" : 21 },
        {"usuario" : "elena" , "artista" : "Tame Impala"  , "minutos" : 25 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 56 },
        {"usuario" : "sofia" , "artista" : "MGMT"         , "minutos" : 43 },
        {"usuario" : "carlos", "artista" : "Dua Lipa"     , "minutos" : 20 }
    ]

    #print(minutos_por_usuario(reproducciones))  # -> {“sofia” : 145, “daniel” : 30, “carlos” : 97, “elena” : 25} 
    #print(artistas_por_usuario(reproducciones)) # -> {“sofia” : [“Wolf ALice”, “Fleetwood Mac”, MGMT],  
    #                                            #     “daniel” : [“Milo J”],  
    #                                            #     “carlos” : [“Americania”, “Dua Lipa”],  
    #                                            #     “elena”  : [“Tame Impala”]} 
    #print(usuario_mas_activo(reproducciones))   # -> sofia
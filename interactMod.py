import sys

from inst import BadIntruction, ejecutarIntruccion


def modoInteractivo():
    try:
        variables = {}
        print("""
Bienvenide a simpleDeDllang, lenguaje no serio hecho por una estudiante de la UCA harta de modelo GOTO.
Es tecnicamente Touring Completo, o eso creo, nadie va a revisar esto.
Modo interactivo:
""")
        while True:
            print(">>> ", flush=True, end="")
            linea = input().strip()
            try:
                if linea.endswith(";"):
                    ejecutarIntruccion(0, linea[:-1], variables, interactivo=True)
                else:
                    ejecutarIntruccion(0, linea, variables, interactivo=True)
                    print(variables)
            except BadIntruction as bd:
                print(
                    f"Intrucción no valida: {bd.args[0] if len(bd.args) == 1 else bd.args[1]}",
                    file=sys.__stderr__,
                )

    except KeyboardInterrupt as _:
        pass

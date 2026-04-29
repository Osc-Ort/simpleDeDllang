import sys
from pathlib import Path

from inst import ejecucionIntrucciones
from interactMod import modoInteractivo


def main():
    argv = sys.argv[1:]
    if not argv:
        modoInteractivo()
    else:
        # Ejecución de archivos
        textos = []
        for arch in argv:
            try:
                data = list(Path(arch).read_text().splitlines())
                for data_t in data:
                    data_t = data_t.strip()
                    if data_t:
                        for inf in data_t.split(";"):
                            textos.append(inf)
            except FileNotFoundError as _:
                print(f"Archivo no existente: {arch}", file=sys.__stderr__)
        # La ejecución de cada instrucción
        ejecucionIntrucciones(textos)


if __name__ == "__main__":
    main()

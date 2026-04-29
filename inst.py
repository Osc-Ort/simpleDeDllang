import sys
from typing import Final, TypeAlias

tiposPermitidos: TypeAlias = float


class BadIntruction(Exception):
    pass


def ejecucionIntrucciones(instrs: list[str]):
    variables: dict[str, tiposPermitidos] = {}
    try:
        i = 0
        while i < len(instrs):
            i = ejecutarIntruccion(i, instrs[i], variables)
    except BadIntruction as bd:
        print(
            f"Bad intruction in line {bd.args[0]} ({bd.args[1]})", file=sys.__stderr__
        )


asignacion: Final[set[str]] = {"="}
operadores_bin: Final[set[str]] = {"+", "-", "/", "*"}
etiquetas: dict[str, int] = {}


def ejecutarIntruccion(
    i: int, inst: str, variables: dict[str, tiposPermitidos], interactivo: bool = False
) -> int:
    inst: list[str] = inst.strip().split()
    if not inst:
        raise Exception("Error fatal")
    if len(inst) == 1:  # O variables solas o etiquetas
        if interactivo:
            raise BadIntruction("No permitidas las etiquetas en modo interactivo.")
        inst: str = inst[0]
        if inst.endswith(":"):
            etiquetas[inst] = i
            return i + 1
        elif inst in variables:
            print(variables[inst])
            return i + 1
        else:
            raise BadIntruction(i, inst)
    elif inst[0] == "IF":  # Los IFs
        if interactivo:
            raise BadIntruction("No permitidos los IFs en modo interactivo.")
        if len(inst) > 3:
            raise BadIntruction(
                i, f"Los IFs solo son seguidos de una variable y una etiqueta. {inst}"
            )
        var = inst[1]
        etiqueta = inst[2]
        if not etiqueta.endswith(":"):
            etiqueta += ":"
        if var not in variables:
            raise BadIntruction(i, f"Variable {var} no existente.")
        if etiqueta not in etiquetas:
            raise BadIntruction(i, f"Etiqueta {var} no existente.")
        if int(variables[var]):
            return etiquetas[etiqueta]
        else:
            return i + 1
    elif (len(inst) > 2 and inst[0] in operadores_bin) or (
        len(inst) > 3 and inst[1] in asignacion
    ):
        if inst[1] in asignacion:  # Asignacion
            inst_c = inst[2:]
        else:
            inst_c = inst
        res = 0.0
        match inst_c[0]:
            case "+":
                res = sum(
                    map(
                        lambda x: variables[x] if x in variables else float(x),
                        inst_c[1:],
                    )
                )
            case "-":
                res = (
                    variables[inst_c[1]] if inst_c[1] in variables else float(inst_c[1])
                ) - sum(
                    map(
                        lambda x: variables[x] if x in variables else float(x),
                        inst_c[2:],
                    )
                )
            case "/":
                res = (
                    variables[inst_c[1]] if inst_c[1] in variables else float(inst_c[1])
                )
                for num in map(
                    lambda x: variables[x] if x in variables else float(x), inst_c[2:]
                ):
                    res /= num
            case "*":
                res = 1.0
                for num in map(
                    lambda x: variables[x] if x in variables else float(x), inst_c[1:]
                ):
                    res *= num
        if inst[1] in asignacion:
            variables[inst[0]] = res
        else:
            print(res)
        return i + 1
    else:
        raise BadIntruction(i, f"Instrucción no existente, {inst}.")

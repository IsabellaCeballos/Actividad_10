

class ReglaValidacion:
    def __init__(self, longitud_esperada):
        self.longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self.longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    def es_valida(self, clave):
        return (
            self._validar_longitud(clave) and
            self._contiene_mayuscula(clave) and
            self._contiene_minuscula(clave) and
            self._contiene_numero(clave)
        )


class ReglaValidacionGanimedes(ReglaValidacion):
    def _contiene_caracter_especial(self, clave):
        caracteres_especiales = "@_#$%"
        return any(c in caracteres_especiales for c in clave)

    def es_valida(self, clave):
        if super().es_valida(clave) and self._contiene_caracter_especial(clave):
            return True
        else:
            raise ExcepcionValidacionGanimedes("La clave no cumple con la regla de Validación Ganímedes")


class ReglaValidacionCalisto(ReglaValidacion):
    def _contiene_calisto(self, clave):
        return "calisto" in clave.lower() and any(c.isupper() for c in clave) and not clave.isupper()

    def es_valida(self, clave):
        if super().es_valida(clave) and self._contiene_calisto(clave):
            return True
        else:
            raise ExcepcionValidacionCalisto("La clave no cumple con la regla de Validación Calisto")


class Validador:
    def __init__(self, regla_validacion):
        self.regla_validacion = regla_validacion

    def es_valida(self, clave):
        try:
            return self.regla_validacion.es_valida(clave)
        except (ExcepcionValidacionGanimedes, ExcepcionValidacionCalisto) as e:
            return str(e)


try:
    regla_ganimedes = ReglaValidacionGanimedes(8)
    validador_ganimedes = Validador(regla_ganimedes)
    clave1 = "Clav3@Gan"
    resultado_ganimedes = validador_ganimedes.es_valida(clave1)
    print("Resultado Ganimedes:", resultado_ganimedes)
except ExcepcionValidacionGanimedes as e:
    print(e)

try:
    regla_calisto = ReglaValidacionCalisto(6)
    validador_calisto = Validador(regla_calisto)
    clave2 = "cAliStO123"
    resultado_calisto = validador_calisto.es_valida(clave2)
    print("Resultado Calisto:", resultado_calisto)
except ExcepcionValidacionCalisto as e:
    print(e)

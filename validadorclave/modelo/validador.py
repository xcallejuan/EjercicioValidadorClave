from abc import ABC, abstractmethod
from .errores import (
    NoCumpleLongitudMinimaError,
    NoTieneLetraMayusculaError,
    NoTieneLetraMinusculaError,
    NoTieneNumeroError,
    NoTieneCaracterEspecialError,
    NoTienePalabraSecretaError
)
class ReglaValidacion(ABC):
    def _init_(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave):
        pass

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)
    class ReglaValidacionGanimedes:

        def _init_(self):
            super()._init_(8)

        def contiene_caracter_especial(self, clave):
            return any(c in "@_#$%" for c in clave)

        def es_valida(self, clave):
            if not self._validar_longitud(clave):
                raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 8 caracteres")
            if not self._contiene_mayuscula(clave):
                raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")
            if not self._contiene_minuscula(clave):
                raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")
            if not self._contiene_numero(clave):
                raise NoTieneNumeroError("La clave debe contener al menos un número")
            if not self.contiene_caracter_especial(clave):
                raise NoTieneCaracterEspecialError(
                    "La clave debe contener al menos un carácter especial (@, _, #, $ o %)")
            return True
class ReglaValidacionCalisto(ReglaValidacion):
    def _init_(self):
        super()._init_(6)

    def contiene_calisto(self, clave):
        clave_lower = clave.lower()
        posiciones = [i for i in range(len(clave_lower)) if clave_lower.startswith("calisto", i)]

        for pos in posiciones:
            palabra_original = clave[pos:pos + 7]
            mayusculas = sum(1 for c in palabra_original if c.isupper())
            if 2 <= mayusculas < 7:
                return True
        return False

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 6 caracteres")

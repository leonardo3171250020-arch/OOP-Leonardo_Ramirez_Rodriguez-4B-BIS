class SuscripcionExpiradaError(Exception):
    def __init__(self):
        self.message = "La suscripción ha expirado. Por favor, renueva tu suscripción para acceder a esta función."
        super().__init__(self.message)

class PuntosInsuficientesError(Exception):
    def __init__(self):
            self.message = "No tienes suficientes gemas para gastar."
            super().__init__(self.message)

class PerfilMovil:

    def __init__(self, username:str, gemas:int = 50):
        self.username = username
        self.gemas = gemas
        self.racha_dias = 1
        self.notificaciones_activas = True
        if self.gemas < 0:
            raise ValueError("El número de gemas no puede ser negativo.")

    def balance(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("El balance de gemas no puede ser negativo.")
        return cantidad
    
    def ganar_gemas(self, cantidad: int) -> int:
        self.gemas += self.balance(cantidad)
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if self.balance(cantidad) > self.gemas:
            raise PuntosInsuficientesError()
        self.gemas -= self.balance(cantidad)
        return self.gemas

class PerfilPro(PerfilMovil):

    def __init__(self, username:str, gemas:int, meses_suscripcion:int = 1):
        super().__init__(username, gemas)
        self.meses_suscripcion = meses_suscripcion
        if self.meses_suscripcion > 0:
            self.es_pro = True
        if self.meses_suscripcion <= 0:
                            raise ValueError("El número de meses de suscripción no puede ser negativo.")
        if self.gemas < 0:
                    raise ValueError("El número de gemas no puede ser negativo.")

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError()
        return "Contenido descargado para uso offline."
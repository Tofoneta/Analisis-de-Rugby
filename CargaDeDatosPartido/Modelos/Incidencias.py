class RuckMaul:
   def __init__(self,rapidoGanado, lentoGanado , rapidoPerdido,lentoPerdido,penalizado):
        self.rapidoGanado = rapidoGanado
        self.rapidoPerdido = rapidoPerdido
        self.lentoGanado = lentoGanado
        self.lentoPerdido = lentoPerdido
        self.penalizado = penalizado
        self.total = rapidoGanado + rapidoPerdido + lentoGanado + lentoPerdido + penalizado


class Kick:
    def __init__(self,suelo, touch, atrapado ):
        self.suelo = suelo
        self.touch = touch
        self.atrapado = atrapado
        self.total = suelo + touch + atrapado



    def __repr__(self):
        return "{0},{1},{2},{3}".format(self.total, self.suelo, self.touch,self.atrapado)


class Scrum:
    def __init__(self,ganadoLimpio, ganadoDesorganizado , perdidoLimpio , perdidoDesorganizado , penalizados):
        self.ganadoLimpio = ganadoLimpio
        self.ganadoDesorganizado = ganadoDesorganizado
        self.perdidoLimpio = perdidoLimpio
        self.perdidoDesorganizado = perdidoDesorganizado
        self.penalizados = penalizados
        self.total = ganadoLimpio + ganadoDesorganizado + perdidoLimpio + perdidoDesorganizado + penalizados


class Pase:
    def __init__(self, precisoAtrapado, precisoCaido, imprecisoAtrapado, imprecisoCaido, imprecisoForward):
        self.precisoAtrapado = precisoAtrapado
        self.precisoCaido = precisoCaido
        self.imprecisoAtrapado = imprecisoAtrapado
        self.imprecisoCaido = imprecisoCaido
        self.imprecisoForward = imprecisoForward


class Lineout: 
    def __init__(self,ganadoLimpio, ganadoDesorganizado , perdidoLimpio , perdidoDesorganizado , penalizados):
        self.ganadoLimpio = ganadoLimpio
        self.ganadoDesorganizado = ganadoDesorganizado
        self.perdidoLimpio = perdidoLimpio
        self.perdidoDesorganizado = perdidoDesorganizado
        self.penalizados = penalizados
        self.total = ganadoLimpio + ganadoDesorganizado + perdidoLimpio + perdidoDesorganizado + penalizados


class Puntuacion:
    def __init__(self,tipoTry,puntos,jugador,minuto):
        self.tipoTry = tipoTry
        self.puntos = puntos
        self.jugador = jugador
        self.minuto = minuto

    def __repr__(self):
        return '{0}, {1}, {2}, {3}'.format(self.tipoTry,self.puntos,self.jugador,self.minuto)
class PuntuacionContrario:
    def __init__(self,tipoTry,minuto):
        self.tipoTry = tipoTry
        
        self.minuto = minuto

    
class Tackle:
    def __init__(self,ofensivo,neutral,pasivo,errado):
        self.touch = ofensivo
        self.suelo = neutral
        self.atrapado = pasivo
        self.errado  = errado
        self.total = ofensivo + neutral + pasivo + errado

    
    def getTotal(self):
        return self.total

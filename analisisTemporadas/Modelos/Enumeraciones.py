from enum import Enum

class Resultado(Enum):
    Victoria = 1,
    Empate = 2,
    Derrota = 3,

class Disciplina(Enum):
    sinBin = "Sin Bin",
    Expulsion = "Expulsion"


class Kicks(Enum):
    Touch = "Touch",
    Atrapado = "Atrapado"
    Suelo = "Suelo"


class TipoIncidencia(Enum):
    Kick = "Kick"
    PaseResultado = "Pase Resultado"
    PaseCalidad = "Pase Calidad"
    Puntuacion = "Puntuacion"
    PuntuacionEnContra = "Puntuacion en contra"
    RuckAndMaukResultado = "Ruck And Maul Resultado"
    RuckAndMaulCalidad = "Ruck and Maul Calidad"
    Tacle = "Tackle"
    LineoutResultado = "Lineout Resultado"
    LineoutCalidad = "Lineout Calidad"
    ScrumCalidad = "Scrum Calidad"
    ScrumResultado = "Scrum Resultado"
    TackleResultado = "Tackle Resultado"
    TackleEficiencia = "Tackle Eficiencia"

class JugadoresDisciplina():
    
    def __init__(self, Nombre, SinBin, Expulsion):
        self.Nombre = ""
        self.SinBin = 0
        self.Expulsion = 0
  
    
    def addSinBin(self):
        self.SinBin += 1

    def addExpulsion(self):
        self.Expulsion += 1

    
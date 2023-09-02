
from enum import Enum

class ResultadoA(Enum):
    Atrapado = 1
    Caido = 2
    Forward = 3

class ResultadoB(Enum):
    Ganado = 1
    Perdido = 2
    Penalizado = 3



class ResultadoC(Enum):
    Realizado = 1
    Errado = 2

class ResultadoD(Enum):
    Atrapado = 1
    Touch = 2
    Suelo = 3

class CalificacionA(Enum):
    Ofensivo = 1
    Neutral = 2
    Pasivo = 3


class CalificacionB(Enum):
    Preciso = 1
    Impreciso = 2

class CalificacionC(Enum):
    Limpio = 1
    Desorganizado  = 2

class CalificacionD(Enum):
    Rapido = 1
    Lento = 2

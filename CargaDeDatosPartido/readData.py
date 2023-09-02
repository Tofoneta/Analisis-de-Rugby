import pandas as pd
import numpy as np
from analisisTemporadas.Modelos import Enumeraciones as en
infoGeneral = ('CargaDeDatosPartido/Planillas de cálculo/Información.xlsx')
partido = ('CargaDeDatosPartido/Planillas de cálculo/Partido.xlsx')


def resultadoPartido(puntosEquipoA,puntosEquipoB,equipoA,equipoB):
    
    if (puntosEquipoA>puntosEquipoB).bool():
        return en.Resultado.Victoria.name
    if (puntosEquipoA<puntosEquipoB).bool():
        return en.Resultado.Derrota.name
    else:
        return en.Resultado.Empate.name

#Equipos Involucrados
def equipos(resultado):
    equipoA = ""
    equipoB = ""
    primeraVuelta = True
    for r in resultado:
        if primeraVuelta:
            equipoA = r
            primeraVuelta = False
        else:
            equipoB = r

    return equipoA,equipoB        



#Lectura del archivo excel
info = pd.read_excel(infoGeneral)
infoPartido = pd.read_excel(partido, header=[0,1],sheet_name="Partido")
incidenciaPartido = pd.read_excel(partido, header=[0,1],sheet_name="Incidencias")
jugadoresPartido = pd.read_excel(partido, sheet_name="Equipo")


temporada = str(infoPartido["Información","Temporada"][0])
torneo =str(infoPartido["Información","Fase"][0])
fechas = str(infoPartido["Información","Fecha"][0])


#Desglosar la información

#Equipos Involucrados y Resultado
resultado = infoPartido["Resultado"]



equipoPrincipal,equipoB = equipos(resultado)
puntosEquipoA = resultado[equipoPrincipal]
puntosEquipoB = resultado[equipoB]



quienGano = resultadoPartido(puntosEquipoA,puntosEquipoB,equipoPrincipal,equipoB)

fecha = "Fecha {0} - {1}".format(fechas,torneo)


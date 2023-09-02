import analisisTemporadas.database as db
from CargaDeDatosPartido import readData as rD
import pandas as pd
import matplotlib.pyplot as plt
import analisisTemporadas.analisisAuxiliar as aA
import analisisTemporadas.Modelos.Enumeraciones as en
import analisisTemporadas.Documentacion.analisisEscritura as es


def Efectividad():
    a = db.readAll()
    equipo = rD.equipoPrincipal
    temporada = rD.equipoPrincipal
    
    porcentajeVictorias,porcentajeDerrotas = aA.efectividad(a)

    es.generarParrafoEfectividad(porcentajeVictorias)
   


def Kicks(temporada):
    a = db.readKicks(temporada)

    
    index, listaPorcentaje,listaCantidadKicks = aA.analisisKicks(a)

    aA.analisisKickCantidad(listaPorcentaje,index)
    listaResultado = aA.analisisDeLosKicks(a)

    #Gráfico
    resultados = pd.DataFrame(listaResultado,columns=["Suelo","Atrapado","Touch"],index=index)
    resultadosKicksCantidad = pd.DataFrame(listaCantidadKicks,columns=["Suelo","Atrapado","Touch"],index=index)
  
    esKick = en.TipoIncidencia.Kick.value
    
    #Crear gráfico
    aA.graficoCantidad(resultadosKicksCantidad,esKick)

    #Crear texto

    aA.analisisDataframe(resultadosKicksCantidad,esKick)

    


def Disciplina(temporada):
    #Hago la query para la base de datos
    ad = db.readDiscipline(temporada)
    #Me devuelve el index y los datos para el dataFrame
    listaJugadoresIndisciplina = pd.DataFrame(ad,columns=["Jugadores","Cantidad de expulsiones","Cantidad de Sin Bin"])
    index,disciplinaResultado = aA.analisisDisciplina(ad)
    #Convierto en Dataframe los datos obtenidos
    datosDisciplina = pd.DataFrame(disciplinaResultado,columns=["Cantidad de Expulsiones","Cantidad de Sin Bin"],index=index)
    #Devuelvo el jugador con mayor cantidad de indisciplinas. Criterio: Mayor cantidad de expulsiones
    mayorIndisciplina = listaJugadoresIndisciplina.head(1)
        

    return datosDisciplina,mayorIndisciplina
    
def Puntuacion(temporada):
    a = db.readPuntuacion(temporada)
    aCuartiles = db.puntuacionCuartiles(temporada)
    index,cuartiles,porcentajes = aA.analisisPuntuacionPercentiles(aCuartiles)
    
    #anotadores = aA.maximosAnotadores(a,3)
   

    listaCuartilesConIndex = pd.DataFrame(aCuartiles,columns=["Fecha","Primeros 20 minutos","Minutos 20 a 40", "Minutos 40 a 60", "Minutos 60 a 80"])
    cuartilesDataframe = pd.DataFrame(cuartiles,columns=["Minutos 0 a 20","Minutos 20 a 40", "Minutos 40 a 60","Minutos 60 a 80"],index=index)
    cuartilesPorcentajesDataframe = pd.DataFrame(porcentajes,columns=["Minutos 0 a 20","Minutos 20 a 40", "Minutos 40 a 60","Minutos 60 a 80"],index=index)

    #maximoCuartil = aCuartiles.idxmax(axis = 1)
    esPuntuacion = en.TipoIncidencia.Puntuacion.value  
    aA.graficoCantidad(cuartilesDataframe,esPuntuacion)
    aA.graficoPorcentaje(cuartilesPorcentajesDataframe,esPuntuacion)

    aA.analisisDataframe(cuartilesDataframe,esPuntuacion)




def PuntuacionEnContra(temporada):
    a = db.readPuntuacionEnContra
   
    aCuartiles = db.puntuacionCuartilesEnContra(temporada)
    index,cuartiles,porcentajes = aA.analisisPuntuacionPercentiles(aCuartiles)
  
    cuartilesEnContraDataframe = pd.DataFrame(cuartiles,columns=["Minutos 0 a 20","Minutos 20 a 40", "Minutos 40 a 60","Minutos 60 a 80"],index=index)
    cuartilesEnContraPorcentajesDataframe = pd.DataFrame(porcentajes,columns=["Minutos 0 a 20","Minutos 20 a 40", "Minutos 40 a 60","Minutos 60 a 80"],index=index)
 
    esPuntuacionEnContra = en.TipoIncidencia.PuntuacionEnContra.value

    aA.graficoCantidad(cuartilesEnContraDataframe,esPuntuacionEnContra)
    aA.graficoPorcentaje(cuartilesEnContraPorcentajesDataframe,esPuntuacionEnContra)


    aA.analisisDataframe( cuartilesEnContraDataframe,esPuntuacionEnContra)

    
def Lineouts(temporada):
    a = db.readLineout(temporada)
    
    index,listaResultadosPorcentaje,listaCalidadPorcentaje,listaResultadoCantidad,listaCalidadCantidad = aA.analisisFormacionesFijas(a)       
    resultadosLineoutCantidad = pd.DataFrame(listaResultadoCantidad,columns=["Ganados","Perdidos","Penalizados"],index=index)
    calidadLineoutCantidad = pd.DataFrame(listaCalidadCantidad,columns=["Limpios","Desorganizados","Penalizados"],index=index)
    resultadosLineoutPorcentajeDataframe = pd.DataFrame(listaResultadosPorcentaje,columns=["Ganados","Perdidos","Penalizados"],index=index)
    calidadLineoutPorcentajeDataframe = pd.DataFrame(listaResultadosPorcentaje,columns=["Limpios","Desorganizados","Penalizados"],index=index)
    

    esLineoutResultado = en.TipoIncidencia.LineoutResultado.value
    aA.graficoCantidad(resultadosLineoutCantidad,esLineoutResultado)
    aA.graficoPorcentaje(resultadosLineoutPorcentajeDataframe,esLineoutResultado)
    #Grafico
  
    esLineoutCalidad = en.TipoIncidencia.LineoutCalidad.value
    aA.graficoCantidad(calidadLineoutCantidad,esLineoutCalidad)
    aA.graficoPorcentaje(calidadLineoutPorcentajeDataframe,esLineoutCalidad)
    

    #Grafico porcentaje comparacion fecha de la calidad
    aA.analisisDataframe(calidadLineoutPorcentajeDataframe,esLineoutCalidad)
    aA.analisisDataframe(resultadosLineoutPorcentajeDataframe,esLineoutResultado)
    
def Pases(temporada):
    a = db.readPase(temporada)
    
    index,pasesPorcentajeCalidad,pasesPorcentajeResultado,pasesCantidadResultado,pasesCantidadCalidad = aA.analisisPases(a)
    resultadoPasesPorcentajeDataframe = pd.DataFrame(pasesPorcentajeResultado,columns=["Atrapados","Caidos","Forwards"],index=index)
    calidadPasesPorcentajeDataframe = pd.DataFrame(pasesPorcentajeCalidad,columns=["Precisos","Imprecisos"],index=index)
    resultadoPasesCantidadDataframe = pd.DataFrame(pasesCantidadResultado,columns=["Atrapados","Caidos","Forwards"],index=index)
    calidadPasesCantidadDataframe = pd.DataFrame(pasesCantidadCalidad,columns=["Precisos","Imprecisos"],index=index)
   
    paseCalidad = en.TipoIncidencia.PaseCalidad.value
    paseResultado = en.TipoIncidencia.PaseResultado.value
    
    aA.graficoCantidad(resultadoPasesCantidadDataframe,paseResultado)
    aA.graficoCantidad(calidadPasesCantidadDataframe,paseCalidad)

    
    aA.graficoPorcentaje(calidadPasesPorcentajeDataframe,paseCalidad)
    aA.graficoPorcentaje(resultadoPasesPorcentajeDataframe,paseResultado)  

    aA.analisisDataframe(calidadPasesPorcentajeDataframe,paseCalidad)

    aA.analisisDataframe(resultadoPasesPorcentajeDataframe,paseResultado)

def RuckAndMaul(temporada):
    a = db.readRuckAndMaul(temporada)
   
    index,porcentajeResultado,porcentajeCalidad,cantidadResultado,cantidadCalidad = aA.analisisFormaciones(a)
        
    
  
    porcentajeResultadoDataFrame = pd.DataFrame(porcentajeResultado,columns=["Ganados","Perdidos","Penalizados"],index=index)
    porcentajeCalidadDataFrame = pd.DataFrame(porcentajeCalidad,columns=["Rapidos","Lentos","Penalizados"],index=index)
    cantidadResultadoDataFrame = pd.DataFrame(cantidadResultado,columns = ["Ganados","Perdidos","Penalizados"],index=index)
    cantidadCalidadDataFrame = pd.DataFrame(cantidadCalidad,columns=["Rapidos","Lentos","Penalizados"],index=index)

    esRuckMaulResultado = en.TipoIncidencia.RuckAndMaukResultado.value
    esRuckMaulCalidad = en.TipoIncidencia.RuckAndMaulCalidad.value
  

    aA.graficoCantidad(cantidadResultadoDataFrame,esRuckMaulResultado)
        
    aA.graficoCantidad(cantidadCalidadDataFrame,esRuckMaulCalidad)

    aA.graficoPorcentaje(porcentajeCalidadDataFrame,esRuckMaulResultado)
    aA.graficoPorcentaje(porcentajeResultadoDataFrame,esRuckMaulResultado)

    aA.analisisDataframe(porcentajeCalidadDataFrame,esRuckMaulCalidad)
    aA.analisisDataframe(porcentajeResultadoDataFrame,esRuckMaulResultado)

    
def Scrum(temporadas):
    a = db.readScrum(temporadas)
    index,porcentajeResultado,porcentajeCalidad,cantidadCalidad,cantidadResultado= aA.analisisFormacionesFijas(a)
    porcentajeResultadoDataFrame = pd.DataFrame(porcentajeResultado,columns=["Ganados","Perdidos","Penalizados"],index=index)
    porcentajeCalidadDataFrame = pd.DataFrame(porcentajeCalidad,columns=["Limpios","Desorganizados","Penalizados"],index=index)
    cantidadResultadoDataFrame = pd.DataFrame(cantidadResultado,columns = ["Ganados","Perdidos","Penalizados"],index=index)
    cantidadCalidadDataFrame = pd.DataFrame(cantidadCalidad,columns=["Limpios","Desorganizados","Penalizados"],index=index)
    scrumCalidad = en.TipoIncidencia.ScrumCalidad.value
    scrumResultado = en.TipoIncidencia.ScrumResultado.value

    #Graficos Cantidad
    aA.graficoCantidad(cantidadCalidadDataFrame,scrumCalidad)
    aA.graficoCantidad(cantidadResultadoDataFrame,scrumResultado)


  

    aA.analisisDataframe(porcentajeResultadoDataFrame,scrumResultado)
    aA.analisisDataframe(porcentajeCalidadDataFrame,scrumCalidad)
def Tackles(temporada):
    a = db.readTackle(temporada)
    index,porcentajeResultado,porcentajeEficiencia = aA.analisisTackles(a)    

    porcentajeResultadoDataframe = pd.DataFrame(porcentajeResultado,columns=["Ofensivos","Neutrales","Pasivos"],index=index)
    porcentajeEficienciaDataframe = pd.DataFrame(porcentajeEficiencia,columns=["Tackles Realizados","Tackles Errados"],index=index)



    #Graficos
    tacklesResultado = en.TipoIncidencia.TackleResultado.value
    tackleEficiencia = en.TipoIncidencia.TackleEficiencia.value

    aA.graficoPorcentaje(porcentajeResultadoDataframe,tacklesResultado)
    aA.graficoPorcentaje(porcentajeEficienciaDataframe,tackleEficiencia)
  
    aA.analisisDataframe(porcentajeEficienciaDataframe,tackleEficiencia)
    aA.analisisDataframe(porcentajeResultadoDataframe,tacklesResultado)

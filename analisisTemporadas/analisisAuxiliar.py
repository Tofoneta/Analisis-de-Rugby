import pandas as pd
import matplotlib.pyplot as plt
import analisisTemporadas.Modelos.Enumeraciones as en
import analisisTemporadas.Documentacion.analisisEscritura as es
import numpy as np
from matplotlib.ticker import MultipleLocator

directorio = 'Agregar dirección para guardar los gráficos'
def efectividad(a):
    victorias = 0
    derrotas = 0
    empates = 0
 
    for elemento in a:
        
        if(elemento[2]) == en.Resultado.Victoria.name:
            victorias += 1

        elif(elemento[2]) == en.Resultado.Empate.name:
            empates += 1

        else:
            derrotas += 1

    total = (victorias+derrotas+empates)


    porcentajeVictoria = (victorias/total)*100
    porcentajeDerrotas = (derrotas/total)*100
    
    return porcentajeVictoria,porcentajeDerrotas
      
def porcentaje(numero,total):
    if total == 0:
        return 0
    else:
        return ((numero/total)*100)


def vacioResultados(victorias,derrotas,empates):
    total = victorias + derrotas + empates

    if victorias > 0:
        porcentajeVictorias = (victorias / total)*100
    
    elif derrotas >0:
        porcentajeDerrotas = (derrotas / total)*100
    
    else:
        porcentajeEmpates = (empates / total)*100    



def analisisDeLosKicks(a):

    listaResultado = []
    for Fecha, Suelo, Atrapado, Touch in a:
            total = Suelo + Atrapado + Touch
            porcentajeSuelo = porcentajeIncidencias(total,Suelo)
            porcentajeTouch = porcentajeIncidencias(total,Touch)
            porcentajeAtrapado = porcentajeIncidencias(total,Atrapado)

            resultado = (round(porcentajeSuelo,2),round(porcentajeAtrapado,2),round(porcentajeTouch,2))
            listaResultado.append(resultado)

    return listaResultado

def analisisKicks(a):
    index = []
    listaPorcentaje = []
    listaCantidad = []
    for Fecha, Suelo, Atrapado, Touch in a:
        total = Suelo + Atrapado + Touch
        porcentajeSuelo = porcentajeIncidencias(total,Suelo)
        porcentajeTouch = porcentajeIncidencias(total,Touch)
        porcentajeAtrapado = porcentajeIncidencias(total,Atrapado)
        kicks = [Suelo,Atrapado,Touch]
     
        index.append(Fecha)
        listaCantidad.append(kicks)
        resultado = (round(porcentajeSuelo,2),round(porcentajeAtrapado,2),round(porcentajeTouch,2))
        listaPorcentaje.append(resultado)

    
    return index,listaPorcentaje,listaCantidad

def porcentajeIncidencias(total,incidencia):
    porcentaje = 0
    if incidencia == 0:
        return porcentaje
    else:
        return (incidencia/total)*100

def analisisKickCantidad(listaKicks,Indice):
    parrafo = ""
   
    touch = 0
    atrapado = 0
    suelo = 0
    
    df = pd.DataFrame(listaKicks,columns=["Suelo","Atrapado","Touch"],index=Indice)
    maxValueIndex = df.idxmax(axis=1)
    for a in maxValueIndex:
        if a == en.Kicks.Suelo.name:
         
            suelo +=1
        elif a == en.Kicks.Touch.name:
            touch += 1
        else:
            atrapado += 1
    
    if atrapado > suelo and atrapado > touch:
        parrafo = "Se puede observar que, a lo largo de las fechas, la mayoría de los kicks fueron atrapados por el equipo contrario."
    elif suelo > atrapado and suelo > touch:
        parrafo = "Se puede observar que, a lo largo de las fechas, la mayoría de los kicks fueron al suelo, no siendo atrapados ni yendose directamente por línea de touch"

    else:
        parrafo = "Se puede observar que, a lo largo de las fechas, la mayoría de los kicks fueron al touch"

        
    return parrafo,df

def analisisFormacionesFijas(a):
    index = []
    listaResultadosPorcentaje = []
    listaCalidadPorcentaje = []
    listaResultadosCantidad = []
    listaCalidadCantidad = []
    for Fecha, GanadoLimpio,GanadoDesorganizado,PerdidoLimpio,PerdidoDesorganizado,Penalizados in a:
        total = GanadoDesorganizado + GanadoLimpio + PerdidoLimpio + PerdidoDesorganizado + Penalizados
        cantidadGanados = GanadoDesorganizado + GanadoLimpio
        cantidadPerdidos = PerdidoDesorganizado + PerdidoLimpio
        cantidadLimpios = GanadoLimpio + PerdidoLimpio
        cantidadDesorganizados = GanadoDesorganizado + PerdidoDesorganizado

        porcentajeGanados = porcentaje(cantidadGanados,total)
        porcentajePerdidos = porcentaje(cantidadPerdidos,total)
        porcentajeLimpios = porcentaje(cantidadLimpios,total)
        porcentajeDesorganizados = porcentaje(cantidadDesorganizados,total)
        porcentajePenalizados = porcentaje(Penalizados,total)    

        porcentajeResultado = (round(porcentajeGanados,2),round(porcentajePerdidos,2),round(porcentajePenalizados,2))
        porcentajeCalidad = (round(porcentajeLimpios,2),round(porcentajeDesorganizados,2),round(porcentajePenalizados,2))
        cantidadResultado = (cantidadGanados,cantidadPerdidos,Penalizados)
        cantidadCalidad = (cantidadLimpios,cantidadDesorganizados,Penalizados)

        index.append(Fecha)
        listaResultadosPorcentaje.append(porcentajeResultado)
        listaCalidadPorcentaje.append(porcentajeCalidad)

        listaResultadosCantidad.append(cantidadResultado)
        listaCalidadCantidad.append(cantidadCalidad)

    return index,listaResultadosPorcentaje,listaCalidadPorcentaje,listaCalidadCantidad,listaResultadosCantidad

def analisisFormaciones(a):
    index = []
    porcentajeResultado = []
    porcentajeCalidad = []
    cantidadResultado = []
    cantidadCalidad = []
    for Fecha, RapidoGanado,LentoGanado,RapidoPerdido,LentoPerdido,Penalizado in a:
        total = RapidoGanado + LentoGanado + RapidoPerdido + LentoPerdido + Penalizado
        ganados = RapidoGanado + LentoGanado
        perdidos = RapidoPerdido + LentoPerdido
        rapidos = RapidoPerdido + RapidoGanado
        lentos = LentoGanado + LentoPerdido
        porcentajeGanados = porcentaje(ganados,total)
        porcentajePerdidos = porcentaje(perdidos,total)
        porcentajeRapidos = porcentaje(rapidos,total)
        porcentajeLentos = porcentaje(lentos,total)
        porcentajePenalizados = porcentaje(Penalizado,total)  
        index.append(Fecha)
        pCalidad = (porcentajeRapidos,porcentajeLentos,porcentajePenalizados)
        pResultado = (porcentajeGanados,porcentajePerdidos,porcentajePenalizados)
        qCalidad = (rapidos,lentos,Penalizado)
        qResultado = (ganados,perdidos,Penalizado)

        porcentajeResultado.append(pResultado)
        porcentajeCalidad.append(pCalidad)
        cantidadResultado.append(qResultado)
        cantidadCalidad.append(qCalidad)

    return index,porcentajeResultado,porcentajeCalidad,cantidadResultado,cantidadCalidad


def analisisPases(a):

    index = []
    pasesPorcentajeResultado = []
    pasesPorcentajeCalidad = []
    pasesCantidadResultado = []
    pasesCantidadCalidad = []

    for Fecha, PrecisoAtrapado,PrecisoCaido,ImprecisoAtrapado,ImprecisoCaido,ImprecisoForward in a:
        index.append(Fecha)
        total = PrecisoAtrapado + PrecisoCaido + ImprecisoAtrapado + ImprecisoCaido + ImprecisoForward
        cantidadPrecisos = PrecisoAtrapado + PrecisoCaido
        cantidadImprecisos = ImprecisoAtrapado + ImprecisoCaido + ImprecisoForward
        cantidadAtrapados = PrecisoAtrapado + ImprecisoAtrapado
        cantidadCaidos = PrecisoCaido + ImprecisoCaido
        
        qResultado = (cantidadAtrapados,cantidadCaidos,ImprecisoForward)
        qCalidad = (cantidadPrecisos,cantidadImprecisos)
        
        atrapados = porcentajeIncidencias(total,cantidadAtrapados)
        caidos = porcentajeIncidencias(total,cantidadCaidos)
        precisos = porcentajeIncidencias(total,cantidadPrecisos)
        imprecisos = porcentajeIncidencias(total,cantidadImprecisos)
        forward = porcentajeIncidencias(total,ImprecisoForward)
        resultadoPases = (round(atrapados,2),round(caidos,2),round(forward))
        calidadPases = (round(precisos,2),round(imprecisos,2))
        pasesPorcentajeResultado.append(resultadoPases)
        pasesPorcentajeCalidad.append(calidadPases)
        pasesCantidadResultado.append(qResultado)
        pasesCantidadCalidad.append(qCalidad)
    
    return index,pasesPorcentajeCalidad,pasesPorcentajeResultado,pasesCantidadResultado,pasesCantidadCalidad

def analisisDisciplina(a):
    index = []
    disciplinaResultado = []
    for jugador,cantidadExpulsiones,cantidadSinBin in a:
        qDisciplina = (cantidadExpulsiones,cantidadSinBin)
        index.append(jugador)
        disciplinaResultado.append(qDisciplina)

    return index,disciplinaResultado


def analisisPuntuacionPercentiles(listaPercentiles):
    fecha = []
    percentiles = []
    porcentajes = []
    for Fecha,PrimerCentil,SegundoCentil,TercerCentil,CuartoCuartil in listaPercentiles:
        total = int(PrimerCentil)+int(SegundoCentil)+int(TercerCentil)+int(CuartoCuartil)
      
        primerCentil = porcentaje(int(PrimerCentil),total)
        segundoCentil = porcentaje(int(SegundoCentil),total)
        tercerCentil  = porcentaje((TercerCentil),total)
        cuartoCuartil = porcentaje((CuartoCuartil),total)
        porcentajeFecha = (primerCentil,segundoCentil,tercerCentil,cuartoCuartil)
        fecha.append(Fecha)
        datosPercentil = (int(PrimerCentil),int(SegundoCentil),int(TercerCentil),int(CuartoCuartil)) 
        percentiles.append(datosPercentil)
        porcentajes.append(porcentajeFecha)

    return fecha,percentiles,porcentajes

def analisisTackles(listaTackles):
    #SELECT Fecha,Ofensivo,Neutral,Pasivo,Errado from Tackle
    fecha = []
    resultado = []
    eficienciaTackle = []
    for Fecha,Ofensivo,Neutral,Pasivo,Errado in listaTackles:
        total = Ofensivo + Neutral + Pasivo + Errado
        totalRealizados = Ofensivo + Neutral + Pasivo
        tacklesRealizados = Ofensivo + Neutral + Pasivo
        porcentajeTacklesRealizados = porcentaje(tacklesRealizados,total)
        porcentajeTacklesErrados = porcentaje(Errado,total)
        porcentajeTacklesOfensivos = porcentaje(Ofensivo,totalRealizados)
        porcentajeTacklesNeutrales = porcentaje(Neutral,totalRealizados)
        porcentajeTacklesPasivos = porcentaje(Pasivo,totalRealizados)

        fecha.append(Fecha)
        Eficiencia = (round(porcentajeTacklesRealizados,2),round(porcentajeTacklesErrados,2))
        Resultado = (round(porcentajeTacklesOfensivos,2),round(porcentajeTacklesNeutrales,2),round(porcentajeTacklesPasivos,2))

        resultado.append(Resultado)
        eficienciaTackle.append(Eficiencia)
    
    return fecha,resultado,eficienciaTackle


def analisisDataframe(df,tipoIncidencia):
    #Encontrar la columna con la mayor cantidad por fecha
    maximaIncidenciaPorFecha = df.idxmax(axis=1)

    # b) Encontrar la columna con la mayor cantidad en total a lo largo de la temporada
    totalPorIncidencia= df.sum()
    maximaIncidenciaPorTemporada= totalPorIncidencia.idxmax()

    # c) Tendencias a lo largo de las fechas
    tendencia = df.copy()
    tendencia['Fecha'] = tendencia.index
    tendenciaTemporada = tendencia.melt(id_vars=['Fecha'], var_name='Categoria', value_name='Cantidad')

    
    
    es.generarParrafo(tipoIncidencia,maximaIncidenciaPorFecha,maximaIncidenciaPorTemporada,tendenciaTemporada)





##Graficos
def graficoCantidad(dataframe,tipoGrafico):
        columnas = dataframe.columns.tolist()
        if tipoGrafico == en.TipoIncidencia.Kick.value:
            titulo = "Cantidad de kicks a lo largo de la temporada"
            nombreArchivo = "Cantidad de kicks.png"
        elif tipoGrafico == en.TipoIncidencia.Puntuacion.value:
            titulo = "Cantidad de trys realizados en los cuartiles del partido"
            nombreArchivo = "Cantidad puntuacion percentiles.png"
        elif tipoGrafico == en.TipoIncidencia.PuntuacionEnContra.value:
            titulo = "Cantidad de trys recibidos en los cuartiles del partido"
            nombreArchivo = "Cantidad puntuacion en contra percentiles.png"
        elif tipoGrafico == en.TipoIncidencia.LineoutResultado.value:
            titulo = "Cantidad de los resultados del lineout"
            nombreArchivo = "Cantidad resultado lineout.png"
        elif tipoGrafico == en.TipoIncidencia.LineoutCalidad.value:
            titulo = "Cantidad de la calidad del lineout"
            nombreArchivo = "Cantidad calidad lineout.png"
        elif tipoGrafico == en.TipoIncidencia.PaseCalidad.value:
            titulo = "Cantidad de calidad de los pases a lo largo de los partidos"
            nombreArchivo = "Cantidad calidad pases.png"
        elif tipoGrafico == en.TipoIncidencia.PaseResultado.value:
            titulo = "Cantidad del resultado de los pases a lo largo de los partidos"
            nombreArchivo = "Cantidad resultado pases.png"
        elif tipoGrafico == en.TipoIncidencia.RuckAndMaukResultado.value:
            titulo = "Cantidad de los resultados de los rucks y mauls"
            nombreArchivo = "Cantidad resultado rucks y mauls.png"
        elif tipoGrafico == en.TipoIncidencia.RuckAndMaulCalidad.value:
            titulo = "Cantidad de la calidad de los rucks y mauls"
            nombreArchivo = "Cantidad calidad Rucks y Mauls.png"
        elif tipoGrafico == en.TipoIncidencia.ScrumCalidad.value:
            titulo = "Cantidad de la calidad de los scrums"
            nombreArchivo = "Cantidad calidad scrum.png"
        elif tipoGrafico == en.TipoIncidencia.ScrumResultado.value:
            titulo = "Cantidad de los resultados de los scrums"
            nombreArchivo = "Cantidad calidad scrums.png"
        
        elif tipoGrafico == en.TipoIncidencia.TackleResultado.value:
            titulo = "Cantidad del resultado de los tackles"
            nombreArchivo = "Cantidad resultado Tackles.png"
        elif tipoGrafico == en.TipoIncidencia.TackleEficiencia.value:
            titulo = "Cantidad de la eficiencia de los tackles"
            nombreArchivo = "Cantidad eficiencia scrums.png"


        # Generar el gráfico
        plt.figure(figsize=(12, 8))  # Ajustar el tamaño del gráfico
        ax = dataframe.plot(figsize=(12, 8), grid=True)
        ax.set_title(titulo)
        ax.set_xlabel("Fechas")
        ax.set_ylabel("Cantidad")

        ax.set_yticks(range(int(dataframe.min().min()), int(dataframe.max().max()) + 1))  # Unidades en el eje Y de uno en uno
        ax.legend(columnas)

        # Guardar el gráfico en el directorio
        plt.savefig(directorio + nombreArchivo)
        plt.close()


def graficoPorcentaje(dataframe,tipoGrafico):
    columnas = dataframe.columns.tolist()
    if tipoGrafico == en.TipoIncidencia.Kick.value:
        titulo = "Porcentaje de kicks a lo largo de la temporada"
        nombreArchivo = "Porcentaje_de_kicks.png"
    elif tipoGrafico == en.TipoIncidencia.Puntuacion.value:
        titulo = "Porcentaje de trys realizados en los cuartiles del partido"
        nombreArchivo = "Porcentaje_puntuacion_percentiles.png"
    elif tipoGrafico == en.TipoIncidencia.PuntuacionEnContra.value:
        titulo = "Porcentaje de trys recibidos en los cuartiles del partido"
        nombreArchivo = "Porcentaje puntuacion en contra percentiles.png"
    elif tipoGrafico == en.TipoIncidencia.LineoutResultado.value:
        titulo = "Porcentaje de los resultados del lineout"
        nombreArchivo = "Porcentaje resultado lineout.png"
    elif tipoGrafico == en.TipoIncidencia.LineoutCalidad.value:
        titulo = "Porcentaje de la calidad del lineout"
        nombreArchivo = "Porcentaje calidad lineout.png"
    elif tipoGrafico == en.TipoIncidencia.PaseCalidad.value:
        
        titulo = "Porcentaje de calidad de los pases a lo largo de los partidos"
        nombreArchivo = "Porcentaje calidad pases.png"
    elif tipoGrafico == en.TipoIncidencia.PaseResultado.value:
        titulo = "Porcentaje del resultado de los pases a lo largo de los partidos"
        nombreArchivo = "Porcentaje resultado pases.png"
    elif tipoGrafico == en.TipoIncidencia.RuckAndMaukResultado.value:
        titulo = "Porcentaje de los resultados de los rucks y mauls"
        nombreArchivo = "Porcentaje resultado rucks y mauls.png"
    elif tipoGrafico == en.TipoIncidencia.RuckAndMaulCalidad.value:
        titulo = "Porcentaje de la calidad de los rucks y mauls"
        nombreArchivo = "Porcentaje calidad Rucks y Mauls.png"
    elif tipoGrafico == en.TipoIncidencia.ScrumCalidad.value:
        titulo = "Porcentaje de la calidad de los scrums"
        nombreArchivo = "Porcentaje calidad scrum.png"
    elif tipoGrafico == en.TipoIncidencia.ScrumResultado.value:
        titulo = "Porcentaje de los resultados de los scrums"
        nombreArchivo = "Porcentaje calidad scrums.png"
    elif tipoGrafico == en.TipoIncidencia.TackleResultado.value:
        titulo = "Porcentaje del resultado de los tackles"
        nombreArchivo = "Porcentaje resultado Tackles.png"
    elif tipoGrafico == en.TipoIncidencia.TackleEficiencia.value:
        titulo = "Porcentaje de la eficiencia de los tackles"
        nombreArchivo = "Porcentaje eficiencia scrums.png"




    # Generar el gráfico de líneas
    plt.figure(figsize=(12, 8))  # Ajustar el tamaño del gráfico
    ax = dataframe.plot(figsize=(12, 8), kind='line', grid=True)
    ax.set_title(titulo)
    ax.set_xlabel("Fechas")
    ax.set_ylabel("Porcentaje")
    ax.set_yticks(range(0, 101, 20))  # Unidades en el eje Y de 20 en 20
    ax.set_ylim(0, 100)  # Límites del eje Y

    # Agregar el símbolo '%' al eje Y
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x)}%"))

    ax.legend(columnas)
    plt.savefig(directorio + nombreArchivo)
    plt.close('all')
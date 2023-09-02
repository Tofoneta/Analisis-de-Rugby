import CargaDeDatosPartido.readData as rD
import pandas as pd
import CargaDeDatosPartido.Modelos.Enumeraciones as rc
import CargaDeDatosPartido.Modelos.Enumeraciones as inc
import CargaDeDatosPartido.baseDatos as bd


#Resultado del encuentro


def resultadoPartido():
   
    

    bd.insertTemporada(rD.temporada,rD.fecha,rD.quienGano)




#Estadisticas de Kick del encuentro

def incidenciasKick():
    suelo = 0
    touch = 0
    atrapado = 0
    

    for kick in rD.incidenciaPartido["Kick","Resultado"]:


        if (kick == rc.ResultadoD.Suelo.name):
            suelo += 1
        if (kick == rc.ResultadoD.Touch.name):
            touch += 1
        
        if (kick == rc.ResultadoD.Atrapado.name):

            atrapado += 1
 
    
    bd.insertKick(rD.temporada,rD.fecha,suelo,atrapado,touch)

#Estadisticas Scrum

def incidenciasScrum():
    ganadoLimpio = 0
    ganadoDesorganizado = 0
    perdidoLimpio = 0
    perdidoDesorganizado = 0
    penalizados = 0

    calidad = rD.incidenciaPartido["Scrum","Calidad"].dropna()
    resultado = rD.incidenciaPartido["Scrum","Resultado"].dropna()
 
    for i in range(0,len(resultado)):
        if resultado[i] == rc.ResultadoB.Ganado.name:
            if calidad[i] == rc.CalificacionC.Limpio.name:
                ganadoLimpio += 1
            else: 
                ganadoDesorganizado  += 1
       
        if resultado[i] == rc.ResultadoB.Perdido.name:
            if calidad[i] == rc.CalificacionC.Limpio:
                perdidoLimpio += 1
            else:
                perdidoDesorganizado += 1
        
        elif resultado[i] == rc.ResultadoB.Penalizado.name:
            penalizados += 1

    bd.insertScrum(rD.temporada,rD.fecha,ganadoLimpio,ganadoDesorganizado,perdidoLimpio,perdidoDesorganizado,penalizados)

def incidenciasTackle():
    ofensivo = 0
    neutral = 0
    pasivo = 0
    errado = 0

    calidad = rD.incidenciaPartido["Tackle","Calidad"].dropna()
    resultado = rD.incidenciaPartido["Tackle","Resultado"].dropna()
    for i in range(0,len(resultado)):
        if resultado[i] == rc.ResultadoC.Realizado.name:
            
            if calidad[i] == rc.CalificacionA.Ofensivo.name:
                ofensivo += 1
            if calidad[i] == rc.CalificacionA.Neutral.name:
                neutral += 1
            if calidad[i] == rc.CalificacionA.Pasivo.name:
                pasivo += 1
        
        elif resultado[i] == rc.ResultadoC.Errado.name:
            errado += 1
            


    bd.insertTackle(rD.temporada,rD.fecha,ofensivo,neutral,pasivo,errado)


def incidenciaPase():
    precisoAtrapado = 0
    precisoCaido = 0
    imprecisoAtrapado = 0
    imprecisoCaido = 0
    imprecisoForward = 0   
    calidad = rD.incidenciaPartido["Pase","Calidad"].dropna()
    resultado = rD.incidenciaPartido["Pase","Resultado"].dropna()
    for i in range(0,len(calidad)):
        if calidad[i] == rc.CalificacionB.Preciso.name:
            if resultado[i] == rc.ResultadoA.Atrapado.name:
                precisoAtrapado += 1
            if resultado[i] == rc.ResultadoA.Caido.name:
           
                precisoCaido += 1

        if calidad[i] == rc.CalificacionB.Impreciso.name:
            if resultado[i] == rc.ResultadoA.Atrapado.name:
                imprecisoAtrapado += 1
            if resultado[i] == rc.ResultadoA.Caido.name:
                imprecisoCaido += 1
            if resultado[i] == rc.ResultadoA.Forward.name:
                imprecisoForward += 1
            

    bd.insertPass(rD.temporada,rD.fecha,precisoAtrapado,precisoCaido,imprecisoAtrapado,imprecisoCaido,imprecisoForward)
 

def incidenciaRuckMaul():
    rapidoGanado = 0
    lentoGanado = 0
    rapidoPerdido = 0
    lentoPerdido = 0
    penalizado = 0

    calidad = rD.incidenciaPartido["Ruck Maul", "Calidad"].dropna()
    resultado = rD.incidenciaPartido["Ruck Maul", "Resultado"].dropna()


    for i in range(0,len(calidad)):
        if calidad[i] == rc.CalificacionD.Rapido.name:
            
            if resultado[i] == rc.ResultadoB.Ganado.name:
                rapidoGanado += 1
            if resultado[i] == rc.ResultadoB.Perdido.name:      

                rapidoPerdido += 1

        
            if resultado[i] == rc.ResultadoB.Penalizado.name:
        
                penalizado += 1
            
        if calidad[i] == rc.CalificacionD.Lento.name:
            if resultado[i] == rc.ResultadoB.Ganado.name:
                lentoGanado += 1
            if resultado[i] == rc.ResultadoB.Perdido.name:
                lentoPerdido += 1
            
            if resultado[i] == rc.ResultadoB.Penalizado.name:
                penalizado += 1
    
    bd.insertRuckMaul(rD.temporada,rD.fecha,rapidoGanado,lentoGanado,rapidoPerdido,lentoPerdido,penalizado)


        
                
    
def incidenciaLineout():
    ganadoLimpio = 0
    ganadoDesorganizado = 0
    perdidoLimpio = 0
    perdidoDesorganizado = 0
    penalizados = 0


    calidad = rD.incidenciaPartido["Line-Out", "Calidad"].dropna()
    resultado = rD.incidenciaPartido["Line-Out", "Resultado"].dropna()


    for i in range(0,len(calidad)):
        if calidad[i] == rc.CalificacionC.Limpio.name:
            
            if resultado[i] == rc.ResultadoB.Ganado.name:
                ganadoLimpio += 1
            if resultado[i] == rc.ResultadoB.Perdido.name:      

                perdidoLimpio += 1

        
            if resultado[i] == rc.ResultadoB.Penalizado.name:
        
                penalizados += 1
            
        if calidad[i] == rc.CalificacionC.Desorganizado.name:
            if resultado[i] == rc.ResultadoB.Ganado.name:
                perdidoDesorganizado += 1
            if resultado[i] == rc.ResultadoB.Perdido.name:
                perdidoLimpio += 1
            
            if resultado[i] == rc.ResultadoB.Penalizado.name:
                penalizados += 1

    bd.insertLineout(rD.temporada,rD.fecha,ganadoLimpio,ganadoDesorganizado,perdidoLimpio,perdidoDesorganizado,penalizados)


def incidenciaPuntuacion():
    tipoTry = rD.incidenciaPartido["Puntuación","Tipo-Try"].dropna()
    equipo = rD.incidenciaPartido["Puntuación","Equipo"].dropna()
    jugador = rD.incidenciaPartido["Puntuación","Jugador"]
    minuto = rD.incidenciaPartido["Puntuación","Minuto"].dropna()

    for i in range(0,len(tipoTry)):        
 
        if (rD.info["Equipo"] == equipo[i]).bool():
               
            bd.insertScore(rD.temporada,rD.fecha,tipoTry[i],jugador[i],minuto[i])
        else:
            
            bd.insertScoreAgainstUs(rD.temporada,rD.fecha,tipoTry[i],minuto[i])
   
 

def incidenciaDisciplina():
    tipoIndisciplina = rD.incidenciaPartido["Indisciplina","Tipo Indisciplina"].dropna()
    jugador = rD.incidenciaPartido["Indisciplina","Jugador"].dropna()
   

    for i in range(0,len(jugador)):
 
        bd.insertDiscipline(rD.temporada,rD.fecha,tipoIndisciplina[i],jugador[i])


def incidenciaJugadores():
    jugadores = rD.jugadoresPartido["Nombre"]
    for i in range(0,len(jugadores)):
        bd.insertJugador(rD.temporada,rD.fecha,jugadores[i])
    
import CargaDeDatosPartido.analisis as an
import CargaDeDatosPartido.readData as rD
import analisisTemporadas.analisisTemporadas as aT
import analisisTemporadas.Documentacion.analisisEscritura as aE
import analisisTemporadas.database as dB
def cargarDatos():
    tablasCreadas = False,

    if not tablasCreadas:
        dB.crearTablas()
        tablasCreadas = True
    
    #Tabla Temporada
    
    an.resultadoPartido()
    #Tabla Kick
    an.incidenciasKick()
    #Tabla Lineout
    an.incidenciaLineout()  
    #Tabla Disciplina
    an.incidenciaDisciplina()
    #Tabla Pase
    an.incidenciaPase()

    an.incidenciaRuckMaul()
    #Tabla Scrum
    an.incidenciasScrum()
    

    
    #Tabla Jugadores
    an.incidenciaJugadores()     
    
    #Tabla Tackle
    an.incidenciasTackle()
    
    #Tabla Puntuacion
    an.incidenciaPuntuacion()
        

def informeTemporada(temporada):
    
   
    
    
    aT.Kicks(temporada)
    aT.Pases(temporada)
    aT.Puntuacion(temporada)
    aT.PuntuacionEnContra(temporada) 
    aT.Lineouts(temporada)
    aT.Scrum(temporada)
    aT.Tackles(temporada)
    aT.RuckAndMaul(temporada)


    aT.Efectividad()

    


def main():
    cargarDatos()
    
    temporada = 2023
    informeTemporada(temporada)


 


if __name__ == "__main__":
    main()


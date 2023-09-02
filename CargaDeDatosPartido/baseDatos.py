import mysql.connector
from mysql.connector import errorcode



cnx = mysql.connector.connect(user='', password='',
                              host='', 
                              database='Rugby')


cursor = cnx.cursor()


def insertTemporada(temporada,fecha,resultado):
    

    addFecha = ("INSERT INTO Temporada (Año, Fecha, Resultado) VALUES (%s,%s,%s)")

    a = (temporada,fecha,resultado)

    cursor.execute(addFecha,a)

    cnx.commit()


def insertScrum(temporada, fecha, ganadoLimpio,ganadoDesorganizado,perdidoLimpio,perdidoDesorganizado,penalizados):
    addScrum = ("INSERT INTO Scrum (Temporada, Fecha, GanadoLimpio, GanadoDesorganizado, PerdidoLimpio, PerdidoDesorganizado, Penalizados) VALUES (%s,%s,%s,%s,%s,%s,%s)")

    a = (temporada, fecha, ganadoLimpio,ganadoDesorganizado,perdidoLimpio,perdidoDesorganizado,penalizados)

    cursor.execute(addScrum,a)
    cnx.commit()

def insertLineout(temporada, fecha, ganadoLimpio,ganadoDesorganizado,perdidoLimpio,perdidoDesorganizado,penalizados):

    addLineout = ("INSERT INTO Lineout (Temporada, Fecha, GanadoLimpio, GanadoDesorganizado, PerdidoLimpio, PerdidoDesorganizado, Penalizados) VALUES (%s,%s,%s,%s,%s,%s,%s)")
    
    a = (temporada, fecha, ganadoLimpio,ganadoDesorganizado,perdidoLimpio,perdidoDesorganizado,penalizados)

    cursor.execute(addLineout,a)
    cnx.commit()

def insertTackle(temporada,fecha,ofensivo,neutral,pasivo,errado):
    addTackle = ("INSERT INTO Tackle (Temporada, Fecha, Ofensivo, Neutral, Pasivo, Errado) VALUES (%s,%s,%s,%s,%s,%s)")

    a = (temporada,fecha,ofensivo,neutral,pasivo,errado)
    cursor.execute(addTackle,a)
    cnx.commit()


def insertKick(temporada,fecha,suelo,atrapado,touch):
    addKick = ("INSERT INTO Kick (Temporada, Fecha, Suelo, Atrapado, Touch ) VALUES (%s,%s,%s,%s,%s)")
    a = (temporada,fecha,suelo,atrapado,touch)

    cursor.execute(addKick,a)
    cnx.commit

def insertRuckMaul(temporada,fecha,rapidoGanado,lentoGanado,rapidoPerdido,lentoPerdido,Penalizado):
    addRuckMaul = ("INSERT INTO RuckAndMaul (Temporada, Fecha, RapidoGanado, LentoGanado, RapidoPerdido, LentoPerdido, Penalizado) VALUES (%s,%s,%s,%s,%s,%s,%s)")

    a = (temporada,fecha,rapidoGanado,lentoGanado,rapidoPerdido,lentoPerdido,Penalizado)

    cursor.execute(addRuckMaul,a)
    cnx.commit


def insertPass(temporada,fecha,precisoAtrapado,precisoCaido,imprecisoAtrapado,imprecisoCaido,imprecisoForward):
    addPass = ("INSERT INTO Pase (Temporada, Fecha, PrecisoAtrapado, PrecisoCaido, ImprecisoAtrapado, ImprecisoCaido, ImprecisoForward) VALUES (%s,%s,%s,%s,%s,%s,%s)")

    a = (temporada,fecha,precisoAtrapado,precisoCaido,imprecisoAtrapado,imprecisoCaido,imprecisoForward)

    cursor.execute(addPass,a)
    cnx.commit


def insertScore(temporada,fecha,tipoPuntuacion,jugador,minuto):
  
    addScore =  ("INSERT INTO Puntuacion (Temporada, Fecha, TipoPuntuacion, Jugador, Minuto) VALUES(%s,%s,%s,%s,%s)")
    
    a = (temporada,fecha,tipoPuntuacion,jugador,int(minuto))
    cursor.execute(addScore, a)
    cnx.commit()



def insertScoreAgainstUs(temporada,fecha,tipoPuntuacion,minuto):
    addScoreAgainstUs = ("INSERT INTO PuntuacionEnContra (Temporada, Fecha, TipoPuntuacion, Minuto) VALUES (%s,%s,%s,%s)")

    a=(temporada,fecha,tipoPuntuacion,int(minuto))
    cursor.execute(addScoreAgainstUs, a)
    cnx.commit()



def insertDiscipline(temporada,fecha,indisciplina,jugador):
  
    addDiscipline = ("INSERT INTO Disciplina (Temporada, Fecha, Indisciplina, Jugador) VALUES (%s,%s,%s,%s)")

    a = (temporada,fecha,indisciplina,jugador)
    

    cursor.execute(addDiscipline,a)
    cnx.commit
 


def insertJugador(temporada,fecha,nombreJugador):
    consulta_insert = "INSERT INTO Jugadores (Temporada, Fecha, NombreJugador) VALUES (%s, %s, %s)"
    datos_jugador = (temporada, fecha, nombreJugador)

    # Ejecutar la consulta
    cursor.execute(consulta_insert, datos_jugador)

    # Hacer commit para guardar los cambios
    cnx.commit()

    


import mysql.connector
from mysql.connector import errorcode
import pandas as pd


cnx = mysql.connector.connect(user='', password='',
                              host='', 
                              database='Rugby')



cursor = cnx.cursor()

def crearTablas():
     # Lista de sentencias SQL para crear las tablas
    sentencias_sql = [
        """
        CREATE TABLE Temporada (
            Año VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            Resultado VARCHAR(50),
            PRIMARY KEY (Año, Fecha)
        );
        """,
        
        """
        CREATE TABLE Scrum (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            GanadoLimpio INT,
            GanadoDesorganizado INT,
            PerdidoLimpio INT,
            PerdidoDesorganizado INT,
            Penalizados INT,
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",

        """
        CREATE TABLE Tackle (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            Ofensivo INT,
            Neutral INT,
            Pasivo INT,
            Errado INT,
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",

      
        """     
        CREATE TABLE Pase (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            PrecisoAtrapado INT,
            PrecisoCaido INT,
            ImprecisoAtrapado INT,
            ImprecisoCaido INT,
            ImprecisoForward INT,
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );
        """,
        """CREATE TABLE RuckAndMaul (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            RapidoGanado INT,
            LentoGanado INT,
            RapidoPerdido INT,
            LentoPerdido INT,
            Penalizado INT,
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",

        """
        CREATE TABLE Lineout (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            GanadoLimpio INT,
            GanadoDesorganizado INT,
            PerdidoLimpio INT,
            PerdidoDesorganizado INT,
            Penalizados INT,
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",
        """
        CREATE TABLE Puntuacion (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            TemporadaPuntuacion VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            TipoPuntuacion VARCHAR(50),    
            Jugador VARCHAR(50),
            Minuto INT,    
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",

        """
        CREATE TABLE PuntuacionEnContra (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            TipoPuntuacion VARCHAR(50),
            Minuto INT NOT NULL,
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",

        """
        CREATE TABLE Disciplina (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            Indisciplina VARCHAR(50),
            Jugador VARCHAR(50),
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );"""

        """
        CREATE TABLE Kick(
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            Suelo INT,
            Touch INT,
            Atrapado INT,
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",
        """
        CREATE TABLE Jugadores(

            Id INT AUTO_INCREMENT PRIMARY KEY,
            Temporada VARCHAR(50) NOT NULL,
            Fecha VARCHAR(50) NOT NULL,
            NombreJugador VARCHAR(256),   
            FOREIGN KEY (Temporada, Fecha) REFERENCES Temporada(Año, Fecha)
        );""",
    ]
    
    try:
        # Ejecutar cada sentencia SQL
        for sql in sentencias_sql:
            cursor.execute(sql)
            print("Tabla creada exitosamente")
        
        # Confirmar los cambios en la base de datos
        cnx.commit()
    
    except mysql.connector.Error as err:
        print("Error:", err)
        # Revertir los cambios en caso de error
        cnx.rollback()
    
    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        cnx.close()




def readAll():
    selectResultado = ("SELECT * FROM Temporada")

    

    a = cursor.execute(selectResultado)
    results = cursor.fetchall()

    # Cerrar el cursor y liberar los resultados

    return results


def readDiscipline(temporada):
 

    sql_query = '''
        SELECT Jugador,  SUM(Expulsiones) AS CantidadExpulsiones, SUM(SinBin) AS CantidadSinBin
        FROM
        (
            SELECT dis.Jugador, COUNT(dis.Indisciplina) as SinBin, 0 as Expulsiones
            FROM Disciplina as dis 
            WHERE dis.Indisciplina = "Sin Bin" AND dis.Temporada = %s 
            GROUP BY Jugador

            UNION ALL

            SELECT dis.Jugador, 0 as SinBin, COUNT(dis.Indisciplina) as Expulsiones
            FROM Disciplina as dis 
            WHERE dis.Indisciplina = "Expulsion" AND dis.Temporada = %s
            GROUP BY Jugador
        ) AS SubconsultaConUnion
        GROUP BY Jugador
        ORDER BY CantidadExpulsiones DESC;
        '''

    try:
            # Ejecuta la consulta
            temp = [(temporada),(temporada)]

            cursor.execute(sql_query,temp)

            # Obtén los resultados
            resultados = cursor.fetchall()
            
            # Imprime los resultados
            return resultados

    except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            return 

 
def readKicks(temporada):
    query = ("Select Fecha, Suelo, Atrapado, Touch from Kick where Temporada = (%s)")
    temp = [(temporada)]

    a = cursor.execute(query,temp)
    results = cursor.fetchall()
    
    return results

def readLineout(temporada):
    query = ("Select Fecha, GanadoLimpio,GanadoDesorganizado,PerdidoLimpio,PerdidoDesorganizado,Penalizados FROM Lineout where Temporada = (%s)")

    temp = [(temporada)]

    a = cursor.execute(query,temp)
    results = cursor.fetchall()

    return results

def readPase(temporada):
    query = ("SELECT Fecha, PrecisoAtrapado,PrecisoCaido,ImprecisoAtrapado,ImprecisoCaido,ImprecisoForward FROM Pase WHERE Temporada = (%s)")
    temp = [(temporada)]

    a = cursor.execute(query,temp)
    results = cursor.fetchall()

    return results


def puntuacionCuartiles(temporada):
    query = ('''SELECT
            Fecha,
            COUNT(CASE WHEN Minuto <= 20 THEN 1 END) AS "Try o Try Penal (0-20)",
            COUNT(CASE WHEN Minuto > 20 AND Minuto <= 40 THEN 1 END) AS "Try o Try Penal (20-40)",
            COUNT(CASE WHEN Minuto > 40 AND Minuto <= 60 THEN 1 END) AS "Try o Try Penal (40-60)",
            COUNT(CASE WHEN Minuto > 60 AND Minuto <= 80 THEN 1 END) AS "Try o Try Penal (60-80)"
        FROM Puntuacion
        WHERE TipoPuntuacion IN ('Try', 'Try Penal') AND Temporada = (%s)
        GROUP BY Fecha;

            '''
        )
    temp = [(temporada)]
    cursor.execute(query,temp)
    results = cursor.fetchall()

    return results


def puntuacionCuartilesEnContra(temporada):
    query = ('''SELECT
                TodasLasFechas.Fecha,
                COALESCE(SUM(CASE WHEN PEC.Minuto <= 20 THEN 1 END), 0) AS "Try o Try Penal (0-20)",
                COALESCE(SUM(CASE WHEN PEC.Minuto > 20 AND PEC.Minuto <= 40 THEN 1 END), 0) AS "Try o Try Penal (20-40)",
                COALESCE(SUM(CASE WHEN PEC.Minuto > 40 AND PEC.Minuto <= 60 THEN 1 END), 0) AS "Try o Try Penal (40-60)",
                COALESCE(SUM(CASE WHEN PEC.Minuto > 60 AND PEC.Minuto <= 80 THEN 1 END), 0) AS "Try o Try Penal (60-80)"
                        
                FROM (
                    SELECT DISTINCT Fecha
                    FROM PuntuacionEnContra
                    WHERE Temporada = (%s)
                ) AS TodasLasFechas
                LEFT JOIN PuntuacionEnContra AS PEC ON TodasLasFechas.Fecha = PEC.Fecha
                    AND PEC.TipoPuntuacion IN ('Try', 'Try Penal')

                GROUP BY TodasLasFechas.Fecha;

            '''
        )
    temp = [(temporada)]
    cursor.execute(query,temp)
    results = cursor.fetchall()

    return results

def readPuntuacion(temporada):
    query = ("SELECT Fecha,TipoPuntuacion,Jugador,Minuto from Puntuacion WHERE Temporada = (%s)")
    temp = [(temporada)]

    a = cursor.execute(query,temp)
    results = cursor.fetchall()

    return results



def readPuntuacionEnContra(temporada):
    query = ("SELECT Fecha,TipoPuntuacion,Minuto FROM PuntuacionEnContra WHERE Temporada = (%s)")
    temp = [(temporada)]
    

    a = cursor.execute(query,temp)
    results = cursor.fetchall()
    print(results)
    return results

def readRuckAndMaul(temporada):
    query = ("SELECT Fecha, RapidoGanado,LentoGanado,RapidoPerdido,LentoPerdido,Penalizado FROM RuckAndMaul WHERE Temporada = (%s)")
    temp = [(temporada)]

    a = cursor.execute(query,temp)
    results = cursor.fetchall()

    return results

def readScrum(temporada):
    query = ("SELECT Fecha, GanadoLimpio,GanadoDesorganizado,PerdidoLimpio,PerdidoDesorganizado,Penalizados FROM Scrum WHERE Temporada = (%s)")
    temp = [(temporada)]

    a = cursor.execute(query,temp)
    results = cursor.fetchall()

    return results
def readTackle(temporada):
    query = ("SELECT Fecha,Ofensivo,Neutral,Pasivo,Errado from Tackle WHERE Temporada = (%s)")
    temp = [(temporada)]

    a = cursor.execute(query,temp)
    results = cursor.fetchall()

    return results
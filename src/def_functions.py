import pandas as pd
import matplotlib.pyplot as plt
nba=pd.read_csv("./output/basket_functions.csv")


def compare(P1, P2, stats=['GP', 'MIN', '2PM', '2PA', '3PM',
       '3PA', '1PM', '1PA', 'TOV', 'PF', 'ORB', 'DRB', 'REB', 'AST', 'STL',
       'BLK', 'PTS']):

    """Esta función se encarga de comparar las estadísticas de 
    los dos jugadores que queremos consultar."""

    results={"Game played":(P1[stats[0]], P2[stats[0]]),
            "Minutes played":(P1[stats[1]], P2[stats[1]]),
            "2 points made":(P1[stats[2]], P2[stats[2]]),
            "2 points attemps":(P1[stats[3]], P2[stats[3]]),
            "3 points made":(P1[stats[4]], P2[stats[4]]),
            "3 points attemps":(P1[stats[5]], P2[stats[5]]),
            "1 points made":(P1[stats[6]], P2[stats[6]]),
            "1 points attemps":(P1[stats[7]], P2[stats[7]]),
            "Turnovers":(P1[stats[8]], P2[stats[8]]),
            "Personal foults":(P1[stats[9]], P2[stats[9]]),
            "Offensive Rebounds":(P1[stats[10]], P2[stats[10]]),
            "Defensive Rebounds":(P1[stats[11]], P2[stats[11]]),
            "Rebounds":(P1[stats[12]], P2[stats[12]]),
            "Assists":(P1[stats[13]], P2[stats[13]]),
            "Steals":(P1[stats[14]], P2[stats[14]]),
            "Block":(P1[stats[15]], P2[stats[15]]),
            "Points":(P1[stats[16]], P2[stats[16]])}
    
    return results


def percentage (Player, stats=['GP', 'MIN','2PM', '2PA', '3PM',
       '3PA', '1PM', '1PA']):

    """Esta función se encarga de devolver el % de aciertos en tiros 
    y los minutos del jugador que queramos consultar"""
    
    res={"%_acierto en tiros de campo":(Player[stats[2]]/ Player[stats[3]]),
         "%_acierto en triples":(Player[stats[4]]/ Player[stats[5]]),
         "%_acierto en tiros libres":(Player[stats[6]]/ Player[stats[7]]),
         "Minutes":(Player[stats[1]]/ Player[stats[0]])}
 
    return res


def describe(stat):

    """Esta función devuelve la descripción estadística
    de la estadística que queramos consultar"""

    return pd.DataFrame(nba[stat].describe().T)


def choose_team(team):

    """Esta función devuelve un dataframe del equipo que queremos ver"""

    return nba[nba["Team"]==team]


def team_stats(stat):

    """Esta función devuelve un dataframe con la suma de la estadística
    que queremos ver agrupada por equipo, de modo que podamos comparar
    con un simple vistazo que equipos tienen mejores stats""" 

    return nba.groupby(["Team"]).agg({stat:"sum"})
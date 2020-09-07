# Storytelling-Project

![nba-los-angeles-lakers](nba-los-angeles-lakers.png) 

El objetivo de este proyecto es vender nuestros servicios de ánalisis de datos a una franquicia de la NBA, en este caso se trata de nada mas y nada menos que de los Ángeles Lakers. Para ello, vamos a realizar una limpieza de la base de datos obtenida, posteriormente analizaremos los datos de Los Lakers con el vigente campeón de liga, Toronto Raptors, para finalmente pasar a realizar un ánalisis comparativo con el resto de equipos de la liga.  


## Hipótesis.

¿Puede ayudar el ánalisis de datos a mejorar las estadísticas de un equipo como Los Ángeles Lakers y por ende ayudar a la consecución de mejores resultados?


## Como se ha realizado.

Se ha importado una extensa base de datos con todas las estadísticas de los jugadores de la NBA desde la temporada 2010, en este caso se trata de un documento csv descargado del siguiente enlace, https://www.kaggle.com/jacobbaruch/basketball-players-stats-per-season-49-leagues

Para realizar la limpieza y manipulación de datos, así como la elaboración de DataFrames he importado el módulo Panda.

Se ha importado también el módulo re, para realizar pequeñas modificaciones con regex.

Se han realizado funciones lambda y han sido aplicadas a los data frames mediante el uso de la función apply().

Se han realizado funciones externas en un archivo .py que posteriormente han sido importadas y llamadas desde jupyter notebook.

Se han importado las librerías seaborn y matplotlib para la representación gráfica de los datos.


## Conclusión.

### Ánalisis 1vs1 entre Los Ángeles Lakers y Toronto Raptors

De todos los datos analizados, podemos observar que Toronto Raptors, equipo que ya cuenta con servicios de Big Data y ánalisis de datos, mejora en casi todos los aspectos a Los Ángeles Lakers, sólo existen 2 puntos en los que son inferiores, y uno de esos dos, en concreto las asistencias, no son un dato muy a tener en cuenta, ya que como hemos visto, Toronto Raptors tiene un juego mucho más asociativo y las asistencias repercuten directamente sobre la cantidad de pérdidas de balón.


### Ánalisis 1vsResto de la liga.

De los datos analizados, observamos que de los 30 equipos que forman la NBA, Los Ángeles Lakers ocupan las siguientes posiciones por estadística:
    
    - Anotaciones de 2 puntos: 10ª posición.
    - Intentos de 2 puntos: 12ª posición.
    - Anotaciones de 3 puntos: 10ª posición.
    - Intentos de 3 puntos: 4ª posición.
    - Anotaciones de 1 puntos: 18ª posición.
    - Intentos de 1 puntos: 13ª posición.
    - Perdidas de balón: 8ª posición.
    - Faltas personales: 10ª posición.
    - Rebotes ofensivos: 19ª posición.
    - Rebotes defensivos: 9ª posición.
    - Rebotes: 13ª posición
    - Asistencias: 19ª posición.
    - Robos: 17ª posición.
    - Bloqueos: 8ª posición.
    - Puntos: 12ª posición.

Si hiciesemos una media de los anteriores datos, nos encontramos con que una franquicia del nivel de Los Ángeles Lakers, está en la posición 12ª de la liga, esto quiere decir que el equipo tiene que mejorar en todos los aspectos anteriores.


### ¿En que puede ayudar el ánalisis de datos a conseguir estos objetivos?.

El ánalisis de datos puede ayudar a la consecución de estos objetivos:
    - Observar cuales son los puntos fuertes y débiles del equipo.
    - Observar que jugadores tienen mejores estadísticas en cada apartado y potenciar su uso en el transcurso de los partidos.
    - Buscar jugadores en el mercado que tengan las mejores estadísticas en aquellos puntos débiles que el equipo debe mejorar.
    - Analizar a los equipos rivales para forzarles a que fallen, haciendoles utilizar aquellas estadísticas en las que sabemos que son débiles.
    - Y un sin fín de posibilidades que podrían hacer que su franquicia  triunfase durante los próximos años.

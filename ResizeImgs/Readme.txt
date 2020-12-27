Instrucciones de uso archivos de recorridos

scenes.txt:
el archivo scenes tiene el siguiente formato para agregar botones de escenas:

Nombre de la escena:numero de esfera(rotacion en vertical, rotacion horizontal)

ruta.txt:
el archivo de ruta tiene formato tipo json de la siguiente manera:

{"scene":0,"direction":1,"rotaY":0,"rotaX":5,"speed":10,"maxTime":15}
primero el numero de la esfera
dreccion va 1 = derecha y 0 = izquierda
rotaion Y es la rotacion horizontal de la camara
rotaion X es la rotacion vertical de la camara
speed velocidad en la que rota la camara
maxTime es el tiempo en la escena, al acabar cambia de escena si hay mas
de lo contrario se quedara en la escena hasta que lo interrumpas

names.txt
son las posiciones de cada esfera con sus siguientes esferas, el formato al final indica que tipo de imagen es p dado el caso que se cambie de formato

config.txt
el archivo config lo principal es la primer escena en la que quieres empezar y alfinal del archivo los botones que quieras activar

carpeta de gallery:
usa esta carpeta para meter imagenes que quieras visualizar en la galeria cuando la actives en los botones, las fotos deven nombres alfanumericos empezando desde cero en el orden que las quieras mostrar ya que el recorrido no sabe el nombre de la imagenes a cargar

Nota: para ver esfera y rotaciones entrar a un recorrido y usa la tecla "V" para visualizar la esfera


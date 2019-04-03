# gyovana
from _spy.vitollino.main import Cena, Elemento, Texto
elemento_gato = "https://sc.mogicons.com/l/garfield-172.png"

def Historia():
	cenaHouse = Cena(img = "https://i.pinimg.com/originals/3f/36/7f/3f367f727042a6c6b03301167d113104.jpg")
	gato = Elemento (img = elemento_gato,
                      tit="Gato Laranja",
                      style = dict( left=150, top =60, width=60, height=200))
	cenaHouse.vai()
Historia()
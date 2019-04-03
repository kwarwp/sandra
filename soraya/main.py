# Larissa dos Anjos
from _spy.vitollino.main import Cena, Elemento, Texto
elemento_gato = "https://sc.mogicons.com/l/garfield-172.png"

def Historia():
	cenaHouse= Cena(img ="http://jogosindie.com/wp-content/uploads/2014/08/lava.png")
	gato = Elemento (img = elemento_gato,
                      tit="Gato Laranja",
                      style = dict( left=150, top =60, width=60, height=200))
	gato.entra(cenaHouse)
	cenaHouse.vai()
Historia()
    
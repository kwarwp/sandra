# Lana Soooooouza
from _spy.vitollino.main import Cena, Elemento, Texto
elemento_alien = "https://cdn3.iconfinder.com/data/icons/pictofoundry-pro-vector-set/512/Alien-512.png"

def Historia():
	cenaHouse = Cena(img = "https://img.elo7.com.br/product/zoom/1360BB4/painel-floresta-g-frete-gratis-fundo-festa-infantil.jpg")
	alien = Elemento ( img = elemento_alien,
                       tit="Alien Laranja",
                       style = dict( left=150, top =60, width=60, height=200))
	alien.entra(cenaHouse)
	cenaFloresta.vai
Historia() 
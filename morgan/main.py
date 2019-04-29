#davy azaredo
from _spy.vittolino.main import Cena, Elemento, Texto
elemento_ninja = "http://pluspng.com/img-png/ninja-hd-png-ninja-images-cnmuqi-hd-wallpapers-306.png"

def Historia():
	cenaHouse= Cena(img = "https://img.elo7.com.br/product/zoom/10C700C/painel-floresta-g-frete-gratis-painel-impresso.jpg")
	ninja = Elemento (img=elemento_ninja, 
                       tit="ninja preto",
                       style = dict( left=150, top =60, width=60, height=200))
	ninja.entra(cenaHouse)
	txtNinja = Texto(cenaHouse,
                       "Vou lutar!")
	ninja.vai = txtNinja.vai
	cenaHouse.vai()
Historia()
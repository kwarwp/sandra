# Pedro Henrique Baridoti Coelho
from _spy.vitollino.main import Cena, Elemento, Texto
Elemento_deadpool="https://vignette.wikia.nocookie.net/xmenmovies/images/7/7c/Deadpool_%28Thumbs_Up_-_Transparent%29.png/revision/latest?cb=20170324222613"

def Historia():
	cenaHouse = Cena(img = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Wrestling%2C_Pavilh%C3%A3o_Atl%C3%A2ntico_1.jpg/250px-Wrestling%2C_Pavilh%C3%A3o_Atl%C3%A2ntico_1.jpg")
	Deadpoo = Elemento(img=Elemento_deadpool,
                        tit="Deadpoo",
                        style = dict(left=150,top =60,width=60,height=200))
	Deadpoo.entra(cenaHouse)
	cenaHouse.vai()
Hitoria()
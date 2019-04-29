# gabriela ribeiro
from _spy.vitollino.main import Cena, Elemento, Texto
elemento_snoopy = "http://www.specialdog.com/snoopygarfield/wp-content/themes/snoopygarfield/images/snoopy.png"

def Historia():
	cenaQuarto = Cena(img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCx-MkZzcdk8uwwRpah7bUzH65QoU0dIxen-7bJp9COzSLi1CR")
	snoopy = Elemento (img = elemento_snoopy,
                        tit="snoopy branco",
                        style = dict( left=150, top=60, width=60,height=200))
	snoopy.entra(cenaQuarto)
	txtSnoopy = Texto( cenaQuarto,
                       "As school kids went for an excursion. When they reached the cave, they lit up like candles and began to explore the mountain. Tom and Amy got lost, but found Injun Joe hiding the treasure.")
	snoopy.vai = txtSnoopy.vai
	cenaQuarto.vai()    
Historia()
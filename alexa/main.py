# jorge
from _spy.vitollino.main import Cena, Elemento, Texto
elemento_Bart = "https://sc.mogicons.com/l/Bart-172.png"

def Historia():
	cenaHouse= Cena(img = "http://ossimpsons-orpg.weebly.com/uploads/1/2/9/6/12964529/850096305.jpg?554")    
	bart = Elemento (img = elemento_Bart,
                  tit="Bart amarelo",
                  style = dict(left 150,top=60,width=60, height=200))
	bart.entra(cenaHouse) 
	txtBart = Texto( cenaHouse,
                 "Estou com fome!")
	bart.vai= txtBart.vai
	cenaHouse.vai()                    
Historia()
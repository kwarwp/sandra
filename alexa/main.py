# jorge
from _spy.vitollino.main import Cena, Elemento, Texto
elemento_Bart = "https://static.simpsonswiki.com/images/8/83/Bart_skate_-_s25_artwork.png"

def Historia():
	cenaHouse= Cena(img = "http://ossimpsons-orpg.weebly.com/uploads/1/2/9/6/12964529/850096305.jpg?554")    
	bart = Elemento (img = elemento_Bart,
                      tit="Bart amarelo",
                      style = dict(left=150,top=60,width=60, height=200))
	bart.entra(cenaHouse) 
	txtBart = Texto( cenaHouse,
                 "The Pirates Return Home. No domingo, a cidade foi para o funeral do três amigos, de repente eles apareceram na igreja todos sujos . Os parentes ficaram muito felizes e Amy também. Tom voltou a ir para a escola e nesse dia salvou sua amiga de apuros que iria entrar como o professor. On Sunday, the city went to the funeral of the three friends, suddenly they appeared in the church all dirty. The relatives were very happy and so was Amy. Tom went back to school and on that day saved his friend from trouble who would enter as the teacher.")
	bart.vai= txtBart.vai
	cenaHouse.vai()                    
Historia()
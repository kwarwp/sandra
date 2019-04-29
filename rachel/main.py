#danielmartins
from _spy.vittolino.main import Cena, Elemento, Texto
elemento_kaneki = "https://data.whicdn.com/images/204362721/superthumb.png?t=1445214745"
  
def Historia():
	cenaKaneki= Cena(img = "https://i.ytimg.com/vi/_-GI_EG7UWM/hqdefault.jpg")
	kaneki=Elemento(img=elemento_kaneki,
                     tit="kaneki preto",
                     style=dict( left=150, top =60, width=60, height=200)) 
	kaneki.entra(cenaKaneki)                                    
	txtKanrki=Texto(cenaKaneki,
                     "Eleta com fome ")

	kaneki.vai=txtkaneki.vai
	cenakaneki.vai()  
    
Historia()  
# Pedro Henrique Barros	
from _spy.vitollino.main import Cena, Elemento, Texto
elemento_night_wing="https://vignette.wikia.nocookie.net/nerdologiaheroespowers/images/2/23/Asa_Noturna.png/revision/latest?cb=20180206000240&path-prefix=pt-br"
def Historia():
	cenaTowertitan = Cena(img = "https://www.google.com.br/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiuo7fonJ7hAhWFD7kGHfJ_ChYQjRx6BAgBEAU&url=http%3A%2F%2Fforums.daybreakgames.com%2Fdcuo%2Findex.php%3Fthreads%2Fnew-teen-titans-tower-look.296433%2F&psig=AOvVaw0VUZ1umKrPFlebIBx6AdDT&ust=1553635326971397")
	night_wing= Elemento(img = elemento_night_wing,
                          tit="Night Wing one",
                          style = dict( left=100, top=60, width=60, heigt=150))
	night_wing.entra(cenaTowertitan)
	txtNight_Wing = Texto (cenaTowertitan,
                             "Estou em casa de novo!")
	night_wing.vai = txtNight_Wing.vai
	cenaTowertitan.vai()
Historia()
pythonxu={"ataque":30,"defesa":20,"vida":100} #N:0   
fegamel={"ataque":40,"defesa":40,"vida":70} #N:1
deusvult={"ataque":50,"defesa":20,"vida":80} #N:2         # Os 5 primeiros são pokemons de valores "mais fracos"
bubbassalto={"ataque":55,"defesa":20,"vida":75} #N:3
charmandela={"ataque":35,"defesa":45,"vida":70} #N:4
feche={"ataque":40,"defesa":30,"vida":110} #N:5
celera={"ataque":50,"defesa":50,"vida":80} #N:6
alohomora={"ataque":60,"defesa":30,"vida":90} #N:7        # 5 pokemons intermediários
cartertorta={"ataque":65,"defesa":30,"vida":85} #N:8
zubate={"ataque":45,"defesa":55,"vida":80} #N:9
roberstoise={"ataque":50,"defesa":40,"vida":120} #N:10
karcana={"ataque":60,"defesa":60,"vida":90} #N:11
agaraga={"ataque":70,"defesa":40,"vida":100} #N:12      # Os mais fortes
viguvigu={"ataque":75,"defesa":40,"vida":95} #N:13
fairinhow={"ataque":55,"defesa":65,"vida":90} #N:14

insperdex=[["pythonxu",50,20,100,"N:0"],["fegamel",40,40,70,"N:1"],["deusvult",55,10,50,"N:2"],["bubbassalto",55,20,80,"N:3"],["charmandela",35,45,70,"N:4"],
["feche",40,30,110,"N:5"],["celera",50,50,80,"N:6"],["alohomora",60,30,90,"N:7"],["cartertorta",65,30,90,"N:8"],["zubate",45,55,80,"N:9"],["robertoise",50,40,120,"N:10"],
["karcana",60,60,90,"N:11"],["agaraga",70,40,100,"N:12"],["viguvigu",75,40,95,"N:13"],["fairinhow",55,65,90,"N:14"]]
insperdéx=[]*20
XP=0
LV=0

import time
import random
import pickle

command="NADA"
pauseplay="JOGAR"

def batalha(mon,ini,insperdéx,insperdex):
	print("Um Inspermón selvagem apareceu!")
	time.sleep(1.5)
	print("Seu Inspermon: {},ataque:{},defesa:{},vida:{}".format(insperdex[mon][0],insperdex[mon][1],insperdex[mon][2],insperdex[mon][3]))
	time.sleep(1)
	print("""inspermon selvagem: {},
		               ataque: {},
		               defesa: {},
		               vida: {}""".format(insperdex[ini][0],insperdex[ini][1],insperdex[ini][2],insperdex[ini][3]))
	
	vidaini=insperdex[ini][3]
	vidajog=insperdex[mon][3]
	
	while vidajog>0 and vidaini>0:
        
		if vidajog>0 and vidaini>0:
			q= str(input("O que você quer fazer: 'lutar' ou 'fugir'?")).upper()
        
		if q=="LUTAR":
			print("Você atacou!")
			w=random.randint(0,19)
        
			if w==10:       #ataque crítico!
				print("Ataque C R Í T I C O!!!")
            
				if ((insperdex[mon][1]*1.5)-(insperdex[ini][2]))<0:
					print("O Inspermon inimigo conseguiu se defender!")
            
				else:
					vidaini=(vidaini)-((insperdex[mon][1]*1.5)-(insperdex[ini][2]))
					print("A vida do seu inimigo agora é de {}".format(vidaini))

			else:    #ataque normal
                
				if ((insperdex[mon][1])-(insperdex[ini][2]))<=0:
					print ("O inspermon inimigo se defendeu do ataque!")
                
				else:
					vidaini=vidaini-((insperdex[mon][1])-(insperdex[ini][2]))
					print("A vida do seu inimigo agora é de: {}".format(vidaini))
		
			if vidaini>0:
				print ("Seu oponente ataca!")
				time.sleep(1)
				if (insperdex[ini][1]-insperdéx[mon][2])<=0:
					print("O seu Inspermon se defendeu do ataque inimigo!")
				else:	
					vidajog=vidajog-(insperdex[ini][1]-insperdéx[mon][2])
					print("A vida de seu Inspermon agora é de: {}".format(vidajog))
               
	 
			if vidaini<=0:
				print ("Você venceu!!!")
				if not(insperdex[ini] in insperdéx):
					insperdéx[ini]=(insperdex[ini])
					print("Parabéns!!! Você capturou um novo Inspermon!!!")
				command="NADA"
        	
			if vidajog<=0:
				print("Você perdeu...")
				command="DERROTA"

		if q=="FUGIR":
			print("Você fugiu!")
			command="FUGA"
			break
    
	
	return (command)

def loopjogo(command,mon,insperdéx,insperdex,XP,LV,batalha):

	if command=="DORMIR":
		print ("MENU")
		pauseplay=str(input("Escreva 'jogar' para retomar o jogo ou 'salvar' para salvar sua sessão de jogo e sair: ")).upper()
		
	if command=="NADA":
		pass 
		
	if command=="FUGA":
		pass
	
	while command!="DORMIR" and command!="DERROTA":
		
		command=str(input("Agora,o que voce quer fazer?: ")).upper()
	
		for h in range (3):
			print("...")
			time.sleep(1)

		if command=="PASSEAR":
			
			if LV<5:	
				ini=random.randint(0,5)
				command=batalha(mon,ini,insperdéx,insperdex)

			if LV>=5 and LV<10:
				ini=random.randint(0,9)
				command=batalha(mon,ini,insperdéx,insperdex)

			if LV>=10 and LV<15:
				ini=random.randint(0,14)
				command=batalha(mon,ini,insperdéx,insperdex)
			
			if command=="NADA":
				XP=XP+1
				print("Seu Inspermon ganhou experiência!")
		
			if XP==10:
				for h in range (3):
					print("...")
					time.sleep(1)
				for i in range(1,3):
					insperdéx[mon][i]=insperdéx[mon][i]+5
				print("Seu Inspermon evoluiu!")
				print(insperdéx[mon])
				XP=1
				LV=LV+1

		if command=="INSPERDÉX":
			for h in range(len(insperdéx)):
				print(insperdéx[h])
	
		if command=="TROCAR":
			for h in range(len(insperdéx)):
				print(insperdéx[h])
			print("Escolha um Inspermon de seu Insperdéx")
			y=mon
			x=input("Diga o número do Inspermon que você gostaria de utilizar em suas batalhas: ")
			mon=x
			if not (x in insperdéx):
				mon=y 
		
		else:
			for h in range(3):
				print("...")
				time.sleep(1)
			print("Lembre-se: quando você ver a opção 'O que você quer fazer?', Você poderá escolher entre:")
			print("------Passear (para achar inspermons)")
			print("------Dormir (para retornar a sua casa e pausar o jogo - você poderá salvá-lo no menu")
			print("------Insperdéx (para ver os innspermons que você encontrou e venceu)")
			print("------Trocar (para substituir o inspermon que você utilizara na próxima batalha)")


	print("Você está em  casa!\n Até a próxima!\n")
	
	if command=="DORMIR":
		pauseplay="PAUSE"
	
	if command=="DERROTA":
		pauseplay="DERROTA"
	
	return (pauseplay)

for h in range(30):
	print(" ")

print				 ("""                                                                                                           
                     `@@@   @@@@  @@@.  +@@@@@@   @@@@@@    @@@@@@@  `@@@@@@@,   @@@@; ,@@@@    @@@@@  ,   @@@, .@@@                                                                                                          
                     `@@@   @@@@. @@@.  @@@@@@@`  @@@@@@@,  @@@@@@@  `@@@@@@@@#  @@@@@ +@@@@   @@@@@@@@  , @@@@ .@@@                                                                                                          
                     `@@@   @@@@@ @@@.  @@@       @@` @@@;  @@@      `@@@  #@@#  @@@@@ @@@@@  @@@    @@@  ,@@@@,.@@@                                                                                                          
                     `@@@   @@@@@,@@@.  #@@@@@    @@``@@@,  @@@@@@@  `@@@@@@@@:  @@@:@ @+@@@  @@@    @@@` ,@@@@@.@@@                                                                                                          
                     `@@@   @@@`@@@@@.   ,@@@@@`  @@@@@@@   @@@@@@@  `@@@@@@@#   @@@`@:@,@@@  @@@    @@@` ,@@@#@'@@@                                                                                                          
                     `@@@   @@@`#@@@@.      @@@'  @@@@@@.   @@@      `@@@ @@@#   @@@ @@@`@@@  @@@    @@@  ,@@@ @@@@@                                                                                                          
                     `@@@   @@@``@@@@.` @@, @@@'  @@@`      @@@      `@@@ :@@@`  @@@ @@@ @@@  @@@    @@@  ,@@@ #@@@@                                                                                                          
                     `@@@   @@@` #@@@.  @@@@@@@`  @@@`      @@@@@@@. `@@@  @@@#  @@@ +@@ @@@   @@@@@@@@.  ,@@@  @@@@                                                                                                          
                     `@@@   @@@`  @@@.   @@@@@`   @@@`      @@@@@@@. `@@@  '@@@  @@@ :@' @@@     @@@@@`   ,@@@  '@@@                                                                                                          
                     """)                                                                                        

time.sleep(5)	 
	
for h in range(20):
	print(" ")		
print("Selecione uma forma de jogo: ")
print("Carregar (para carregar seu jogo salvo)")
print("Novo jogo (para começar um jogo novo)")
jogo=str(input("Como você gostaria de prosseguir?:  ")).upper()

if jogo=="NOVO JOGO":
	print ("Olá!")
	time.sleep(2)
	print("Bem vindo à Inspermon!")
	time.sleep(2)
	print ("Vamos começar!")
	time.sleep(2)
	print("Você vai precisar de um Insperdéx...")
	time.sleep(2)
	print("Agora, é hora de escolher o seu primeiro Inspermon para começar a sua aventura!")
	time.sleep(4)
	insp= str(input("Escolha um Inspermon: pythonxu, fegamel, deusvult: ")).upper()

	if insp=="PYTHONXU":
		insperdéx[0]=(insperdex[0])
		mon=0
	
	if insp=="FEGAMEL":
		insperdéx[1]=(insperdex[1])
		mon=1

	if insp=="DEUSVULT":
		insperdéx[2]=(insperdex[2])
		mon=2

	time.sleep(1.5)
	print("Você escolheu {}!".format(insperdex[mon][0]))
	command="nada"

if jogo=="CARREGAR":
	save1 = open('insperdéx.pkl', 'rb')
	insperdéx=pickle.load(save1)
	save1.close()
	save2 = open('XP.pkl', 'rb')
	XP= pickle.load(save2)
	save2.close()
	save3 = open('LV.pkl', 'rb')
	LV= pickle.load(save3)
	save3.close()
	print("Bem vindo de volta!")
	for h in range(len(insperdéx)):
		print(insperdéx[h])
	print("Escolha um Inspermon de seu Insperdéx")
	
	x=int (input("Diga o número do Inspermon que você gostaria de utilizar em suas batalhas: "))
	mon=x
	if not (x in insperdéx):
		insperdéx[0]=insperdex[0]
		mon=0

time.sleep(2.5)
print("Lembre-se: quando você vir a opção 'O que você quer fazer?', Você poderá escolher entre:")
print("------Passear (para achar inspermons)")
print("------Dormir (para retornar a sua casa e pausar o jogo)(leva ao 'MENU' e a opção 'SAVE')")
print("------Insperdéx (para ver os innspermons que você encontrou e venceu)")
print("------Trocar (para substituir o inspermon que você utilizara na próxima batalha)")

time.sleep(2)
for h in range(5):
	print("")

while True:         #Loop fechado em que o jogo funciona
	
	if pauseplay=="JOGAR":
		command="NADA"
		pauseplay=loopjogo(command,mon,insperdéx,insperdex,XP,LV,batalha)
	
	if pauseplay=="PAUSE":
		print ("MENU")
		pauseplay=str(input("Escreva 'jogar' para retomar o jogo ou 'salvar' para salvar sua sessão de jogo e sair: ")).upper()
		if pauseplay=="JOGAR":
			print("Resumindo o jogo...")
			time.sleep(2)
			print("")

	if pauseplay=="SALVAR":
		arquivo1 = open('insperdéx.pkl', 'wb')
		pickle.dump(insperdéx, arquivo1)
		arquivo1.close()
		arquivo2 = open('XP.pkl', 'wb')
		pickle.dump(XP, arquivo2)
		arquivo2.close()
		arquivo3 = open('LV.pkl', 'wb')
		pickle.dump(LV, arquivo3)
		arquivo3.close()
		time.sleep(1.5)	
		print ("Jogo salvo! ATÉ A PRÓXIMA!")
		break
	
	if pauseplay=="DERROTA":
		print("FIM DE JOGO")
		break
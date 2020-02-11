from datetime import date

class OggettoCacca(object):
	def __init__(self, number, mattina, pome, sera, notte, ratio, string):
		self.number = number
		self.mattina = mattina
		self.pome = pome
		self.sera = sera
		self.notte = notte
		self.ratio = ratio
		self.string = string
	def compare(item1, item2):
		if item1.number < item2.number:
			return -1
		elif item1.number > item2.number:
			return 1
		else:
			return 0			

def diff_dates():
	startDate = date(2019,12,8)
	today = date.today()
	return abs(today-startDate).days

lista = []

me = 0
meM = 0
meP = 0
meS = 0
meN = 0

elia = 0
eliaM = 0
eliaP = 0
eliaS = 0
eliaN = 0

gloria = 0
gloriaM = 0
gloriaP = 0
gloriaS = 0
gloriaN = 0

veronica = 0
veronicaM = 0
veronicaP = 0
veronicaS = 0
veronicaN = 0

boldro = 0
boldroM = 0
boldroP = 0
boldroS = 0
boldroN = 0

step = 0
stepM = 0
stepP = 0
stepS = 0
stepN = 0

giulia = 0
giuliaM = 0
giuliaP = 0
giuliaS = 0
giuliaN = 0

favero = 0
faveroM = 0
faveroP = 0
faveroS = 0
faveroN = 0

claudia = 0
claudiaM = 0
claudiaP = 0
claudiaS = 0
claudiaN = 0

benny = 0
bennyM = 0
bennyP = 0
bennyS = 0
bennyN = 0

differenza = diff_dates()

print()
print("Sono passati "+str(differenza)+" giorni dall'inizio (08/12/19)")
print()

f = open("chat.txt", "r", encoding="utf8")
for x in f:
	orario = x[10:12]
	if "Guglielmo: " in x:
		benny+=1
		if (int(orario)>=6 and int(orario)<=12):
			bennyM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			bennyP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			bennyS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			bennyN+=1
	elif "Daniele: " in x:
		me+=1
		if (int(orario)>=6 and int(orario)<=12):
			meM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			meP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			meS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			meN+=1
	elif "Mattia: " in x:
		favero+=1
		if (int(orario)>=6 and int(orario)<=12):
			faveroM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			faveroP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			faveroS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			faveroN+=1
	elif ";: " in x:
		gloria+=1
		if (int(orario)>=6 and int(orario)<=12):
			gloriaM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			gloriaP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			gloriaS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			gloriaN+=1
	elif "Nicolò B: " in x:
		boldro+=1
		if (int(orario)>=6 and int(orario)<=12):
			boldroM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			boldroP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			boldroS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			boldroN+=1
	elif "Claudia: " in x:
		claudia+=1
		if (int(orario)>=6 and int(orario)<=12):
			claudiaM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			claudiaP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			claudiaS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			claudiaN+=1
	elif "Giulia: " in x:
		giulia+=1
		if (int(orario)>=6 and int(orario)<=12):
			giuliaM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			giuliaP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			giuliaS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			giuliaN+=1
	elif "Stefano: " in x:
		step+=1
		if (int(orario)>=6 and int(orario)<=12):
			stepM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			stepP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			stepS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			stepN+=1
	elif "Veronica: " in x:
		veronica+=1
		if (int(orario)>=6 and int(orario)<=12):
			veronicaM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			veronicaP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			veronicaS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			veronicaN+=1
	elif "Elia: " in x:
		elia+=1
		if (int(orario)>=6 and int(orario)<=12):
			eliaM+=1
		elif (int(orario)>=13 and int(orario)<=18):
			eliaP+=1
		elif (int(orario)>=19 and int(orario)<=23):
			eliaS+=1
		elif (int(orario)>=0 and int(orario)<=5):
			eliaN+=1

bennyR = round((benny/differenza), 2)
boldroR = round((boldro/differenza), 2)
meR = round((me/differenza), 2)
claudiaR = round((claudia/differenza), 2)
giuliaR = round((giulia/differenza), 2)
veronicaR = round((veronica/differenza), 2)
faveroR = round((favero/differenza), 2)
eliaR = round((elia/differenza), 2)
stepR = round((step/differenza), 2)
gloriaR = round((gloria/differenza), 2)

lista.append(OggettoCacca(benny, bennyM, bennyP, bennyS, bennyN, bennyR, 'benny = '))
lista.append(OggettoCacca(me, meM, meP, meS, meN, meR, 'io = '))
lista.append(OggettoCacca(boldro, boldroM, boldroP, boldroS, boldroN, boldroR, 'boldro = '))
lista.append(OggettoCacca(claudia, claudiaM, claudiaP, claudiaS, claudiaN, claudiaR, 'claudia = '))
lista.append(OggettoCacca(giulia, giuliaM, giuliaP, giuliaS, giuliaN, giuliaR, 'giulia = '))
lista.append(OggettoCacca(veronica, veronicaM, veronicaP, veronicaS, veronicaN, veronicaR, 'veronica = '))
lista.append(OggettoCacca(favero, faveroM, faveroP, faveroS, faveroN, faveroR, 'favero = '))
lista.append(OggettoCacca(elia, eliaM, eliaP, eliaS, eliaN, eliaR, 'elia = '))
lista.append(OggettoCacca(step, stepM, stepP, stepS, stepN, stepR, 'step = '))
lista.append(OggettoCacca(gloria, gloriaM, gloriaP, gloriaS, gloriaN, gloriaR, 'gloria = '))

lista.sort(reverse = True, key=lambda x: (x.number))

for obj in lista:
    print(obj.string, obj.number)
    print('con una ratio di ', obj.ratio, ' cacche al giorno')
    print('di cui:')
    print('   ', obj.mattina, ' di mattina')
    print('   ', obj.pome, ' di pomeriggio')
    print('   ', obj.sera, ' di sera')
    print('   ', obj.notte, ' di notte')
    print(' ')
from datetime import date
import json
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


class OggettoCacca(object):
	def __init__(self, number, mattina, pome, sera, notte, ratio, string):
		self.number = number
		self.mattina = mattina
		self.pome = pome
		self.sera = sera
		self.notte = notte
		self.ratio = ratio
		self.string = string
	def compare(self, item2):
		if self.number < item2.number:
			return -1
		elif self.number > item2.number:
			return 1
		else:
			return 0			
def diff_dates():
	startDate = date(2019,12,8)
	today = date.today()
	return abs(today-startDate).days

lista = []
maxCagate = 0
differenza = diff_dates()

print()
print("Sono passati "+str(differenza)+" giorni dall'inizio (08/12/19)")
print()


merdaDizionario = dict()

f = open("chat.txt", "r", encoding="utf8")
for x in f:
	orario = x[10:12]
	messaggio = x[18:]
	if(":" in messaggio):
		mittente = messaggio[0:messaggio.index(':')]
		if mittente in merdaDizionario:
			if (int(orario)>=6 and int(orario)<=12):
				merdaDizionario[mittente]['cagate']['mattino'] = merdaDizionario[mittente]['cagate']['mattino'] + 1
			elif (int(orario)>=13 and int(orario)<=18):
				merdaDizionario[mittente]['cagate']['pomeriggio'] = merdaDizionario[mittente]['cagate']['pomeriggio'] + 1
			elif (int(orario)>=19 and int(orario)<=23):
				merdaDizionario[mittente]['cagate']['sera'] = merdaDizionario[mittente]['cagate']['sera'] + 1
			elif (int(orario)>=0 and int(orario)<=5):
				merdaDizionario[mittente]['cagate']['notte'] = merdaDizionario[mittente]['cagate']['notte'] + 1
		else:
			#creo la voce
			cagateElement = {}
			if (int(orario)>=6 and int(orario)<=12):
				cagateElement = {
					'mattino': 1,
					'pomeriggio': 0,
					'sera': 0,
					'notte':0,
				}
			elif (int(orario)>=13 and int(orario)<=18):
				cagateElement = {
					'mattino': 0,
					'pomeriggio': 1,
					'sera': 0,
					'notte':0,
				}
			elif (int(orario)>=19 and int(orario)<=23):
				cagateElement = {
					'mattino': 0,
					'pomeriggio': 0,
					'sera': 1,
					'notte':0,
				}
			elif (int(orario)>=0 and int(orario)<=5):
				cagateElement = {
					'mattino': 0,
					'pomeriggio': 0,
					'sera': 0,
					'notte':1,
				}

			dictionaryElement = {
				'cagate': cagateElement,
				'media':0,
				'totale':0,
			}
			merdaDizionario[mittente] = dictionaryElement
#calcolo le varie medie 
for cagatore in merdaDizionario:
	totaleCagate = merdaDizionario[cagatore]['cagate']['mattino'] + merdaDizionario[cagatore]['cagate']['pomeriggio'] + merdaDizionario[cagatore]['cagate']['sera'] + merdaDizionario[cagatore]['cagate']['notte']
	merdaDizionario[cagatore]['totale'] = totaleCagate
	merdaDizionario[cagatore]['media']= round((totaleCagate/differenza),2)
	lista.append(OggettoCacca(merdaDizionario[cagatore]['totale'],
		merdaDizionario[cagatore]['cagate']['mattino'],merdaDizionario[cagatore]['cagate']['pomeriggio'],merdaDizionario[cagatore]['cagate']['sera'], 
		merdaDizionario[cagatore]['cagate']['notte'], merdaDizionario[cagatore]['media'],cagatore +' = '))
	if totaleCagate > maxCagate:
		maxCagate = totaleCagate
lista.sort(reverse = True, key=lambda x: (x.number))  

results = open("results"+str(date.today())+".csv", "w")
outputString = ""
outputCsv = "Nome, Totale, Ratio, Mattina, Pomeriggio, Sera, Notte\n"

for obj in lista:
    outputString += obj.string + str(obj.number) +"\n"
    outputString += 'con una ratio di '+ str(obj.ratio)+ ' cacche al giorno'+"\n"
    outputString += 'di cui:'+"\n"
    outputString += '   '+ str(obj.mattina)+ ' di mattina'+"\n"
    outputString += '   '+ str(obj.pome)+ ' di pomeriggio'+"\n"
    outputString += '   '+ str(obj.sera)+ ' di sera'+"\n"
    outputString += '   '+ str(obj.notte)+ ' di notte'+"\n\n"

    outputCsv += obj.string.split(' ', 1)[0] + "," + str(obj.number)  + "," + str(obj.ratio) + "," + str(obj.mattina) + "," + str(obj.pome) + "," + str(obj.sera) + "," + str(obj.notte) + "\n"

print(outputString)
results.write(outputCsv)
results.close()

with open ('output.json', 'w', encoding='utf8') as output:
	json.dump(merdaDizionario, output, ensure_ascii=False)


N = 0
mattinoBar = []
pomeriggioBar = []
seraBar = []
notteBar = []
names = []
for cagatore in merdaDizionario:
	N = N + 1
	mattinoBar.append(int(merdaDizionario[cagatore]['cagate']['mattino']))
	pomeriggioBar.append(int(merdaDizionario[cagatore]['cagate']['pomeriggio']))
	seraBar.append(int(merdaDizionario[cagatore]['cagate']['sera']))
	notteBar.append(int(merdaDizionario[cagatore]['cagate']['notte']))
	names.append(cagatore)

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence




p1 = plt.bar(ind, mattinoBar, width)
p2 = plt.bar(ind, pomeriggioBar, width, bottom=mattinoBar)
p3 = plt.bar(ind, seraBar, width, bottom=np.array(pomeriggioBar)+np.array(mattinoBar))
p4 = plt.bar(ind, notteBar, width, bottom=np.array(pomeriggioBar)+np.array(mattinoBar)+np.array(seraBar))

plt.ylabel('Cagate')
plt.title('Che cagate')
plt.xticks(ind, names)
plt.yticks(np.arange(0, maxCagate, 50))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Mattino', 'Pomeriggio', 'Sera', 'Notte'))
plt.show()

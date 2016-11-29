# -*- coding: utf-8 -*-

#########################################
### Titel: 			 Buhnenrennen   ####
### VersionsNr:			  V3.33	   	###
### Autor:			Johannes Sonn   ##
#####################################



###Import
import sys

###Variablendeklaration
inputfile = ""
input = ""
outputfile = ""
outputfilename = ""
startMax = 0 #Startposition vom Max
startMinnie = 0 #Startposition von Minnie
vMax = 25.0/3.0 #m/s
vMinnie = 50.0/9.0 #m/s
i = 1 #i = Buhnenzahl
j = 1 #wird für die Berechnung von tMax benötigt
k = 1 #wird für die Berechnung von tMax benötigt
y1 = 0 #wird für die Berechnung von tMinnie benötigt
y2 = 0 #wird für die Berechnung von tMinnie benötigt
tMax = 0 #Zeit die Max benötigt um von der Startposition zu einem bestimmten Loch zu gelangen
tMinnie = 0 ##Zeit die Max benötigt um von der Startposition zu einem bestimmten Loch zu gelangen
tLoesungMinnie = 0
tLoesungMax = 0
tMaxGes = 0
tMinnieGes = 0
maxPos = 0
loesungen = []
loesungList = []
tLoesungList = []
xLoecher = []
tXLoecher = []
minnieGefangen = False
USAGE = "Buhnenrennen [input-Datei]"

#Wenn das Programm nicht mit 2 Argumenten (der Programmname wird mitgezählt) aufgerufen wurde,...
if len(sys.argv) != 2:
	#...wird ausgegeben wie man das Programm richtig aufruft
	print USAGE

#Wenn es mit 2 Argumente aufgerufen wurde, wird die angegebene Datei als "file" geöffnet
#und als Liste in "input" eingelesen
else:
	file = open(sys.argv[1])
	input = file.readlines()

	#Es werden die Zeilenumbrüche der Input-Datei in "input" gelöscht
	for koor in input:
		input[input.index(koor)] = koor[0:-1]
	

	#Y-Koordinaten der Startloecher werden in "startMax" und "startMinnie" eingelesen
	startMax = float(input[0][4:])
	startMinnie = float(input[1][4:])


	
	
	
	#Für alle Einträge (Koordinaten der Löcher) bzw. "koor" in "input", wird folgendes ausgeführt:
	for koor in input:
	
		
		#Wenn Minnie noch nicht gefangen wurde
		if minnieGefangen == False:
			
			#Wenn '70' mal "i" in "koor" vorkommt (bzw. '70' mal "i" nicht nicht in "koor" gefunden wurde)
			if koor.find(" " + str(70 * i) + " ") != -1:
			
				#Der y-Wert aus "koor" wird in "y2" geschrieben
				y2 = float(koor[3+len(str(70 * i)):])
				
				#Wenn in "koor" 70 vorkommt, also bei der ersten Buhne
				if koor.find(" 70 ") == 1:
					
					#Die Zeiten, die Minnie und Max von dem letzten Loch zum Loch mit den Koordinaten "koor" werden berechnet
					#Die Strecke wird durch den Satz des Pythagoras berechnet und durch die Geschwindigkeit der beiden Hunde (in m/s) berechnet
					tMinnie = ((70**2 + (startMinnie - y2)**2)**0.5)/vMinnie
					tMax = ((70**2 + (startMax - y2)**2)**0.5)/vMax
				
					#Wenn Minnie schneller als Max zum nächsten Loch kommt (also tMinnie kleiner al tMax ist),
					#werden die Zeit und die y-Koordinaten des Lochs zu "loesungList" und in "tLoesungList" hinzugefügt
					if tMinnie < tMax:
						loesungList.append(y2)
						tLoesungList.append(((70**2 + (startMinnie - y2)**2)**0.5)/vMinnie)

						
			
				
				#Bei jedem weiteren Loch, außer bei jedem ersten Loch in einer neuen Buhne und bei der ersten Buhne
				elif koor.find(" 0 ") == -1:
					
					#Der letzte Eintrag aus "loesungen" (also Minnies letzte Position) wird in y1 eingefügt
					y1 = loesungen[-1]
					
					#Die y-Koordinate aus "koor" wird in y2 eingefügt
					y2 = float(koor[3+len(str(70 * i)):])
					
					#Die Summe aus der Zeit, die Minnie von der aktuellen Position zu "koor" benötigt und "tMinnieGes" (die Summe der vorigen berechneten Zeiten) wird in "tMinnie" gespeichert
					tMinnie = ((70**2 + (y1 - y2)**2)**0.5)/vMinnie + tMinnieGes
					
					
					###MAX Zeit rückwärts berechnen
					
					#In "j" wird der Index von "koor" in "input" um 1 verringert gespeichert
					j = input.index(koor) - 1
					
					#In "k" wird "i" um 1 verringert gespeichert
					k = i - 1
					
					#tMax wird auf 0 gesetzt
					tMax = 0
					
					#Der Wert aus "y2" wird in "maxPos" gespeichert
					maxPos = y2
					
					#Solange "k" größer als 0 ist, wird folgendes ausgeführt
					while k > 0:
						
						#Wenn der Eintrag aus "input" mit dem Index "j" mit ("x " + str( k * 70 ) + " ") beginnt (also der Eintrag ein großes Loch mit der x-Position (k*70) beschreibt),
						#soll folgendes ausgeführt werden:
						if (input[j]).startswith("x " + str( k * 70 ) + " "):

							#Zur Liste "xLoecher" soll aus diesem Eintrag aus "input" mit Index "j" der y-Wert des Max-Lochs hinzugefügt
							xLoecher.append( float( input[ j ] [ ( (input[j]).index(" ", 2) +1 ) :]))
							
							#Außerdem soll die benötigte Zeit, die Max benötigt um von der letzten Position (maxPos)
							#zu diesem Loch zu gelangen zu "txLoecher" hinzugefügt werden
							tXLoecher.append(((70**2 + ( (xLoecher[-1]) - maxPos)**2)**0.5)/vMax)
							
						#Wenn in dem Eintrag aus "input" mit dem Index "j"  ("x " + str( k * 70 ) + " ") NICHT gefunden werden kann (also der Eintrag ein Loch beschreibt, welches sich nicht in der Buhne, mit der x-Koordinate (k+70) befindet)
						# UND in dem (" "+str( i * 70 )+" ") NICHT gefunden wird (also der Eintrag ein Loch beschreibt, welches NICHT in der selben Buhne vorkommt wie "koor"),
						#soll folgendes ausgeführt werden
						elif (input[j]).find(" "+str( k * 70 )+" ") == -1 and (input[j]).find(" "+str( i * 70 )+" ") == -1:
							
							#Wenn "tXLoecher" nicht leer ist, soll folgendes ausgeführt werden.
							if tXLoecher:
								
								#"tMax" soll um das Minimum aus "tXLoecher" erhöht werden
								tMax += min(tXLoecher)
								
								#"maxPos" soll auf die Position des Lochs gesetzt werden, welches am nächsten zur vorherigen Position ist (also den Wert aus "xLoecher" mit dem Index des Minimums aus tXLoecher)
								maxPos = xLoecher[tXLoecher.index(min(tXLoecher))]
							
							#"xLoecher" und "tXLoecher" werden geleert
							xLoecher = []
							tXLoecher = []
							
							#"k" wird um 1 verringert
							k -= 1
							
							
							#Wenn "k" gleich 0 ist, dann soll folgendes ausgeführt werden:
							if k == 0:
							
								#"tMax" wird um die Zeit erhöht, die Max benötigt um von seiner Startposition (startMax) zur ersten Buhne bzw. "maxPos" zu rennen
								tMax += ((70**2 + ( startMax - maxPos)**2)**0.5)/vMax
							
						#"j" wird um 1 verringert
						j -= 1	
	
	
					
						#Wenn Minnie schneller als Max zum nächsten Loch kommt (also tMinnie kleiner al tMax ist),
						#werden die Zeit und die y-Koordinaten des Lochs zu "loesungList" und in "tLoesungList" hinzugefügt
						if tMinnie < tMax:
							loesungList.append(y2)
							tLoesungList.append(((70**2 + (y1 - y2)**2)**0.5)/vMinnie)
						
			
			
			#Bei jedem ersten Loch in jeder Buhne, außer in der nullten (also " 0 " nicht in "koor" gfunden wird) und der ersten Buhne, soll folgendes ausgeführt werden:
			elif koor.find(" 0 ") == -1:

				#Wenn die "loesungList" leer ist, also Minnie gefangen wurde und es bei einer Buhne kein Loch gab zu dem Minnie schneller rennen konnte,
				#wird "minnieGefangen" auf 'True' gesetzt
				if loesungList == []:
					minnieGefangen = True

				#Wenn Minnie nicht gefangen wurde, soll folgendes ausgeführt werden:
				else:
					#Es wird der Liste "loesungen" die y-Koordinate des letzten Lochs hinzugefügt
					loesungen.append(loesungList[tLoesungList.index(min(tLoesungList))])
					
					#"loesungList" wird geleert
					loesungList = []
					
					#Zu tMinnieGes wird das Minimum aus "tLoesungList" addiert
					tMinnieGes +=  min(tLoesungList)
					
					#"tLoesungList", "xLoecher" und "tXLoecher" werden geleert
					tLoesungList = []
					xLoecher = []
					tXLoecher = []

					#"i" wird um 1 erhöht
					i += 1
					
					#Der letzte Eintrag aus "loesungen" (also Minnies letzte Position) wird in y1 eingefügt
					y1 = loesungen[-1]
					
					#Die y-Koordinate aus "koor" wird in y2 eingefügt
					y2 = float(koor[3+len(str(70 * i)):])
					
					#Die Summe aus der Zeit, die Minnie von der aktuellen Position zu "koor" benötigt und "tMinnieGes" (die Summe der vorigen berechneten Zeiten) wird in "tMinnie" gespeichert
					tMinnie = ((70**2 + (y1 - y2)**2)**0.5)/vMinnie + tMinnieGes

					
					#MAX Zeit rückwärts berechnen
					
					#In "j" wird der Index von "koor" in "input" um 1 verringert gespeichert
					j = input.index(koor) - 1
					
					#In "k" wird "i" um 1 verringert gespeichert
					k = i - 1
					
					#tMax wird auf 0 gesetzt
					tMax = 0
					
					
					
					#Der Wert aus "y2" wird in "maxPos" gespeichert
					maxPos = y2
					
					#Solange "k" größer als 0 ist, wird folgendes ausgeführt
					while k > 0:
						
						#Wenn der Eintrag aus "input" mit dem Index "j" mit ("x " + str( k * 70 ) + " ") beginnt (also der Eintrag ein großes Loch mit der x-Position (k*70) beschreibt),
						#soll folgendes ausgeführt werden:
						if (input[j]).startswith("x "+str( k * 70 )+" "):

							#zur Liste xLoecher wird aus input aus dem "index(koor) -j" der y-Wert des Max-Lochs hinzugefügt
							xLoecher.append( float( input[ j ] [ ( (input[j]).index(" ", 2) +1 ) :])) 
							#Außerdem soll die benötigte Zeit, die Max benötigt um von der letzten Position (maxPos)
							#zu diesem Loch zu gelangen zu "txLoecher" hinzugefügt werden
							tXLoecher.append(((70**2 + ( (xLoecher[-1]) - maxPos)**2)**0.5)/vMax)
			
						#Wenn in dem Eintrag aus "input" mit dem Index "j"  ("x " + str( k * 70 ) + " ") NICHT gefunden werden kann (also der Eintrag ein Loch beschreibt, welches sich nicht in der Buhne, mit der x-Koordinate (k+70) befindet)
						# UND in dem (" "+str( i * 70 )+" ") NICHT gefunden wird (also der Eintrag ein Loch beschreibt, welches NICHT in der selben Buhne vorkommt wie "koor"),
						#soll folgendes ausgeführt werden
						elif (input[j]).find(" "+str( k * 70 )+" ") == -1 and (input[j]).find(" "+str( i * 70 )+" ") == -1:

							#Wenn "tXLoecher" nicht leer ist, soll folgendes ausgeführt werden.
							if tXLoecher:
								
								#"tMax" soll um das Minimum aus "tXLoecher" erhöht werden
								tMax += min(tXLoecher)
								
								#"maxPos" soll auf die Position des Lochs gesetzt werden, welches am nächsten zur vorherigen Position ist (also den Wert aus "xLoecher" mit dem Index des Minimums aus tXLoecher)
								maxPos = xLoecher[tXLoecher.index(min(tXLoecher))]
							
							#"xLoecher" und "tXLoecher" werden geleert
							xLoecher = []
							tXLoecher = []
							
							#"k" wird um 1 verringert
							k -= 1
							
														
							#Wenn "k" gleich 0 ist, dann soll folgendes ausgeführt werden:
							if k == 0:
							
								#"tMax" wird um die Zeit erhöht, die Max benötigt um von seiner Startposition (startMax) zur ersten Buhne bzw. "maxPos" zu rennen
								tMax += ((70**2 + ( startMax - maxPos)**2)**0.5)/vMax
								
						#"j" wird um 1 verringert	
						j -= 1	
						
					
						#Wenn Minnie schneller als Max zum nächsten Loch kommt (also tMinnie kleiner al tMax ist),
						#werden die Zeit und die y-Koordinaten des Lochs zu "loesungList" und in "tLoesungList" hinzugefügt
						if tMinnie < tMax:
							loesungList.append(y2)
							tLoesungList.append(((70**2 + (y1 - y2)**2)**0.5)/vMinnie)
						
	
	#Wenn Minnie nicht gefangen wurde, also "minnieGefangen" gleich "False" ist, soll folgendes ausgeführt werden:
	if minnieGefangen == False:
		
		#Zur Liste "loesungen" soll das Minimum aus der "loesungList" hinzugefügt werden
		loesungen.append(loesungList[tLoesungList.index(min(tLoesungList))])
		
		#Zur List "loesungen" soll an nullter Stelle die y-Koordinate Minnies Startposition (startMinnie) hinzugefügt werden
		loesungen.insert(0, startMinnie)

		#Es soll "Loesung;" ausgegeben werden
		print ("")
		print ("Loesung:")
		print ("")
		
		#Es werden Ort und Name der Output-Datei festgelegt und diese Datei geöffnet
		outputfilename = sys.argv[1][0:-4] + "_Loesung.txt"
		outputfile = open(outputfilename, "w")
		
		
		#Zu allen y-Koordinaten in der Liste "loesungen", soll vor der y-Koordinate die entsprechende x-Koordinate #(Vielfaches von 70) eingefügt werden.
		for loesungKoor in loesungen:
			loesungKoor= str(70 * i ) + ", " + str(loesungKoor)
			i += 1
			
			#Danach soll dieser Tupel (die x- und y-Koordinaten der Löcher durch die Minnie sicher vor Max entkommen kann) ausgegeben werden
			print loesungKoor
			
			#Es soll "loesungKoor" und ein Zeilenumbruch in die Output-Datei geschrieben werden
			outputfile.write(loesungKoor + "\n")

		#Die Output-Datei wird geschlossen
		outputfile.close()
		
	

	
	#Wenn Minnie bei einer Buhne bei keinem Loch schneller war und somit gefangen wurde, soll ausgegeben werden "Minnie wird gefangen!"
	else:
		print ("Minnie wird gefangen!")
		
###Programmende###
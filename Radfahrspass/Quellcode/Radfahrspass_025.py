# -*- coding: utf-8 -*-

#############################
### Titel: Radfahrspass	####
### VersionsNr: 25		###
### Autor: Johannes Sonn##
#########################

#Import
import sys
import os


#Variablen werden deklariert
diffSteigGef = 0
erg = 0
anzGeraden = 0
anzSteigungen = 0
anzGefaelle = 0
parcours = ""
inputFile = ""
outputFile = ""
filename = ""
outputFilename = ""
filesize = 0
inputPaket = ""
paketSize = 1024
anzInputPakete = 0
rest = 0
i = 0
firstChar = ""
anzPlus = 0
anzMinus = 0
USAGE = "USAGE: Radfahrspass [input-file]"


#Falls der Speicherort des "input-files" nicht angegeben ist,
#wird ausgegeben wie man dieses Programm richtig aufruft (USAGE)
if len(sys.argv) != 2:
	print USAGE
	
#Falls das Programm mit zwei Argumenten aufgerufen wurde...
if len(sys.argv) == 2:
	
	#...wird das Argument, also der Dateipfad in "filename" geschrieben,...
	filename = str(sys.argv[1])
	
	#...die Dateigröße in Byte in "filesize" geschrieben,...
	filesize = os.path.getsize(filename)
	
	#...die Anzahl der Input-Pakete berechnet und in "anzInputPakete" geschrieben und ...
	anzInputPakete = filesize/paketSize
	
	#...die restlichen Byte, des Input-Files berechnet und in "rest" geschrieben
	rest = filesize%paketSize
	
	#Bei Dateien die kleiner als die bestimmte Paketgröße sind, also "anzInputPakete" gleich 0 ...
	if anzInputPakete == 0: #-- kleine Dateien --
		
		#...wird die Datei als "inputFile" geöffnet...
		inputFile = open(filename)
		
		#...und komplett eingelesen
		inputPaket = inputFile.read()
		
		
		
		
		
		#Danach wird die Anzahl von jeweils Steigungen, Gefällen und Geraden gezählt
		#und in die entsprechende Variable gespeichert
		anzSteigungen = inputPaket.count("/")
		anzGefaelle = inputPaket.count("\\")
		anzGeraden = inputPaket.count("_")
	
	#Bei Dateien die größer als die bestimmte Paketgröße sind, also "anzInputPakete" größer 0 ...
	else:
		
		#...wird die Datei als "inputFile" geöffnet
		inputFile = open(filename)
		
		#Für alle Input-Pakete, also solange "i" kleiner als "anzInputPakete" ist wird...
		while i < anzInputPakete:
			
			#..."i" um 1 erhöht...
			i += 1
			
			#...das erste Input-Paket in inputPaket eingelesen...
			inputPaket = inputFile.read(paketSize)
			
			#... und die Anzahl von jeweils Steigungen, Gefällen und Geraden gezählt
			#und in zu der entsprechenden Variable dazu addiert
			anzSteigungen += inputPaket.count("/")
			anzGefaelle += inputPaket.count("\\")
			anzGeraden += inputPaket.count("_")
			
			#Falls restliche Zeichen exestieren, also "rest" größer 0 ist...
			if rest > 0:
			
				#...wird der Rest komplett in "inputPaket" eingelesen...
				inputPaket = inputFile.read(rest)
				
				#...und anschließend die Anzahl von jeweils Steigungen, Gefällen und Geraden gezählt
				#und in zu der entsprechenden Variable dazu addiert
				anzSteigungen += inputPaket.count("/")
				anzGefaelle += inputPaket.count("\\")
				anzGeraden += inputPaket.count("_")

	#Nachdem wird die Datei geschlossen
	inputFile.close()

	#Es wird die Differenz zwischen der Anzahl der Steigungen (anzSteigungen) und der Anzahl der Gefaelle (anzGefaelle) berechnet
	diffSteigGef = anzGefaelle - anzSteigungen

	#Es wird die Datei nochmal geöffnet, ...
	inputFile = open(filename)
	
	#...das erste Zeichen in "firstChar" gespeichert, ...
	firstChar = inputFile.read(1)
	
	#...die ParcoursDatei geschlossen
	inputFile.close()
	
	#Es wird in "outputFilename" der "filename" mit "_Loesung.txt" als Ergänzung geschrieben
	outputFilename = (str(filename[0:-4]) + "_Loesung.txt")
	
#Es überprüft ob der "firstChar" ein Backslash ist, also der Parcours mit einem Gefälle beginnt
if (firstChar != "\\"):
	print "ERROR"
	print "ungueltiger parcours"
	
	
	
#Wenn der Parcours mit einem Gefälle beginnt und diffSteigGef positiv ist,...
elif diffSteigGef > 0:
	
	#...wird die Differenz zwischen "diffSteigGef" und "anzGeraden" in "erg" gespeichert, wobei "anzGeraden" der Subtrahend ist
	erg = diffSteigGef - anzGeraden

	#falls "erg" gleich 0 ist
	#und somit die 'überschüssige' Geschwindigkeit komplett ausgebremst werden kann,
	#soll auf jeder Geraden gebremst werden (-)
	#Dies wird in die Output-Datei geschrieben und es wird ausgegeben wo sich diese befindet
	if erg == 0:
		print "Ja, der Parcours ist regelkonform befahrbar"
		anzMinus = anzGeraden
		outputFile = open(outputFilename, "w")
		outputFile.write(anzGeraden * "-")
		outputFile.close()
		print "Es soll", anzMinus, "mal gebremst werden"
		
		#Es wird ausgegeben wo die Loesung gespeichert wurde
		print 'Die Loesung wurde unter "', outputFilename, '" gespeichert'
			
	#falls "erg" grösser 0 ist
	#und somit die 'überschüssige' Geschwindigkeit nicht ausgebremst werden kann,
	#ist der Parcours nicht regelkonform befahrbar (ERROR #1)
	elif erg > 0:
		print "Nein, der Parcours ist nicht regelkonform befahrbar"
			
	#falls "erg" kleiner 0 ist
	#und somit die 'überschüssige' Geschwindigkeit, durch die Geraden ausgebremst werden kann
	#und noch Geraden 'übrig' sind,
	#soll auf den letzten Geraden gebremst werden,
	#damit die 'überschüssige' Geschwindigkeit ausgebremst werden kann 
	#und auf den restlichen Geraden soll auf der ersten Haelfte beschleunigt und auf der zweiten gebremst werden.
	#Dies wird in die Output-Datei geschrieben und es wird ausgegeben wo sich diese befindet
	#
	#Es wird erst beschleunigt und anschliessend gebremst um zu verhindern,
	#dass man waehrend der Fahrt auf oder sogar unter eine Geschwindigkeit von 0 m/s gelangt
	
	elif erg < 0:
		if erg%2 == 0:  #Dies ist aber nur möglich wenn die Anzahl der 'überschüssigen' Geraden gerade ist 
			print "Ja, der Parcours ist regelkonform befahrbar"
			anzPlus = (-1*erg) / 2
			anzMinus = anzGeraden - ((-1*erg) / 2)
			outputFile = open(outputFilename, "w")
			outputFile.write(anzPlus * "+" + anzMinus * "-")
			outputFile.close()
			print "Es soll", anzPlus, "mal beschleunigt und", anzMinus, "mal gebremst werden"
			
			#Es wird ausgegeben wo die Loesung gespeichert wurde
			print 'Die Loesung wurde unter "', outputFilename, '" gespeichert'
			
		
		
#Wenn diffSteigGef negativ ist,...
elif diffSteigGef < 0:

	#...wird die Summe von "diffSteigGef" und "anzGeraden" in "erg" gespeichert
	erg = diffSteigGef + anzGeraden

	
	
	
	
	
	
	#falls "erg" gleich 0 ist
	#und somit die 'benötigte' Geschwindigkeit, um mit 0 m/s im Ziel anzukommen komplett 'hergestellt' werden kann,
	#soll auf jeder Geraden beschleunigt werden (+)
	#Dies wird in die Output-Datei geschrieben und es wird ausgegeben wo sich diese befindet
	if erg == 0:
		print "Ja, der Parcours ist regelkonform befahrbar"
		anzPlus = anzGeraden
		outputFile = open(outputFilename, "w")
		outputFile.write(anzGeraden*"+")
		outputFile.close()
		print "Es soll", anzPlus, "mal beschleunigt werden"
		
		#Es wird ausgegeben wo die Loesung gespeichert wurde
		print 'Die Loesung wurde unter "', outputFilename, '" gespeichert'
	
	#falls "erg" grösser 0 ist
	#und somit die 'benötigte' Geschwindigkeit, durch die Geraden 'hergestellt' werden kann
	#und noch Geraden 'übrig' sind,
	#soll auf den ersten Geraden beschleunigt werden,
	#damit die 'benötigte' Geschwindigkeit 'hergestellt' werden kann 
	#und auf den restlichen Geraden soll auf der ersten Haelfte beschleunigt und auf der zweiten gebremst werden.
	#Dies wird in die Output-Datei geschrieben und es wird ausgegeben wo sich diese befindet
	#
	#Es wird erst beschleunigt und anschliessend gebremst um zu verhindern,
	#dass man waehrend der Fahrt auf oder sogar unter eine Geschwindigkeit von 0 m/s gelangt
	elif erg > 0:
		if erg%2 == 0:
			anzPlus = anzGeraden - (erg) / 2
			anzMinus = erg / 2
			outputFile = open(outputFilename, "w")
			outputFile.write(anzPlus * "+" + anzMinus * "-")
			outputFile.close()
			print "Ja, der Parcours ist regelkonform befahrbar"
			print "Es soll", anzPlus, "mal beschleunigt und", anzMinus, "mal gebremst werden"
			
			#Es wird ausgegeben wo die Loesung gespeichert wurde
			print 'Die Loesung wurde unter "', outputFilename, '" gespeichert'

	#falls "erg" kleiner 0 ist
	#und somit die 'benötigte' Geschwindigkeit nicht hergestellt'' werden kann,
	#ist der Parcours nicht regelkonform befahrbar
	elif erg < 0:
		print "Nein, der Parcours ist nicht regelkonform befahrbar"
		
		

#Wenn diffSteigGef neutral (0) ist...
elif diffSteigGef == 0:
	if anzGeraden%2 == 0:  #...und "anzGeraden" gerade ist,...
		print "Ja, der Parcours ist regelkonform befahrbar"
		anzPlus = anzMinus = anzGeraden/2
		#...soll auf der ersten Haelfte beschleunigt und auf der zweiten gebremst werden
		#Dies wird in die Output-Datei geschrieben und es wird ausgegeben wo sich diese befindet
		outputFile = open(outputFilename, "w")
		outputFile.write((anzGeraden/2)*"+" + (anzGeraden/2)*"-")
		outputFile.close()
		print "Es soll", anzPlus, "mal beschleunigt und", anzMinus, "mal gebremst werden"
		#
		#Es wird erst beschleunigt und anschliessend gebremst um zu verhindern,
		#dass man waehrend der Fahrt auf oder sogar unter eine Geschwindigkeit von 0 m/s gelangt
		
		
		
		
		
		
		#Es wird ausgegeben wo die Loesung gespeichert wurde
		print 'Die Loesung wurde unter "', outputFilename, '" gespeichert'
		
	#Sonst ist der Parcours nicht regelkonform befahrbar
	else:
		print "Nein, der Parcours ist nicht regelkonform befahrbar"
		

#Sonst liegt ein Fehler vor
else:
	print "ERROR"

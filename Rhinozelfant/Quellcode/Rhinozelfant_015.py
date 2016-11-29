# -*- coding: utf-8 -*-

###Titel:	 	Rhinozelefant
###VersionsNr:	15
###Autor: 		Johannes Sonn
###Datum: 		15.01.2016

###Import###
from PIL import Image
import time
import sys


###Variablen deklarieren###
i = 0
falscheEingabe = True
usage = 'USAGE: Rhinozelefant_xxx.py -i [input-file] -o [output-file]'
inputIm = 0
outputIm = 0
x = 0
y = 0


###Es wird die Anzahl der Argumente überprüft
if len(sys.argv) == 5:

	#Falls das erste Argument gleich "-i" ist,...
	if sys.argv[1] == "-i" or sys.argv[1] == "-I":
	
		###Ausgabe: "Importiere Photo"
		print "Importiere Photo"
	
		#...dann wird das angegeben Bild als "inputIm" geoeffnet und als "inputPix" geladen...
		inputIm = Image.open(sys.argv[2])
		inputPix = inputIm.load()
		
		#...und es wird eine Kopie mit dem Namen "outputIm" angefertigt und als "outputPix" geladen.
		outputIm = inputIm.copy()
		outputPix = outputIm.load()
		
		
		###Ausgabe: "Analysiere Photo"
		print "Analysiere Photo"
		
		#Solange der y-Wert kleiner als die Bildgröße ist...
		while y < inputIm.size[1]:
			#...und der x-Wert kleiner als die Bildgröße ist...
			while x < inputIm.size[0]:
							
				#...und solange er nicht am Rand ist, ...
				if x < inputIm.size[0] - 1:
					
					#...werden die RGB-Werte des Pixels[x, y] mit dem Nachbar-Pixel[x+2, y] verglichen
					if inputPix[x, y] == inputPix[x + 1, y]:
						
						#Wenn die RGB-Werte identisch sind, werden in der Output-Kopie die entsprechenden Pixel weiß (255, 255, 255) gefärbt
						outputPix[x, y] = (255, 255, 255)
						outputPix[x + 1, y] = (255, 255, 255)
				
				#Wenn der Pixel nicht am Rand ist, ...	
				if y < inputIm.size[1] - 1:
					
					
					
					
					
					
					#Wenn die RGB-Werte identisch sind, werden in der Output-Kopie die entsprechenden Pixel weiß (255, 255, 255) gefärbt
					#...werden die RGB-Werte des Pixels[x, y] mit dem Nachbar-Pixel[x+2, y] verglichen
					if inputPix[x, y] == inputPix[x, y + 1]:
					
					#Wenn die RGB-Werte identisch sind, werden in der Output-Kopie die entsprechenden Pixel weiß (255, 255, 255) gefärbt
						outputPix[x, y] = (255, 255, 255)
						outputPix[x, y+1] = (255, 255, 255)
						
				#Nach jedem Pixel wird der x-Wert um 1 erhöht
				x  += 1
			
			#Nach einer Pixel-Reihe wird der y-Wert um 1 erhöht und der x-Wert auf 0 gesetzt
			y += 1
			x = 0 	

			
		#Wenn das dritte Argument gleich "-o" ist,...
		if sys.argv[3] == "-o" or sys.argv[3] == "-O":
		
			#...wird ausgegeben, in welchem Pfad und unter welchem Namen die Output-Kopie gespeichert wird...
			print 'Speichere bearbeitetes Photo unter "' + sys.argv[4] + '"'
			
			#...und unter dem angegeben Pfad und Namen gespeichert
			outputIm.save(sys.argv[4])

				
			#Ausgabe 'Fertig!'
			print "--------"
			print 'Fertig!'

		

	#Wenn das Programm mit dem Argument "-h" oder "--help" aufgerufen oder falsch aufgerufen wird,
	#wird ausgegeben wie man es richtig aufruft
	else:
		print usage
else:
		if sys.argv[-1] == "-h" or sys.argv[-1] == "-H" or sys.argv[-1] == "--help":
			print usage
		else:
			print usage
	

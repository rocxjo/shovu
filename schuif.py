bestandsnaam = raw_input("Bestandsnaam: ")
verschuiving = float(raw_input("Hoeveel seconden +/- opschuiven? "))

bestand = open(bestandsnaam, "r")
nieuwbestand = []
i=0
for regel in bestand :
	nieuweregel = regel
	if len(regel)>5 :
		if regel[2]==":" and regel[5]==":" :
			uur1=int(regel[0:2])
			minuut1=int(regel[3:5])
			seconde1=float(regel[6:8]+"."+regel[9:12])
			seconde1 = seconde1 + verschuiving
			if seconde1<0 :
				seconde1=seconde1+60
				minuut1=minuut1-1
			if seconde1>=60 :
				seconde1=seconde1-60
				minuut1=minuut1+1
			if minuut1<0 :
				minuut1=minuut1+60
				uur1=uur1-1
			if minuut1>=60 :
				minuut1=minuut1-60
				uur1=uur1+1
			uur1=str(round(uur1,0))[:-2]
			if len(uur1)==1 :
				uur1 = "0"+uur1
			minuut1=str(round(minuut1,0))[:-2]
			if len(minuut1)==1 :
				minuut1 = "0"+minuut1
			seconde1=str(round(seconde1,3))
			if seconde1[1]=="." :
				seconde1 = "0"+seconde1
			seconde1 = seconde1+(6-len(seconde1))*"0"
			
			uur2=int(regel[17:19])
			minuut2=int(regel[20:22])
			seconde2=float(regel[23:25]+"."+regel[26:29])
			seconde2 = seconde2 + verschuiving
			if seconde2<0 :
				seconde2=seconde2+60
				minuut2=minuut2-1
			if seconde2>=60 :
				seconde2=seconde2-60
				minuut2=minuut2+1
			if minuut2<0 :
				minuut2=minuut2+60
				uur2=uur2-1
			if minuut2>=60 :
				minuut2=minuut2-60
				uur2=uur2+1
			uur2=str(round(uur2,0))[:-2]
			if len(uur2)==1 :
				uur2 = "0"+uur2
			minuut2=str(round(minuut2,0))[:-2]
			if len(minuut2)==1 :
				minuut2 = "0"+minuut2
			seconde2=str(round(seconde2,3))
			if seconde2[1]=="." :
				seconde2 = "0"+seconde2
			seconde2 = seconde2+(6-len(seconde2))*"0"
			nieuweregel=uur1+":"+minuut1+":"+seconde1[0:2]+","+seconde1[3:6]+" --> "+uur2+":"+minuut2+":"+seconde2[0:2]+","+seconde2[3:6]+"\r\n"
	nieuwbestand.append(nieuweregel)
	print nieuweregel[:-2]
jn = raw_input("Bestand overschrijven? ")
if jn=="j" or jn=="J" or jn=="ja" or jn=="Ja" :
	bestand = open(bestandsnaam, "w")
	for regel in nieuwbestand :
		bestand.write(regel)
	print "Overgeschreven. Geniet van de film."
			


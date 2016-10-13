import sys
import string
# import args
for line in sys.stdin:
	line = line.strip()
	string1,string2 = line.split('\t')
	print fuzzy(string1,string2)




def fuzzy(string1,string2):
	check1 = []
	check2 = []
	s1 = list(string1)
	s2 = list(string2)
	counter = 0
	str1 = len(string1)
	str2 = len(string2) 
	for i in range(0,str1-1):
		a = s1[i]+s1[i+1]
		check1.append(a)
		i = i+1
	
	for i in range(0,str2-1):
		b = s2[i]+s2[i+1]
		check2.append(b)
	
	for i in range(0,str1-1):
		for j in range(0,str2-1):
	 		if (check1[i] == check2[j]):
	 			counter = counter + 2		
	
	score = (float(counter)/float(str2))
	#print('Your score is :' + str(score) )			
	return score


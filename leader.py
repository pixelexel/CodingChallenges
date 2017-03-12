T = int(raw_input())


list_leader = []

for j in range(T):

	length = 0 

	n = int(raw_input())

	i = 0

	for i in range(n):
	
		name = raw_input()
	
		l = list(name)

		if length<len(set(l)):
			length = len(set(l))
			leader = name

		elif length == len(set(l)):
			length = len(set(l))
			leader = min(name,leader)


	list_leader.append(leader)
	
j = 0

for j in range(T):
	print "Case #%d: %s" %(j+1,list_leader[j]) 


#https://code.google.com/codejam/contest/6304486/dashboard







T = int(raw_input())


answer = []

for i in range(T):

	l,r =  map(int,raw_input().split())
	if l > r:
		n = r
	else:
		n=l

	x = n*(n+1)/2
	answer.append(x)

for i in range(T):
	 print "Case #%d: %d" %(i+1,answer[i])


#https://code.google.com/codejam/contest/6304486/dashboard#s=p2



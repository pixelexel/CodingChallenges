
import itertools

from collections import Counter

T = int(raw_input())

finallist = []


for i in xrange(T):


	counter = 0
	countk = 0

	voters = []
	perm = []

	n,m = map(int,raw_input().split())

	for j in range(n):
		voters.append('a')
	for j in range(m):
		voters.append('b')

	#perm = list(itertools.permutations(voters))

	for k in list(itertools.permutations(voters)):

 		counta = countb = 0

		countk += 1

		for l in k:

			if l == 'a':
				counta += 1
			else:
				countb +=1

			if counta <= countb:
				counter += 1
				break


	prob = (countk - counter)/float(countk)

	finallist.append(prob)

for i in xrange(T):

	print "Case #%d: %f" %(i+1,finallist[i])

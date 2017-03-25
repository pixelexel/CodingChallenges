import string

sentence = raw_input("Enter the Sentence: ")

punctuation = [ch for ch in string.punctuation] #Adding punctuations to a list

word = ''  
tokens = []

for ch in sentence:
	if ch not in punctuation and ch != ' ':  #creating word tokens if not separated by space or punctuation
		word = word + ch
	else:
		if word != '': 
			tokens.append(word)	#word token added to list
			word = ''
		if ch != ' ':
			tokens.append(ch)	#punctuation token added to list

print tokens





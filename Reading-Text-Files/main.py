# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as text_file:
    	read = text_file.read()
    	text_file.close()
    return read


def count_words():
	text = read_file_content("./story.txt")
	# [assignment] Add your code here
	words = {}

	for word in text.split():
		if not words.get(word):
			words[word] = 1
		else:
			words[word] += 1

	return words

#print(count_words())
import re
import string
frequency = {}
document_text = open('Sports1.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b\d{4,8}\b', text_string)
 
for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    
frequency_list = frequency.keys()
 
for words in frequency_list:
        if frequency[words] > 2 :
            print (words, frequency[words])

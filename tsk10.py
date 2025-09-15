sentence = input()              
words = sentence.split()      
first_word = words[0]  
result = []            

for word in words[1:]:          
    if word != first_word:      
        unique_letters = set(word) 
        if len(unique_letters) == len(word):  
            result.append(word) 

print(', '.join(result))    

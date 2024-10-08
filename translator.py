from collections import OrderedDict

# Create an Ordered Dictionary
dic = OrderedDict()

# Read the number of words in the dictionary
count = int(input())
for _ in range(count):
    word_pair = input().strip().split()  # Read each word pair
    dic[word_pair[0]] = word_pair[1]  # Add to the dictionary

# Read the sentence to be translated
sentence = input().strip().split()

# Translate the sentence
translated_sentence = []
for word in sentence:
    if word in dic:
        translated_sentence.append(dic[word])  # Translate using the dictionary
    else:
        translated_sentence.append(word)  # Keep the original word if not in dictionary

# Print the translated sentence
print(" ".join(translated_sentence))


            
           
    

  



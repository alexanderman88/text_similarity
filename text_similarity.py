import re
import math

# Replaces contractions and punctations
def replace_contractions(document):
    
    # Dictionary of common contractions and punctuations
    contractions = {
                    "won\'t": "will not",
                    "can\'t": "can not",
                    "n\'t": " not",
                    "\'re": " are",
                    "\'s": " is",
                    "\'d": " would",
                    "\'ll": " will",
                    "\'t": " not",
                    "\'ve": " have",
                    "\'m": " am",
                    "[^\w\s]":''
    }
    
    # Replaces contractions and punctuations in document
    for item in contractions.keys():
        document = re.sub(item, contractions[item], document)
    
    return document

# Standardizes phrase and splits it into individual words.
def word_extraction(document):
    
    # Remove leading and trailing spaces
    document = document.strip()
    
    # Remove uppercase
    document = document.lower()
    
    # Replace contractions and punctuations
    document = replace_contractions(document)
    
    # Separate into individual words
    document = document.split()
    
    return document


# Creates a dictionary of every unique word and the respective word count.
def countOccurence(words):
    # Create an empty dictionary 
    d = dict() 

    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
    return d

# Calculates the cosine angle between two vectors
def cosine_similarity(d1, d2):
    
    # Creates a combined set of all the unique words in the document
    terms = set(d1).union(d2)
    
    # Calculates the dot product of document 1 vector and document 2 vector
    dot = sum(d1.get(k, 0) * d2.get(k, 0) for k in terms)
    
    # Calculates the magnitude of document 1 vector
    mag1 = math.sqrt(sum(d1.get(k, 0)**2 for k in terms))
    
    # Calculates the magnitude of document 2 vector
    mag2 = math.sqrt(sum(d2.get(k, 0)**2 for k in terms))
    
    # Calculates the cosine similarity by dividing the dot product by the product of the magnitudes of the vectors
    cosineSimilarity = dot / (mag1 * mag2)
    
    return cosineSimilarity


def main():
    
    # Asks for first document as an input.
    while True:
        try:
            doc1 = input("Enter the first document: ")
            doc1 = str(doc1)
        except:
            print("\nInvalid input\n")
            continue
        # Checks if input string is empty
        if not doc1:
            print("\nPlease enter a valid input")
        else:
            break
    
    # Asks for second document as an input.
    while True:
        try:
            doc2 = input("Enter the second document: ") 
            doc2 = str(doc2)
        except:
            print("\nInvalid input\n")
            continue
        # Checks if input string is empty
        if not doc2:
            print("\nPlease enter a valid input")
        else:
            break
    
    # Convert to individual words
    doc1 = word_extraction(doc1)
    doc2 = word_extraction(doc2)
    
    # Create word count dictionary
    d1 = countOccurence(doc1)
    d2 = countOccurence(doc2)
    
    # Calculate the similarity of the documents rounded to two decimal places
    similarity = round(cosine_similarity(d1, d2), 2)
    
    # Display the similarity of the two documents
    print("\nThe similarity of these two documents is: " + str(similarity))


main()
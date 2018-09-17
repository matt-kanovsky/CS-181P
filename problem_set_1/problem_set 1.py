import operator
import math

def dictionaryAdd(dictionary, key):
    # helper function that creates a dictonary which keeps 
    # track of the number of times a word has shown up in
    # the text file 
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

# input: txt file of words
# output: two dictionaries, one of tuples and conditional probabilities, and other other  
def populateWords(filename):
    # takes in a file name and iterates through each word
    # adding it to the dictionary
    wordDictionary = dict()
    conditionalDictionary = dict()
    condProbDictionary = dict()
    txtfile_in_list = []
    numWords = 0
    for line in filename:
        for word in line.split(): 
            if numWords > 0:
                #populate dictionary with tuples of w and w-1, and their frequency
                dictionaryAdd(conditionalDictionary, (previous_word,word))
            #populate dictionary with words and their occurences
            dictionaryAdd(wordDictionary, word)
            previous_word = word
            numWords += 1
            txtfile_in_list += [word]
    #populate dictionary with conditional probability of tuples
    for key in conditionalDictionary:
        N = wordDictionary[key[0]]
        condProb = conditionalDictionary[key] / N
        condProbDictionary[key] = condProb
    #populate dictionary with regular probabilities
    regProbDictionary = probDictionary(wordDictionary, numWords)
    return condProbDictionary, regProbDictionary, txtfile_in_list

# input: dictionary of words and their number of occurences, and number of total words in the document
# output: a dictionary with each unique word and its total probability in the document 
def probDictionary(dictionary,totalWords):
    probability_dictionary = dict()
    for key in dictionary:
        wordProb = dictionary[key]/totalWords
        probability_dictionary[key] = wordProb
    return probability_dictionary

# input: dictionary of words and their number of occurences
# output: the words with the top ten high occurence percentages
def sortDictionary(d):
    sorted_d = sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse = True)
    for i in range (0,10):
        print(i+1,":", sorted_d[i])

# input: list of words created from a txt file (alternative would be reading the file from scratch)
#        and a dictionary of words and their probabilities
# output: the entropy of the words in the document
def entropy(wordlist, dictionary):
    entropy = 0
    numWords = len(wordlist)
    for i in range(0,numWords):
        prob = dictionary[wordlist[i]]
        entropy += math.log(prob,2)
    entropy = entropy * (-1/numWords)
    return entropy

# input: list of words created from a txt file (alternative would be reading the file from scratch)
#        and a dictionary of words and their conditional probabilities
# output: the entropy of the words in the document
def cond_entropy(wordlist, dictionary):
    entropy = 0
    numWords = len(wordlist)
    for i in range(1,numWords):
        key = (wordlist[i-1], wordlist[i])
        prob = dictionary[key]
        entropy += math.log(prob,2)
    entropy = entropy * (-1/(numWords-1))
    return entropy

def main():
    testfile = open("corpus.txt","r")
    cond_dict, reg_dict, txtlist = populateWords(testfile)
    print(len(reg_dict))
    print(len(cond_dict))
    print(len(txtlist))
    sortDictionary(reg_dict)
    test_ent = entropy(txtlist,reg_dict)
    test_cond_ent = cond_entropy(txtlist, cond_dict)
    print(test_ent)
    print(test_cond_ent)

if __name__ == "__main__":
    main()
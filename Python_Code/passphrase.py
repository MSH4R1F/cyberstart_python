with open("/tmp/randomwordsnumbers.txt", "r") as file:
    data = file.read()
        
wordNumbers = data.rstrip().split("\n")
with open("/tmp/words.txt", "r") as file1:
    data1 = file1.read()
    words = data1.rstrip().split("\n")
    word1 = int(wordNumbers[0])
    word2 = int(wordNumbers[1])
    word3 = int(wordNumbers[2])
    print("%s %s %s" %(words[word1], words[word2], words[word3]))

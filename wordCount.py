# to detect the Product purchase frequency
f=open("D:/imp/Python/test/shineDiscussion.txt", 'r')
word_fre ={}
lines = f.readlines()
for x in lines:
    wordset= x.strip().split(" ")
    for word in wordset:
        freq = 1
        try:
            freq = word_fre[word] + 1
        except KeyError:
            pass
        word_fre[word]= freq
print("Word Frequency in this document is =%s" % word_fre)

print("Formatted Output of the above section")

for word in word_fre:
    print("Word: '%s'  occurred %d times" % (word, word_fre[word]))
   


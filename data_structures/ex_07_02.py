fname = input("Enter a file name: ")
fhandle = open(fname, 'r')
spam_confidence = 0
count = 0
for line in fhandle:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        s_spam_prob = line[line.find(":") + 1 : ]
        spam_prob = float(s_spam_prob)
        spam_confidence = spam_confidence + spam_prob
print("Average spam confidence: ", spam_confidence / count)

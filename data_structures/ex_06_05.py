str = 'X-DSPAM-Confidence:0.8475'
ipos = str.find(":")
value = float(str[ipos + 1: ])
print(value)

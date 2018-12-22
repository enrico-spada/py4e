sH = input("Enter Hours: ")
sR = input("Enter Rate: ")
try:
    fH = float(sH)
    fR = float(sR)
except:
    print("Error: please enter a numeric input")
    quit()

print(fH, fR)
if fH > 40:
    ord = fR * 40
    ovr = (fR * 1.5) * (fH - 40)
    pay = ord + ovr
else:
    pay = fH * fR
print("Pay: ", pay)

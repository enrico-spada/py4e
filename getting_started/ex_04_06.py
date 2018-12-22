def computepay(H, R):
    if H > 40:
        ord = R * 40
        ovr = (R * 1.5) * (H - 40)
        pay = ord + ovr
    else:
        pay = H * R
    return pay

sH = input("Enter Hours: ")
sR = input("Enter Rate: ")
try:
    fH = float(sH)
    fR = float(sR)
except:
    print("Error: please enter a numeric input")
    quit()

print(fH, fR)
print("Pay: ", computepay(fH, fR))

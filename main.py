def computepay(h,r):
    if h > 40:
        pay = (h-40)*r*1.5+40*r
    else:
        pay = h*r
    return pay

h = float(input('Enter Hours: '))
r = float(input('Enter rate: '))
p = computepay(h,r)
print('Pay is ', p)
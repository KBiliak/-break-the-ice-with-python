# Write a program that computes the value of a+aa+aaa+aaaa with a given digit
# as the value of a.
#
# Suppose the following input is supplied to the program:
#
# 9
# Then, the output should be:
#
# 11106
# 9 + 99 + 999
digit = "9"
r = range(4)
l = []
for a in r:
    a *= a
    l.append(digit)
    a *= l

print(l)
    # l.append(digit)
    # print(digit)
# for digit in

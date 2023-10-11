s = input()
count = lambda s, c: sum(1 for i in s if i == c)
print("yes" if count(s, '0') == count(s, '1') else "no")

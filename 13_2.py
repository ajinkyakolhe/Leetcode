s = "MCMXCIV"
if not s:
    print( 0)
dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
n = len(s)
total = dic[s[n-1]]
for i in range(n-1,0,-1):
    current = dic[s[i]]
    prev = dic[s[i-1]]
    #total += prev if prev >= current else -prev
    if prev >= current:
        total+= prev
    else:
        total-=prev
print( total)

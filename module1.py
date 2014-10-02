dic = {}
string = raw_input("enter string")
l  = string.split(" ")
for i in l:
    if dic.has_key(i):
        dic_key = dic[i] +1
        dic[i] = dic_key
    else:
        dic[i]=1
print dic

v= dic.values()

v.sort(reverse=True)

print v
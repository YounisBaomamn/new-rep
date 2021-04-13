dic = {'a':1,'b':4,'c':5,'d':2}
r =  dic.get('s',3)
print(r)
p =list( dic.values())
# branch
print(p)
#e
e= list( dic.items())
for key , val in dic.items():
    print(val)
    
x = list( dic.keys())
print(x)


#print
print(dic.items())
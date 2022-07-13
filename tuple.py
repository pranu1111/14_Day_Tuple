s=("p","s","c")
# print(type(s))
# print(len(s))
a=("a",)
# print(type(s))
mytup=tuple(("sweety","soni","moni"))
# print(type(mytup))
# print(mytup[1])
# print(mytup[-1])
# print(mytup[-2])

thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])
# print(thistuple[:4])
# print(thistuple[-7:-2])
# print(thistuple[-5:-1])
# print(thistuple[-6:-3])

# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# # y=list(thistuple)
# print(type(y))
# y[1]='grapes'
# print(y)
# thistuple=tuple(y)
# print(type(thistuple))
# print(thistuple)

thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

y=("s",1.11)
# thistuple += y
# print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)
del thistuple
# print(thistuple)

# unpacking item..............
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# (a,b,c,d,e,f,g)=thistuple1
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)

x=('g','d','r',1,8,3,2,2)
print(x.count(2))
print(x.index(2))
print(x.index("g"))
print(x.index("r"))
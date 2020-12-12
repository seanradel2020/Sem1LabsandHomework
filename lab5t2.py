#Sean Radel
#task2 Lists

playlist =[
"Dark Entries",
"Bela Lugosi's Dead",
"Third Uncle",
"All We Ever Wanted Was Everything", "The Three Shadows",
"She's in Parties",
"Hollow Hills",
"The Man With the X-Ray Eyes"
]

for i in range(len(playlist)):
    print(playlist[i])
print()
for k in range(len(playlist),0,-1):
    print(playlist[k-1])
print()
for q in range(0,len(playlist),2):
    print(playlist[q])

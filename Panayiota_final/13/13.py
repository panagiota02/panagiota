def pair_print_remove (list_lex,list_size_l):
    lex=list_lex
    size_l=list_size_l
    thesi=0
    print("\nPair of words with sum equal to 20 characters")
    print("_____________________________________________\n")
    while thesi<len(size_l):
        found_pair=False
        x=0
        while found_pair==False and x<len(size_l):
            if thesi!=x and (size_l[thesi] + size_l[x] == 20):
                       print("%20s\t%20s"%(lex[x],lex[thesi]))
                       size_l.pop(x)
                       lex.pop(x)
                       size_l.pop(thesi)
                       lex.pop(thesi)
                       found_pair=True
                       thesi-=1
            else:                                              
                    x+=1
        thesi+=1
   
text=open("data.txt","r")        
lexis=[]
size_lexis=[]
lexis.clear()
size_lexis.clear()
line=text.readline()
no=0
while line != "":
    words=line.split(" ")
    for i in range (0,len(words)):
        lexis.append(words[i].strip())
        size_lexis.append(len(words[i]))
        no+=1
    line=text.readline()
print("%20s%20s"%("Words","Sizes"))
print("%20s"%("_____________________________________________________\n"))
for i in range (0,no):
    print("%20s%20s"%(lexis[i],size_lexis[i]))
pair_print_remove (lexis,size_lexis)
text.close()


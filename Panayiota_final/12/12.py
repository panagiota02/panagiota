text=open("data.txt","r",encoding='utf-8')
def convert_char (w):
    convert_to_bytes = bytes(w, 'cp1252')
    convert_to_int=int.from_bytes(convert_to_bytes, "big")
    temp=convert_to_int
    convert_to_int=255-convert_to_int
#   print("before katoptrikos:\t" + str(temp) +"\tkatoptrikos: " + str(convert_to_int))
    convert_to_bytes_again=bytes([convert_to_int])
    result=convert_to_bytes_again.decode('latin-1')
    return result

line=text.readline()
while line != "":
    line=line[0:len(line)-1]
    words=line.split(" ")
    new_line=""
    for i in range (0,len(words)):
        kathe_lexi=""           
        for j in range (0,len(words[i])):
              each_char=convert_char(words[i][j])
              kathe_lexi+=each_char          
        new_line+=" "
        new_line+=kathe_lexi
    for i in range (len(new_line)-1,-1,-1):  
        print(new_line[i],end="")
    print()
   
    line=text.readline()
    line.strip()

text.close()


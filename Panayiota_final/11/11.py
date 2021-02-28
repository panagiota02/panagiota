import ast
#recursion
def get_all_values(nested_dictionaries,keys_list):   
    for key, value in nested_dictionaries.items():       
        if type(value) is dict:
            get_all_values(value,keys_list)            
        else:
            keys_list.append(key)
            
def find_key_with_max_appearance(keys_list):
    max_key=""
    max_no=0
    for i in keys_list:
        cnt=0
        for j in range (0,len(keys_list)):
           if i == keys_list[j]:
                cnt=cnt+1
        if cnt > max_no:
             max_no=cnt
             max_key=i
    return max_key,max_no

         
nested_dict_file=open("data.txt","r")
keys_list=[]
n_d=nested_dict_file.read()
nested_dictionaries = ast.literal_eval(n_d)
get_all_values(nested_dictionaries,keys_list)
print("Extracted keys from file are: " + str(keys_list))
m_key,m_no=find_key_with_max_appearance(keys_list)
print("The dictionaries key which appearces mosts is:  " + m_key)
print("Total number of appearance is: " + str(m_no))
nested_dict_file.close()

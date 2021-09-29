lst = [1,2,3,'a'] 
dist = {'A':[1,2,3], 'B':['a','b','c']}
string="hello bhai"
print(isinstance(string, (str, dict,list)))

emplyoee_list = [['Ashok','Patil',21],['Seema','Gali',48],['Kulwinder','Singh',52],['Lata','Agrwal',25],['Pooja','Shetty',35]] 
print("The given list of lists is as follows :")
print(emplyoee_list)
print("\n")
print ("Sorting the list of lists using lambda is as follows:")
emplyoee_list.sort(key = lambda i: i[2])
print(emplyoee_list)
my_dict = {'Prokhor' : 2002 , 'Zlata' : 2002} #работа с словарями
print(my_dict)
print(my_dict['Prokhor'])
my_dict['Vika']=1995
print(my_dict)
my_dict.update({'Den':1987,'Pasha':1997})
print(my_dict)
a=my_dict.pop('Pasha')
print(my_dict)
my_set={13,21,10,'Vova',13,10}#работa с множествами
print(my_set)
print(my_set.add(14),my_set.add(15))
print(my_set)
my_set.discard('Vova')
print(my_set)
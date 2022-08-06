import re

sql_script="SELECT a.uid, b.uname FROM (select * from user WHERE 1=1  GROUP BY 1,2) a, (select * from user_details) b;"
# ABOVE QUERY WE HAVE TO EDIT WITH OUR REQUIRED QUERY

sub1 = "SELECT"
sub2 = "FROM"
idx1 = sql_script.find(sub1)
idx2 = sql_script.find(sub2)
res1 = sql_script[idx1 + len(sub1) + 1: idx2]
res2=res1.split(',')
res3=[i.strip() for i in res2]
#print(res3) #output['a.uid', 'b.uname']


X=re.findall(r'FROM(.*?)\)*\,', sql_script)
Y=re.findall(r'FROM(.*?)\)*\;', sql_script)
Z=[i.strip() for i in Y]
#print(Z) #output['(select * from user WHERE 1=1 GROUP BY 1,2) a, (select * from user_details) b']


Z1=[i.replace(')','').split('(select') for i in Z]
#print(Z1) #output[['', ' * from user WHERE 1=1 GROUP BY 1,2 a, ', ' * from user_details b']]


Z2=[]
for x in Z1[0]:
   if x == '':
       pass
   else :
       y1=x.strip().replace(',','')
       Z2.append(y1)

#print(Z2) #output['* from user WHERE 1=1 GROUP BY 12 a', '* from user_details b']

Z3=[i.split('from')[1].strip() for i in Z2]
#print(Z3) #output['user WHERE 1=1 GROUP BY 12 a', 'user_details b']

z6=dict(zip([i.split(' ')[-1] for i in Z3],[i.split(' ')[0]  for i in Z3]))
#print(z6) #output{'a': 'user', 'b': 'user_details'}

print('column => table')
for x in res3:
   y2=x.split('.')[0]
   k=x
   v=z6.get(y2)
   print(x.split('.')[-1],'=>',z6.get(y2))

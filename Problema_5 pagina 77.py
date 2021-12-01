with open ("C:\\Users\\User\\Desktop\\Новая папка (2).txt",'w') as f:
    f.write(str(input('')))
with open('C:\\Users\\User\\Desktop\\Новая папка (2).txt','r') as f :
    x=f.read()
print(x)
z=0
for i in x:
    if i in ['a','e','i','u','o','A','E','U','I','O']:
        z=+1
print('mesajul are', z, 'vocale')
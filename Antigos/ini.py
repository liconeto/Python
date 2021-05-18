Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=1
>>> b=2
>>> a == b
False
>>> a != B
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a != B
NameError: name 'B' is not defined
>>> a != b
True
>>> a > b
False
>>> a < a
False
>>> a < b
True
>>> 2 * a >= b
True
>>> 3 * a > = b # loco em
SyntaxError: invalid syntax
>>> 3 * a >= b
True
>>> 2 ** 3 # É o mesmo que 2 2³ (dois ao cubo)
8
>>> 2 ** (3+6) # Dois elevado a 9
512
>>> 7 % 2
1
>>> 2 ** (3+6) % 7
1
>>> valor1=2
>>> valor1
2
>>> type(valor1)
<class 'int'>
>>> valor1='Boa Tarde!'
>>> valor1
'Boa Tarde!'
>>> type(valor1)
<class 'str'>
>>> palavra='termodinâmica'
>>> palavra
'termodinâmica'
>>> print palavra
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(palavra)?
>>> print(palavra)
termodinâmica
>>> palavra[2]
'r'
>>> 2 * palavra[0]
'tt'
>>> palavra[9:12]
'mic'
>>> print(palavra[:9])
termodinâ
>>> print(palavra[:])
termodinâmica
>>> palavra[1:8:2]
'emdn'
>>> palavra[7:0:-1]
'nidomre'
>>> palavra[7::-1]
'nidomret'
>>> palavra[::-1]
'acimânidomret'
>>> palindromo='socorram me subi no onibus em marrocos'
>>> palindromo[::-1]
'socorram me subino on ibus em marrocos'
>>> palavra = palavra+' aplicada'
>>> print(palavrra)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(palavrra)
NameError: name 'palavrra' is not defined
>>> print(palavra)
termodinâmica aplicada
>>> palavra[14:]
'aplicada'
>>> len (palavra)
22
>>> lista=[1,2,3]
>>> lista
[1, 2, 3]
>>> lista[0]
1
>>> lista[0]+lista[2]
4
>>> lista=lista+[4]
>>> lista
[1, 2, 3, 4]
>>> lista+4
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lista+4
TypeError: can only concatenate list (not "int") to list
>>> lista=lista[0,0,0]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    lista=lista[0,0,0]
TypeError: list indices must be integers or slices, not tuple
>>> lista=lista+[0,0,0,]
>>> lista
[1, 2, 3, 4, 0, 0, 0]
>>> lista[0]='zero'
>>> lista
['zero', 2, 3, 4, 0, 0, 0]
>>> lista[1 = lista[1]+lista[2]
	  
SyntaxError: invalid syntax
>>> lista[1] = lista[1]+lista[2]
	  
>>> lista
	  
['zero', 5, 3, 4, 0, 0, 0]
>>> lista[2] = lista[0]
	  
>>> lista
	  
['zero', 5, 'zero', 4, 0, 0, 0]
>>> a='Boa tarde!'
	  
>>> a=[0]='N'
	  
SyntaxError: can't assign to literal
>>> a[0]='N'
	  
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a[0]='N'
TypeError: 'str' object does not support item assignment
>>> linha1=[1,2,3]
	  
>>> linha2[0,-1,1]
	  
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    linha2[0,-1,1]
NameError: name 'linha2' is not defined
>>> linha2=[0,-1,1]
	  
>>> linha3[3,3,3]
	  
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    linha3[3,3,3]
NameError: name 'linha3' is not defined
>>> linha3=[3,3,3]
	  
>>> matriz=[linha1,linha2,linha3]
	  
>>> matriz
	  
[[1, 2, 3], [0, -1, 1], [3, 3, 3]]
>>> matriz[1]
	  
[0, -1, 1]
>>> matriz[1][2]
	  
1
>>> tupl=(1,2,3)
	  
>>> tupl
	  
(1, 2, 3)
>>> tupl[0]=0
	  
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    tupl[0]=0
TypeError: 'tuple' object does not support item assignment
>>> a,b = 0,'Deu certo?'
	  
>>> a
	  
0
>>> b
	  
'Deu certo?'
>>> a,b=b,a
	  
>>> a
	  
'Deu certo?'
>>> b
	  
0
>>> aurelio={'denominação':'Ilha Solteira','população':23000,'renda':1500}
	  
>>> aurelio
	  
{'denominação': 'Ilha Solteira', 'população': 23000, 'renda': 1500}
>>> aurelio['vocação']='turismo'
	  
>>> aurelio
	  
{'denominação': 'Ilha Solteira', 'população': 23000, 'renda': 1500, 'vocação': 'turismo'}
>>> aurelio['reda']
	  
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    aurelio['reda']
KeyError: 'reda'
>>> aurelio['renda']
	  
1500
>>> aurelio['renda']=aurelio['renda']+200
	  
>>> aurelio['renda']
	  
1700
>>> aurelio.keys()
	  
dict_keys(['denominação', 'população', 'renda', 'vocação'])
>>> aurelio.has_key('idade')
	  
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    aurelio.has_key('idade')
AttributeError: 'dict' object has no attribute 'has_key'
>>> aurelio['idade']=33
	  
>>> aurelio.dict()
	  
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    aurelio.dict()
AttributeError: 'dict' object has no attribute 'dict'
>>> aurelio.keys()
	  
dict_keys(['denominação', 'população', 'renda', 'vocação', 'idade'])
          
>>> 

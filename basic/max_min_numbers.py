import time
try:
    p = int(input('Digite o primeiro valor: ')) 
    s = int(input('Digite o segundo valor: '))  
    t = int(input('Digite o terceiro valor: ')) 
except ValueError:
    print('Erro. Digite apenas números.')


#menor
menor = p
if s<p and s<t:
    menor = s
if t<p and t<s:
    menor = t

#maior
maior = s
if p>s and p>t:
    maior = p
if t>s and t>p:
    maior = t
print('carregando...')
time.sleep(3)
print ('O menor valor é {}'.format(menor),)
time.sleep(0.5)
print('O maior valor é {}'.format(maior))


from time import sleep
def maior(*num):
    print('-='*25)
    mai = cont = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont+=1
    print(f'foram digitados {cont} valores')
    print(f'O maior valor digitado foi: {mai}')


maior(1,4,3,6,4,5,4)
maior(5,7,34,7,54,6,4,2)
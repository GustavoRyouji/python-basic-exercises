from datetime import datetime
def voto(nasc):
    r1 = "Negado"
    r2 = "opcional"
    r3 = "Obrigatório"
    idade = datetime.now().year - nasc
    if 16 <= idade < 18 or idade > 65:
        return print(f"com {idade} anos, o voto é {r2}")
    elif idade >18:
        return print(f"com {idade} anos, o voto é {r3}")
    else:
        return print(f"com {idade} anos, o voto é {r1}")


n = int(input('Qual ano você nasceu?: '))
voto(n)


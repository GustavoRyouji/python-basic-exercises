import urllib
import urllib.request
# Exemplo de teste de conexão com um site.
# Alguns sites modernos podem retornar HTTP 403 (Forbidden)
# por bloquearem requisições automatizadas.
site = input('Digite um URL: ')
try:
    urllib.request.urlopen(site)
except Exception as erro:
    print("Deu erro.")
    print(erro.__class__.__name__)
else:
    print('tudo ok.')
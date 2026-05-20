def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] < 6:
            r['situação'] = 'ruim'
        elif 6 < r['media'] < 7:
            r['situação'] = 'bom'
        else:
            r['situação'] = 'ótimo'
    return r


resp = notas(5.5, 5.5, 9, sit=True)
print(resp)

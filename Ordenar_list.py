#from a random list of int numbers, the output must be a sorted list from 1 to 15+0
puzzle= [[10,3,6,4],[1,5,8,0],[2,13,7,15],[14,9,12,11]]

def tes():
    list=[]
    n = 0
    for l in puzzle:
        for i in puzzle[n]:
            list.append(i)
        n += 1
    print (f'Original: {list}')
    lista=sorted(list)
    print(f'Sorted: {lista}')
    lista.append(0)
    lista.remove(0)
    print(f'FINAL: {lista}')
    resuelto = []
    chunk = 4
    for i in range(0, len(lista), chunk):
        resuelto.append(lista[i:i + chunk])
    print(f'Aquí está resuelto: {resuelto}')
    return resuelto


puzzok = tes()


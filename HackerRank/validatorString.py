def mutate_string(string, position, character):
    stringEnLista = list(string)
    stringEnLista[position] = character
    stringEnLista = ''.join(stringEnLista)
    
    return stringEnLista

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

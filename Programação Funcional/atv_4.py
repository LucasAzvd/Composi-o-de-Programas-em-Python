def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    """
    return map(lambda x: x[-1], L)

def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus']]
    print(list(citations(L)))
    """
    return map(lambda x: (x[0][0].capitalize() + ". " +x[-1]), L)

def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    print(list(fullCitations(L)))
    print((fullCitations(L)))
    Note que as iniciais precisam estar capitalizada.
    """
    lista_nome = []
    for i in L:
        for j in i:
            if j == i[-1]:
                nome += ". " + j
            elif j == i[0]:
                nome = j[0].upper()
            else:
                nome += ". " + j[0].upper()
        lista_nome.append(nome)
    # map(lambda x: (x[0][0].capitalize() + ". "+ x[1][0].capitalize() + ". " +x[-1]), L)
    return lista_nome
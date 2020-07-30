from atv_3 import Livro, CestaCompras, Brinquedo

livro1 = Livro("Senhor dos Aneis", 15.00)
brinq1 = Brinquedo("Carrinho", 12.99)

cesta = CestaCompras()
cesta.adicionar_item(livro1, 3)
cesta.adicionar_item(brinq1, 4)

cesta.relatorio_final()

for item, qtde in cesta.itens.items():
    print("%s, %i" % (item.nome, qtde))

"""
Saída esperada:

93.01
Livro, Senhor dos Aneis, 3, 15.00, 45.00, 43.65
Brinquedo, Carrinho, 4, 12.99, 51.96, 49.36
"""

"""
--- Input ---
 1
L;Senhor dos Aneis;15.00;3
B;Carrinho;12.99;4
E;Televisor;259.00;1

--- Program output ---
331.29
Livro, Senhor dos Aneis, 3, 15.0, 45.0, 43.65
Brinquedo, Carrinho, 4, 12.99, 51.96, 49.36
Eletronico, Televisor, 1, 259.0, 259.0, 238.28

--- Expected output (text)---

331.29
Livro, Senhor dos Aneis, 3, 15.00, 45.00, 43.65
Brinquedo, Carrinho, 4, 12.99, 51.96, 49.36
Eletronico, Televisor, 1, 259.00, 259.00, 238.28

Test 4: 2b
Incorrect program output
--- Input ---
 1
L;Livro1;2.99;4
L;Livro2;12.5;1
L;Livro3;9.25;2
L;Livro4;4;3
B;Brinquedo1;29.8;2
B;Brinquedo2;37.5;2
E;Eletr1;125;1
E;Eletr2;399.5;1
E;Eletr3;249.99;1

--- Program output ---
893.71
Livro, Livro1, 4, 2.99, 11.96, 11.6
Livro, Livro2, 1, 12.5, 12.5, 12.12
Livro, Livro3, 2, 9.25, 18.5, 17.95
Livro, Livro4, 3, 4.0, 12.0, 11.64
Brinquedo, Brinquedo1, 2, 29.8, 59.6, 56.62
Brinquedo, Brinquedo2, 2, 37.5, 75.0, 71.25
Eletronico, Eletr1, 1, 125.0, 125.0, 115.0
Eletronico, Eletr2, 1, 399.5, 399.5, 367.54
Eletronico, Eletr3, 1, 249.99, 249.99, 229.99

--- Expected output (text)---

893.71
Livro, Livro1, 4, 2.99, 11.96, 11.60
Livro, Livro2, 1, 12.50, 12.50, 12.12
Livro, Livro3, 2, 9.25, 18.50, 17.95
Livro, Livro4, 3, 4.00, 12.00, 11.64
Brinquedo, Brinquedo1, 2, 29.80, 59.60, 56.62
Brinquedo, Brinquedo2, 2, 37.50, 75.00, 71.25
Eletronico, Eletr1, 1, 125.00, 125.00, 115.00
Eletronico, Eletr2, 1, 399.50, 399.50, 367.54
Eletronico, Eletr3, 1, 249.99, 249.99, 229.99
"""

def concatenate(**itens):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in itens.values():
        result += arg+', '
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
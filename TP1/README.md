# TP1

## Autor: João Lopes, A100829

Para resolver o problema comecei por ler o ficheiro *csv* e criar instâncias da classe Atleta para cada atleta no ficheiro, instâncias essas que foram adicionadas a uma lista.

De modo a obter todas as modalidades ordenadas criei um *set* para evitar modalidades repetidas e adicionei a modalidade de todos os atletas na lista, por fim converti o *set* numa lista que foi ordenada alfabeticamente.

Para obter as percentagens de atletas aptos e inaptos percorri a lista e dependendo do valor do campo **resultado** incrementei um inteiro, sendo que existem dois inteiros que começam a 0, um para aptos e outro para inaptos. Por fim apenas multipliquei cada inteiro por 100 e dividi pelo número total de atletas para obter os resultados como percentagens.

Para distribuir os atletas por escalões etários comecei por descobrir as idades do atleta mais novo e do mais velho, com essa informação é possível calcular o número de intervalos de 5 anos que são necessários. Criei então um dicionário cujos valores são inteiros que começam a 0 e cujas chaves são o limite inferior do intervalo de idades, ou seja, para o intervalo **20-24** a chave é **20**, para o intervalo **25-29** a chave é **25**, etc. De seguida, percorro todos os atletas da lista e calculo o multiplo de 5 mais próximo da idade do atleta, valor esse que vai ser sempre uma das chaves do dicionário, o valor associado a essa chave é então incrementado.
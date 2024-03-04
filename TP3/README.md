# TP3

## Autor: João Lopes, a100829

Para resolver o problema do somador on/off utilizei a seguinte expressão *regex*: `(on|off|=|\d+)`. Esta expressão em conjunto com a função `re.findall()` com a flag `re-IGNORECASE` é capaz de encontrar todas as ocorrências de *on*, *off*, *=* e qualquer número inteiro no *input*. Sendo que o resultado da função `re.findall()` é uma lista com todas as *matches* ordenadas, o resto do problema consiste em apenas verificar a que cada elemento da lista corresponde e atualizar o valor da soma e o *boolean* que indica se é para continuar a somar, tendo em conta o valor de dito elemento da lista.
# TP2

## Autor: João Lopes, A100829

Usei maioritariamente expressões *regex* através do método `re.sub()` para converter o texto *markdown* para *html*.

Para *headers* usei a expressão `r"(#+) (.+)"` para encontrar os *headers markdown* e a função *headers_to_html* para fornecer a expressão de substituição, nesta função calculo o número de `#` através do primeiro grupo de captura para saber que tipo de *header* está a ser convertido e crio a expressão de substituição para *html* correspondente, com o texto no segundo grupo de captura.

Para *bold* usei a expressão `r"\*\*(.+)\*\*"` para encontrar texto em *bold* e a expressão `r"<b>\1</b>"` como substituição, efetivamente substituí os asteriscos por `<b>`, mantendo o texto igual através do grupo de captura.

O processo para itálico é bastante semelhante ao de *bold*, apenas mudo as expressóes *regex*, para encontrar texto em itálico uso a expressão `r"\*(.+)\*"` e para substituição a expressão `r"<i>\1</i>"` com o texto no grupo de captura.

De modo a converter imagens uso a expressão `r"!\[(.+)\]\((.+)\)"` para encontrar as imagens em *markdown*, esta expressão tem dois grupos de captura, um que captura o *link* da imagem e outro que captura a descrição. Para converter para *html* uso a expressão `r'<img src="\2" alt="\1"/>'` com os grupos de captura que guardaram os dados que quero converter.

Para converter *links* uso a expressão `r"\[(.+)\]\((.+)\)"` para encontrar *links* em *markdown* e a expressão `r'<a href="\2">\1</a>'` para converter os *links* para *html*, tal como nas imagens, os grupos de captura guardam o *link* e a descrição.

É necessário que as imagens sejam convertidas antes dos *links* porque a expressão *regex* dos links tambem dá *match* com as imagens em *markdown*, visto que as imagens em *markdown* têm um `!` no início e de resto são iguais aos *links*, isto faria com que o conversor transformasse as imagens em *links* no *html* se não fossem convertidas previamente.

Para converter listas numeradas precisei de ler o texto linha a linha, para cada linha verifico se a expressão `r"(\d+)\. (.+)"` dá *match* através do método `re.match()`, se o resultado for uma ***Match*** verifico se é o primeiro elemento de uma lista através do valor da variável ***curr_list_number***, inicializada a 0. Se for o primeiro elemento, `curr_list_number == 0`, adiciono a uma lista de *strings* a *string* `f"<ol>\n    <li>{m.group(2)}</li>"`, caso não seja o primeiro adiciono `f"    <li>{m.group(2)}</li>"`, por ultimo altero o valor da variável ***curr_list_number*** para ser igual ao valor do primeiro grupo de captura que é o número do item da lista, sendo o segundo grupo de captura o conteúdo do item da lista. Se o resultado de `re.match()` for ***None*** existem duas possibilidades, se o valor de ***curr_list_number*** for 0 significa que não existem listas por fechar e então apenas adiciono a linha à lista, se o valor for diferente de 0 significa que uma lista terminou na linha anterior e portanto adiciono `</ol>` à lista antes de adcionar a própria linha e por último volto a colocar ***curr_list_number*** a 0.

Devido à conversão de listas ser a última etapa, todas as linhas na lista de *strings* estão convertidas para *hmtl* e então apenas junto os elementos da lista numa só *string*, separados por `\n`.
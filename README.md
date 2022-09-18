# Crossbots
códigos do processo seletivo

### Os códigos estão com comentários sobre o que cada função faz, neste arquivo pretendo explicar o desenvolvimento do raciocínio por trás dos códigos

#### muito_simples_p1:
  Decidi calcular a distancia pela fórmula da distancia entre dois pontos, porém para isso seria necessário com que houvesse algo que calculasse a distancia entre as respectivas coordenadas e as elevasse ao quadrado, eu não quis fazer uma outra função que só fizesse isso, então optei por usar uma lambda, entretanto como eu teria que usar essa lambda duas vezes eu decidi nomea-la, o resto foi apenas a aplicação da fórmula e o arredondamento do resultado
  
#### muito_simples_p2:
  Pesquisei no google a fórmula de conversão de fahrenheit para graus e fiz a aplicação direta na função

#### simples_p1: 
  Decidi fazer uma função que fizesse a soma de duas posições em um vetor, caso seja necessário que o código seja utilizado mais de uma vez. E a lista de valores com 10 posições será pedida ao usuario fora da função, optei por fazer um type casting diretamente no valor recebido pelo input para reduzir as linhas de código
 
#### simples_p2:
  Dentro da função, optei por fazer uma list comprehension para achar os divisores do número, que serão aqueles que estão entre 1 até metade inteira do número (coloquei o +1 por precaução) com o resto da divisão igual a zero. Esses valores são automaticamente adicionados na lista, então eu apliquei a função sum() para somar todos os valores dessa lista caso essa soma seja igual ao número significa que ele é perfeito, retornando True, do contrário retorna False

#### simples_p3:
  Creio que o código não seja o mais eficiente, porém na iteração para veficar se o número é primo há uma variavel de controle, em que a cada divisor do número ela é incrementada em 1, no final do loop é verificada se o seu valor é igual a 1, indicando que o divisor do número é só o 1, implicando que ele seja um número primo.
  
#### simples_p4:
  Decidi usar a função count() para reduzir a quantidade de linhas do código e não precisar criar uma variavel e iterar sobre a string contando quantas vezes a letra passada aparece

#### intermediario_p1:
  Para achar o angulo entre os 3 pontos, decidi fazer dois vetores e aplicar a fórmula do ângulo entre dois vetores: acos = v1.v2 / (|v1|*|v2|)
  Nomeei uma lambda novamente que calculava o módulo do vetores, não quis criar uma função separada para isso para economizar linhas de código.
  Decidi calcular os vetores juntando as respectivas coordenadas em uma tupla com o zip e fazendo uma lista com a subtração das respectivas coordenadas
  O produto interno/produto escalar dos vetores eu fiz da mesma forma, porém em vez de subtrair as respectivas coordenadas elas são multiplicadas e depois somadas
  Tendo todas as variaveis, calculei o angulo com a fórmula, porém a função acos da biblioteca math retorna o angulo em radianos, assim foi necessário converter para graus e arredondar o resultado.
  
#### intermediario_p2:
  Como só era necessário eliminar os números repetidos, eu decidi converter a lista para um set/conjunto, para que os valores repetidos fossem eliminados e depois reconverti para uma lista

#### dificil_p1: 
  Optei por usar a biblioteca re, já que particularmente eu a acho a melhor quando se é para encontrar padrões dentro de strings, primeiramente eliminei todos os caracteres que fossem diferentes de "<" ou ">", depois fiz um loop que enquanto encontrasse o padrão "<>" irá continuar funcionando, quando o padrão "<>" é encontrado é buscado todas as ocorrências dele na string passada, essas ocorrencias são adicionadas a uma variável, após isso todos os "<>" são eliminados, voltando para a condição do loop. Quando não houver mais "<>" o loop para e é retornado o valor da variavel com as ocorrencias do "<>"
  
#### dificil_p2:
  Deicidi fazer uma classe pois fiz relativamente bastante funções e elas tem que ser usadas em uma certa ordem, com a classe eu posso forçar essa ordem a ocorrer e deixar o código mais organizado.
  Procurei encontrar primeiramente aonde os reis estavam localizados no tabuleiro, tendo a posição do rei eu decidi "olhar" em torno do rei para ver se alguma peça poderia estar o atacando. Com isso eu fiz os movimentos que cada peças teriam, como para os cavalos e os peoes não é necessário verificar se há alguma peça bloqueando o ataque, eu decidi os fazer primeiro. 
  Eu estava buscando uma forma de fazer os movimentos sem ter que fazer uma cadeia de if's e elif's e consegui achar um método de ver quantas casas cada peça andam em seu movimento, tanto em linhas quanto nas colunas, e coloquei isso dentro de uma lista de tuplas. Com isso eu fiz um loop nessa lista e buscava se na posição em que o rei estava mais a respectiva linha e coluna do movimento da peça, havia a própria peça, caso houvesse significaria que o rei estaria em cheque, isso para o caso do cavalo e do peao
  Já para o caso da torre, bispo e rainha, é necessário ver se há alguma peça que esteja antes do atacante, assim bloqueando o ataque. Para isso eu usei uma lógica semelhante ao do movimento do cavalo, que seria fazer uma lista de tuplas com as possiveis posicoes em que uma torre/bispo poderia estar. Com isso eu fiz um método de classe responsável por ver se em volta do rei há alguma peça na direção do possível ataque, se houver já é retornado False, ou seja, que o rei não está em cheque, porém caso não haja essa peça na direção do possível ataque é feito um loop até o fim/começo do tabuleiro, se alguma peça que não ataque naquela direção for encontrada é retornado False, porém se for encontrado uma peça que ataque naquela direção é retornado True
  O método de classe principal seria o de checar se os reis estão em cheque, ele irá chamar automoticamente o dos ataques e verificar se algum deles retorna True, significando que o rei está em cheque.
  Tive a ideia de adicionar um parametro booleano nos métodos de ataque e de achar a posição do rei, para que fosse possível utilizar os mesmos, tanto para encontrar o rei branco como o rei preto
  
  
 
  
  

class Tabuleiro():
    """ Uma classe que simula um tabuleiro de xadrez e analisa se algum dos reis está em cheque

    A instância de classe irá necessariamente precisar de quantos "tabuleiros" (quantas vezes o código será executado),
    para usar a classe é necessário instancia-la, após isso utilizar o método: adicionar_tabuleiro() e inserir as linhas
    com as devidas posições das peças, depois de se acrescentar as 8 linhas do tabuleiro deve-se se inserir uma linha em
    branco. Posteriormente, deve-se utilizar o método checar_reis() para verificar se algum dos reis está em cheque

    """

    def __init__(self, qntd_execucao):
        """ Uma função para inicializar a clase

        :param qntd_execucao: Quantidade de vezes que o código será executado
        """

        self.qntd_execucao = qntd_execucao
        self.tabuleiros = []  # Uma variável que irá armazenar todos os tabuleiros que forem adicionados

    def _posicao_rei(self, tabuleiro, black=False):
        """ Um método de classe usado para descobrir a posição que está o rei

        :tabuleiro: O tabuleiro que irá ser analisado
        :type tabuleiro: list
        :black: Quando o parametro é passado para True irá buscar a posição do rei das pretas, do contrário busca a
        posição do rei das brancas
        :type black: bool
        """
        rei = 'k' if black else 'K'  # tipo do rei para ser encontrado

        for indice, peca in enumerate(tabuleiro):

            if peca.find(rei) != -1:
                # gera um atributo de classe contendo a linha e a coluna em que o rei indicado está
                self.posicao_rei = (indice, peca.find(rei))

    def _ataque_cavalo(self, tabuleiro,black=False):
        """ Um método de classe que com base na posição relativa do rei irá buscar se tem algum cavalo atacando a casa
        Como os cavalos "pulam" por outras peças, só é buscado se em alguma possível casa de ataque de cavalo há algum

        :param tabuleiro: O tabuleiro que está sendo analisado
        :type tabuleiro: list
        :param black: Quando o parametro é passado para True, irá visualizar se o rei preto está sendo atacado, do
        contrário irá visualizar se o rei branco está sendo atacado
        :type black: bool

        """
        knight = "N" if black else "n"
        xref, yref = self.posicao_rei

        # possiveis movimentos de onde um cavalo pode estar para dar cheque no rei
        posicoes = [(-2, -1), (-2, 1), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2)]

        for x, y in posicoes:
            x_peca = xref + x if xref + x > 0 else 8
            y_peca = yref + y if yref + y > 0 else 8

            try:
                if tabuleiro[x_peca][y_peca] == knight:
                    return True

                return False

            except IndexError:
                pass

    def _ataque_peao(self, tabuleiro, black=False):
        """ Um método de classe que com base na posição relativa do rei irá ver a casa está sendo atacada por um peao

        :param tabuleiro: O tabuleiro que está sendo analisado
        :type tabuleiro: list
        :param black: Quando o parametro é passado para True, irá visualizar se o rei preto está sendo atacado, do
        contrário irá visualizar se o rei branco está sendo atacado
        :type black: bool

        """

        pawn = 'P' if black else 'p'  # irá ver o tipo de peao baseado no parametro black
        xrel = -1 if black else 1  # irá alterar a linha a ser analisada baseado no parametro black

        xref, yref = self.posicao_rei  # linha e coluna onde o rei está
        x_peca = xref - xrel if xref - xrel > 0 else 8  # irá forçar um erro caso a linha seja menor que 0
        y_peca = yref - 1 if yref - 1 > 0 else 8  # irá forçar um erro caso a coluna seja menor que 0

        try:
            if tabuleiro[x_peca][yref + 1] == pawn or tabuleiro[x_peca][y_peca] == pawn:
                return True

            return False

        except IndexError:
            pass

    def _ataque_torre(self, tabuleiro, black=False):
        """Um metodo de classe para verificar se o rei está sendo atacado por uma torre ou rainha

        Caso em volta do rei não haja nenhuma peça que possa bloquear o ataque da torre, o código irá buscar na mesma
        linha e coluna onde o rei está até encontrar uma torre/rainha, retornando que o rei está em cheque
        ou alguma outra peça que bloqueara o ataque, retornando que o rei não está em cheque

        :param tabuleiro: O tabuleiro que está sendo analisado
        :type tabuleiro: list
        :param black: Quando o parametro é passado para True, irá visualizar se o rei preto está sendo atacado, do
        contrário irá visualizar se o rei branco está sendo atacado
        :type black: bool
        """

        xref, yref = self.posicao_rei  # linha e coluna onde o rei está

        posicoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # possiveis posição em que a torre/rainha podem estar
        nar = 'BPNKbpnkrq' if black else 'BPNKRQbpnk'  # peças que não atacam no mesmo padrão da torre e da rainha
        ar = 'RQ' if black else 'rq'  # peças que possivelmente podem estar atacando o rei

        return self._padrao_ataque(posicoes, tabuleiro, ar, nar, xref, yref)

    def _ataque_bispo(self, tabuleiro, black=False):
        """Um metodo de classe para verificar se o rei está sendo atacado por um bispo ou rainha

           Caso em volta do rei não haja nenhuma peça que possa bloquear o ataque do bispo ou rainha,
           o código irá buscar nas diagonais da onde o rei está até encontrar um bispo/rainha,
           retornando que o rei está em cheque (True), ou alguma outra peça que bloqueara o ataque,
           retornando que o rei não está em cheque (False)

           :param tabuleiro: O tabuleiro que está sendo analisado
           :type tabuleiro: list
           :param black: Quando o parametro é passado para True, irá visualizar se o rei preto está sendo atacado, do
           contrário irá visualizar se o rei branco está sendo atacado
           :type black: bool
            """
        xref, yref = self.posicao_rei  # linha e coluna do rei
        nad = 'RPNKrpnkqb' if black else 'RPNKrpnkQB'  # peças que não atacam na diagonal, o peão está incluso pois o
        # seu ataque é analisado antes do bispo/rainha
        ad = 'QB' if black else 'qb'  # peças que atacam na diagonal

        posicoes = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # possiveis movimento do bispo

        return self._padrao_ataque(posicoes, tabuleiro, ad, nad, xref, yref)

    def _padrao_ataque(self, posicoes, tabuleiro, pa, pna, xref, yref):
        """ Um método de classe responsavel por iterar sobre as linhas e colunas visualizando se o rei está em cheque


        :param posicoes: possiveis posicao em que o atacante pode estar
        :type posicoes: list
        :param tabuleiro: tabuleiro analisado
        :type tabuleiro: list
        :param pa: peças podem atacar o rei naquela direcao
        :type pa: str
        :param pna: peças que não pdoem atacar o rei naquela direcao
        :type pna: str
        :param xref: linha em que está o rei
        :type xref: int
        :param yref: coluna em que está o rei
        :type yref: int
        """

        for x, y in posicoes:  # irá iterar sobre a lista de posicoes, pegando o x e o y

            # soma a linha que está com o rei com a posicao em que pode estar um ataque, força um erro caso seja < 0
            x_peca = xref + x if xref + x > 0 else 8

            # soma a coluna do rei com a posicao em que pode estar um ataque, força um erro caso seja < 0
            y_peca = yref + y if yref + y > 0 else 8

            # o acrescimo que cada linha deve ter
            xmais = x

            # o acrescimo que cada coluna deve ter
            ymais = y

            # irá tentar iterar sobre o tabuleiro
            try:

                # Verifica se em volta do rei há alguma peça que já o ataque
                if tabuleiro[x_peca][y_peca] != '.' and tabuleiro[x_peca][y_peca] not in pna:
                    return True

                # Verifica se em volta do rei não há nenhuma peça que o possoa proteger
                if tabuleiro[x_peca][y_peca] == '.':

                    # busca nas posicoes passadas, até o fim do tabuleiro, se há alguma peça que possa atacar o rei
                    while 0 <= x_peca < 8 and 0 <= y_peca < 8:

                        # Verifica se há alguma peça que possa bloquear o ataque
                        if tabuleiro[x_peca][y_peca] in pna:
                            return False

                        # Verifica se há alguma peça que possa atacar o rei
                        if tabuleiro[x_peca][y_peca] in pa:
                            return True

                        x_peca += xmais  # irá voltar/avançar sobre as linhas
                        y_peca += ymais  # irá voltar/avançar sobre as colunas

            # caso o indice não esteja na lista do tabuleiro essa tentativa só é ignorada
            except IndexError:
                pass

    def adicionar_tabuleiro(self):
        """Um método de classe que serve para pegar o tabuleiro do teclado

        Irá pedir para o usuario inserir as linhas do tabuleiro, caso o tamanho das linhas sejam diferente de
        8 caracteres irá gerar um erro e avisar ao usuario. Caso o tabuleiro passado seja vazio, o laço é quebrado

        """

        tabuleiro = []  # irá ordenar o tabuleiro
        tabuleiro_vazio = [''.join('.' for x in range(8)) for k in range(8)]  # gera um tabuleiro vazio
        for i in range(self.qntd_execucao):  # pega quantas vezes o código é executado

            for j in range(8):  # irá pegar as linhas do tabuleiro do usuario
                linha = input()

                if len(linha) != 8:
                    # levanta um erro caso a linha não tenha 8 caracteres
                    raise AttributeError("Cada linha do tabuleiro deve ter 8 caracteres")

                # adiciona a linha ao tabuleiro
                tabuleiro.append(linha)

            # verifica se o tabuleiro formado é igual ao tabuleiro vazio, caso for quebra o loop
            if tabuleiro == tabuleiro_vazio:
                break

            input()  # um input para pegar um "enter" do usuario

            # adiciona o tabuleiro ao atributo de classe self.tabuleiros
            self.tabuleiros.append(tabuleiro)

    def checar_reis(self):
        """Irá verificar se algum dos reis está em cheque

        Primeiro irá verificar se o rei preto está em cheque, depois analisa se o rei branco está em cheque, se nenhum
        estiver em cheque irá imprimir que nenhum deles está em cheque
        """

        # irá pegar os jogos que estão no atributo self.tabuleiros
        for i, tabuleiro in enumerate(self.tabuleiros, 1):

            self._posicao_rei(tabuleiro, black=True)  # define o rei preto como referencial

            # chama cada uma das funções de ataque para verificar se alguma delas retorna True
            if self._ataque_peao(tabuleiro, black=True) or self._ataque_cavalo(tabuleiro, black=True) or self._ataque_torre(tabuleiro, black=True) or self._ataque_bispo(tabuleiro, black=True):
                print(f"Jogo #{i}: rei preto está em cheque.")
                continue

            self._posicao_rei(tabuleiro)  # define o rei branco como referencial

            # chama cada uma das funções de ataque para verificar se alguma delas retorna True
            if self._ataque_peao(tabuleiro) or self._ataque_cavalo(tabuleiro) or self._ataque_torre(tabuleiro) or self._ataque_bispo(tabuleiro):
                print(f"Jogo #{i}: rei branco está em cheque.")
                continue

            # Caso nenhuma das condições acima seja satisfeita, significa que nenhum rei está em cheque
            print(f"Jogo #{i}: nenhum rei está em cheque.")


# exemplo de uso
if __name__ == '__main__':
    t1 = Tabuleiro(3)
    # t1.adicionar_tabuleiro()

    # Estou passando os tabuleiros diretamente, porém caso se queira passar manualmente basta descomentar a linha
    # anterior e comentar a linha a seguir
    t1.tabuleiros = [['rnbqk.nr', 'ppp..ppp', '....p...', '...p....', '.bPP....', '.....N..', 'PP..PPPP', 'RNBQKB.R'],
                     ['..k.....', 'ppp.pppp', '........', '.R...B..', '........', '........', 'pppppppp', 'K.......'],
                     ['..k.....', 'ppp.pppp', '........', '........', '........', '........', 'PPPPPPPP', 'K.......'],
                     ]
    t1.checar_reis()

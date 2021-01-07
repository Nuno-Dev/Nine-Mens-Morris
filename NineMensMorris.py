#-----------------------------------------------------------------------------------------------#
#--------------------------------------| 99292 Nuno Martins |-----------------------------------#
#-----------------------------------------------------------------------------------------------#

#-#############################################################################################-#
#                                           TAD POSICAO                                         #
#-#############################################################################################-#

# Construtor:

def cria_posicao(c,l):
    #cria_posicao: str x str -> posicao
    """
    cria_posicao(c,l) recebe duas cadeias de carateres correspondentes a coluna c e a 
    linha l de uma posicao e devolve a posicao correspondente. Se os argumentos forem 
    invalidos, gera ValueError.
    """
    if type(c)==str and type(l)==str:
        if c in ['a','b','c'] and l in ['1','2','3']:
            return c+l
    raise ValueError('cria_posicao: argumentos invalidos')

def cria_copia_posicao(p):
    #cria_copia_posicao: posicao -> posicao
    """
    cria_copia_posicao(p) recebe uma posicao e devolve uma copia nova da posicao.
    """
    if eh_posicao(p):
        return p
    else:
        raise ValueError('cria_copia_posicao: argumentos invalidos')

#-----------------------------------------------------------------------------------------------#

# Seletores:

def obter_pos_c(p):
    #obter_pos_c: posicao -> str
    """
    obter_pos_c(p) devolve a componente coluna c da posicao p.
    """    
    return p[0]


def obter_pos_l(p):
    #obter_pos_l: posicao -> str
    """
    obter_pos_l(p) devolve a componente linha l da posicao p.
    """  
    return p[1]

#-----------------------------------------------------------------------------------------------#

# Reconhecedor:

def eh_posicao(arg):
    #eh_posicao: universal -> booleano
    """
    eh_posicao(arg) devolve True caso o seu argumento seja um TAD posicao e 
    False caso contrario.
    """    
    if type(arg)==str:
        if obter_pos_c(arg) in ['a','b','c'] and obter_pos_l(arg) in ['1','2','3']:
            return True
    return False

#-----------------------------------------------------------------------------------------------#

# Teste:

def posicoes_iguais(p1, p2):
    #posicoes_iguais: posicao x posicao -> booleano
    """
    posicoes_iguais(p1, p2) devolve True apenas se p1 e p2 sao posicoes e sao iguais.
    """    
    return eh_posicao(p1) and eh_posicao(p2) and p1==p2

#-----------------------------------------------------------------------------------------------#

# Transformador:

def posicao_para_str(p):
    #posicao_para_str: posicao -> str
    """
    posicao_para_str(p) devolve a cadeia de caracteres 'cl' que representa o
    seu argumento, sendo os valores c e l as componentes coluna e linha de p.
    """    
    return obter_pos_c(p)+obter_pos_l(p)

#-----------------------------------------------------------------------------------------------#

# Funcao de alto nivel:

def obter_posicoes_adjacentes(p):
    #obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    """
    obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes 
    a posicao p de acordo com a ordem de leitura do tabuleiro.
    """    
    c = obter_pos_c(p)
    l = obter_pos_l(p)
    if l=='1':
        if c=='a':
            return ('b1','a2','b2')
        elif c=='b':
            return ('a1','c1','b2')
        elif c=='c':
            return ('b1','b2','c2')
    elif l=='2':
        if c=='a':
            return ('a1','b2','a3')
        elif c=='b':
            return ('a1','b1','c1','a2','c2','a3','b3','c3')
        elif c=='c':
            return ('c1','b2','c3')
    elif l=='3':
        if c=='a':
            return ('a2','b2','b3')
        elif c=='b':
            return ('b2','a3','c3')
        elif c=='c':
            return ('b2','c2','b3')

#-#############################################################################################-#
#                                           TAD PECA                                            #
#-#############################################################################################-#

# Construtor:
    
def cria_peca(s):
    #cria_peca: str -> peca
    """
    cria_peca(s) recebe uma cadeia de carateres correspondente ao identificador de um 
    dos dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve a peca 
    correspondente. Se os argumentos forem invalidos, gera ValueError.
    """    
    if eh_peca(s):
        return s
    else:
        raise ValueError('cria_peca: argumento invalido')
    

def cria_copia_peca(j):
    #cria_copia_peca: peca -> peca
    """
    cria_copia_peca(j) recebe uma peca e devolve uma copia nova da peca.
    """    
    if eh_peca(j):
        return j
    else:
        raise ValueError('cria_copia_peca: argumento invalido')

#-----------------------------------------------------------------------------------------------#

# Reconhecedor:

def eh_peca(arg):
    #eh_peca: universal -> booleano
    """
    eh_peca(arg) devolve True caso o seu argumento seja um TAD peca e False caso contrario.
    """    
    if type(arg)==str:
        if len(arg)==1:
            if arg=='X' or arg=='O' or arg.isspace():
                return True
    return False

#-----------------------------------------------------------------------------------------------#

# Teste:

def pecas_iguais(j1,j2):
    #pecas_iguais: peca x peca -> booleano
    """
    pecas_iguais(j1, j2) devolve True apenas se p1 e p2 sao pecas e sao iguais.
    """    
    return j1==j2

#-----------------------------------------------------------------------------------------------#

# Transformador:

def peca_para_str(j):
    #peca_para_str: peca -> str
    """
    peca_para_str(j) devolve a cadeia de caracteres que representa o jogador dono 
    da peca, isto e, '[X]', '[O]' ou '[ ]'.
    """    
    return '[{}]'.format(j)

#-----------------------------------------------------------------------------------------------#

# Funcoes de alto nivel:

def peca_para_inteiro(j):
    #peca_para_inteiro: peca -> N
    """
    peca_para_inteiro(j) devolve um numero inteiro  1, -1 ou 0, dependendo se a 
    peca e do jogador 'X', 'O' ou livre, respetivamente.
    """    
    if j=='X':
        return 1
    elif j=='O':
        return -1
    elif j==' ':
        return 0

#-#############################################################################################-#
#                                           TAD TABULEIRO                                       #
#-#############################################################################################-#

# Construtor:

def cria_tabuleiro():
    #cria_tabuleiro: {} -> tabuleiro
    """
    cria_tabuleiro() devolve um tabuleiro de jogo do moinho de 3x3 com posicoes todas vazias.
    """    
    return {'a1':' ', 'b1':' ', 'c1':' ', 'a2':' ', 'b2':' ', 'c2':' ', \
            'a3':' ', 'b3':' ', 'c3':' '}

def cria_copia_tabuleiro(t):
    #cria_copia_tabuleiro: tabuleiro -> tabuleiro
    """
    cria_copia_tabuleiro(t) recebe um tabuleiro e devolve uma copia nova do tabuleiro.
    """    
    if eh_tabuleiro(t):
        tab_copia = t.copy()
        return tab_copia
    else:
        raise ValueError('cria_copia_tabuleiro: argumento invalido')

#-----------------------------------------------------------------------------------------------#

# Seletores:

def obter_peca(t,p):
    #obter_peca: tabuleiro x posicao -> peca
    """
    obter_peca(t, p) devolve a peca na posicao p do tabuleiro. Devolve uma peca 
    livre se a posicao nao estiver ocupada.
    """    
    return t[p]

def obter_vetor(t,s):
    #obter_vetor: tabuleiro x str -> tuplo de pecas
    """
    obter_vetor(t, s) devolve todas as pecas da linha ou coluna especicada pelo seu 
    argumento.
    """    
    if s=='a':
        return (t['a1'],t['a2'],t['a3'])
    elif s=='b':
        return (t['b1'],t['b2'],t['b3'])
    elif s=='c':
        return (t['c1'],t['c2'],t['c3'])
    elif s=='1':
        return (t['a1'],t['b1'],t['c1'])
    elif s=='2':
        return (t['a2'],t['b2'],t['c2'])
    elif s=='3':
        return (t['a3'],t['b3'],t['c3'])        

#-----------------------------------------------------------------------------------------------#

# Modificadores:

def coloca_peca(t,j,p):
    #coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    """
    coloca_peca(t, j, p) modifica destrutivamente o tabuleiro t colocando a peca 
    j na posicao p e devolve o proprio tabuleiro.
    """    
    t[p]=j
    return t

def remove_peca(t,p):
    #remove_peca: tabuleiro x posicao -> tabuleiro
    """
    remove_peca(t, p) modifica destrutivamente o tabuleiro t removendo a peca 
    da posicao p e devolve o proprio tabuleiro.
    """    
    t[p]=' '
    return t

def move_peca(t,p1,p2):
    #move_peca: tabuleiro x posicao x posicao -> tabuleiro
    """
    move_peca(t, p1, p2) modifica destrutivamente o tabuleiro t movendo a peca 
    que se encontra na posicao p1 para a posicao p2 e devolve o proprio tabuleiro.
    """    
    coloca_peca(t,t[p1],p2)
    remove_peca(t,p1)
    return t

#-----------------------------------------------------------------------------------------------#

# Reconhecedor

def eh_tabuleiro(arg): 
    #eh_tabuleiro: universal -> booleano
    """
    eh_tabuleiro(arg) devolve True caso o seu argumento seja um TAD tabuleiro e False 
    caso contrario. Um tabuleiro valido pode ter um maximo de 3 pecas de 
    cada jogador, nao pode conter mais de 1 peca mais de um jogador que do contrario e 
    apenas pode haver um ganhador em simultaneo.
    """    
    if type(arg)==dict:
        if len(arg)==9:
            keys = list(arg.keys())
            values = list(arg.values())
            for i in range(9):
                if keys[i] not in ['a1','a2','a3','b1','b2','b3','c1','c2','c3'] \
                   or values[i] not in ['X','O',' ']:
                    return False
            numX = values.count('X')
            numO = values.count('O')
            if numX>3 or numO>3 or abs(numX-numO)>1 or dois_ganhadores(arg)>1:
                return False
            return True
    return False

# Funcao auxiliar de eh_tabuleiro para verificar quantos ganhadores ha

def dois_ganhadores(t):
    #dois_ganhadores: tabuleiro -> N
    """
    dois_ganhadores(t) e uma funcao auxiliar da funcao eh_tabuleiro e ela recebe um 
    tabuleiro e devolve o numero de ganhadores nesse tabuleiro. Vai ser usada
    para verificar a condicao de so haver 1 ganhador em simultaneo na funcao eh_tabuleiro.
    """    
    res = []
    lines = [obter_vetor(t,'1'),obter_vetor(t,'2'),obter_vetor(t,'3'), \
             obter_vetor(t,'a'),obter_vetor(t,'b'),obter_vetor(t,'c')]
    for el in lines:
        if el.count('X')==3:
            if 'X' not in res:
                res+=['X']
        elif el.count('O')==3:
            if 'O' not in res:
                res+=['O']
    return len(res)

def eh_posicao_livre(t,p):
    #eh_posicao_livre: tabuleiro x posicao -> booleano
    """
    eh_posicao_livre(t, p) devolve True se a posicao p do tabuleiro 
    for uma posicao livre.
    """    
    return t[p]==' ' 

#-----------------------------------------------------------------------------------------------#

# Teste

def tabuleiros_iguais(t1,t2):
    #tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    """
    tabuleiros_iguais(t1, t2) devolve True se t1 e t2 sao tabuleiros e sao iguais.
    """    
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1==t2

#-----------------------------------------------------------------------------------------------#

# Transformador:

def tabuleiro_para_str(t):
    #tabuleiro_para_str: tabuleiro -> str
    """
    tabuleiro_para_str(t) devolve a cadeia de caracteres que representa o tabuleiro.
    """    
    l1 = '[{}]-[{}]-[{}]'.format(t['a1'],t['b1'],t['c1'])
    l2 = '[{}]-[{}]-[{}]'.format(t['a2'],t['b2'],t['c2'])
    l3 = '[{}]-[{}]-[{}]'.format(t['a3'],t['b3'],t['c3'])
    return ('   a   b   c\n1 {}\n   | \\ | / |\n2 {}\n' \
           '   | / | \\ |\n3 {}'.format(l1,l2,l3))

def tuplo_para_tabuleiro(t):
    #tuplo_para_tabuleiro: tuplo -> tabuleiro
    """
    tuplo_para_tabuleiro(t) devolve o tabuleiro que e representado pelo tuplo t
    com 3 tuplos, cada um deles contendo 3 valores inteiros iguais a 1, -1 ou 0.
    """    
    res = dict()
    values = []
    for el in t:
        for value in el:
            if type(value)==int:
                if value==1:
                    values+=['X']
                elif value==-1:
                    values+=['O']
                elif value==0:
                    values+=[' ']
    keys = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
    for i in range(9):
        res[keys[i]]=values[i]
    return res    

#-----------------------------------------------------------------------------------------------#

# Funcoes de alto nivel:

def obter_ganhador(t):
    #obter_ganhador: tabuleiro -> peca
    """
    obter ganhador(t) devolve uma peca do jogador que tenha as suas 3 pecas em linha
    na vertical ou na horizontal no tabuleiro. Se nao existir nenhum ganhador, devolve
    uma peca livre.
    """    
    lines = [obter_vetor(t,'1'),obter_vetor(t,'2'),obter_vetor(t,'3'), \
             obter_vetor(t,'a'),obter_vetor(t,'b'),obter_vetor(t,'c')]
    for el in lines:
        if el.count('X')==3:
            return 'X'
        elif el.count('O')==3:
            return 'O'
    return ' '

def obter_posicoes_livres(t):
    #obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    """
    obter_posicoes_livres(t) devolve um tuplo com as posicoes nao ocupadas pelas 
    pecas de qualquer um dos dois jogadores na ordem de leitura do tabuleiro.
    """    
    res = tuple()
    pos_lst = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
    for pos in pos_lst:
        if t[pos]==' ':
            res+=(pos,)
    return res

def obter_posicoes_jogador(t,j):
    #obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    """
    obter posicoes jogador(t, j) devolve um tuplo com as posicoes ocupadas pelas 
    pecas j de um dos dois jogadores na ordem de leitura do tabuleiro.
    """    

    pos_lst = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
    return tuple([pos for pos in pos_lst if t[pos]==' '])

#-#############################################################################################-#
#                                         FUNCOES ADICIONAIS                                    #
#-#############################################################################################-#

def obter_movimento_manual(t,j):
    #obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    """
    obter_movimento_manual(t, j) e uma funcao auxiliar que recebe um tabuleiro
    e uma peca de um jogador e devolve um tuplo com uma ou duas posicoes (dependendo
    se estamos na fase de colocacao ou na fase de movimento) que representam uma
    posicao ou um movimento introduzido manualmente pelo jogador, respetivamente.
    """    
    #Fase de colocacao
    if len(obter_posicoes_livres(t))>3:
        pos = input('Turno do jogador. Escolha uma posicao: ')
        #if len(pos)==2:
        if eh_posicao(pos):
            if eh_posicao_livre(t,pos):
                return (pos,)
        raise ValueError('obter_movimento_manual: escolha invalida')
    #Fase de movimentacao
    else:
        pos = input('Turno do jogador. Escolha um movimento: ')
        if len(pos)==4:
            p1 = pos[0]+pos[1]
            p2 = pos[2]+pos[3]
            if eh_posicao(p1) and eh_posicao(p2):
                pos_jog = obter_posicoes_jogador(t,j)
                pos_adj = obter_posicoes_adjacentes(p1)
                pos_livres = [eh_posicao_livre(t,pos) for pos in pos_adj].count(True)
                if (p1 in pos_jog) and eh_posicao_livre(t,p2) and (p2 in pos_adj):
                    return (p1,p2)
                elif (p1 in pos_jog) and posicoes_iguais(p1,p2) and (pos_livres==0):
                    return (p1,p2)
                else:
                    raise ValueError('obter_movimento_manual: escolha invalida')
    raise ValueError('obter_movimento_manual: escolha invalida')
    
#-----------------------------------------------------------------------------------------------#

def vitoria(t,j):
    #vitoria: tabuleiro x peca -> tuplo de posicoes
    """
    vitoria(t, j) e uma funcao auxiliar da funcao obter_movimento_auto,
    recebe um tabuleiro e uma peca de um jogador. No caso do jogador
    ter duas das suas pecas em linha e uma posicao livre entao devolve
    um tuplo com essa posicao (ganhando o jogo).
    """    
    pos_livres = obter_posicoes_livres(t)
    for pos in pos_livres:
        t1 = cria_copia_tabuleiro(t)
        t1 = coloca_peca(t1,j,pos)
        if obter_ganhador(t1)==j:
            return (pos,)

def bloqueio(t,j):
    #bloqueio: tabuleiro x peca -> tuplo de posicoes
    """
    bloqueio(t, j) e uma funcao auxiliar da funcao obter_movimento_auto,
    recebe um tabuleiro e uma peca de um jogador. No caso do adversario
    ter duas das suas pecas em linha e uma posicao livre entao devolve
    um tuplo com essa posicao (para bloquear o adversario).
    """    
    if j=='X':
        outro_j='O'
    else:
        outro_j='X'
    return vitoria(t,outro_j)

def centro(t):
    #centro: tabuleiro -> tuplo de posicoes
    """
    centro(t) e uma funcao auxiliar da funcao obter_movimento_auto,
    recebe um tabuleiro. No caso da posicao central estar livre entao
    devolve um tuplo com essa posicao.
    """    
    if eh_posicao_livre(t,'b2'):
        return ('b2',)

def canto_vazio(t):
    #canto_vazio: tabuleiro -> tuplo de posicoes
    """
    canto_vazio(t) e uma funcao auxiliar da funcao obter_movimento_auto,
    recebe um tabuleiro. No caso de um canto estar livre entao devolve 
    um tuplo com essa posicao.
    """      
    cantos = ['a1','c1','a3','c3']
    for canto in cantos:
        if eh_posicao_livre(t, canto):
            return (canto,)

def lateral_vazio(t):
    #lateral_vazio: tabuleiro -> tuplo de posicoes
    """
    lateral_vazio(t) e uma funcao auxiliar da funcao obter_movimento_auto,
    recebe um tabuleiro. No caso de uma posicao lateral (que nem e o centro,
    nem um canto) estar livre entao devolve um tuplo com essa posicao.
    """      
    laterais = ['b1','a2','c2','b3']
    for lateral in laterais:
        if eh_posicao_livre(t, lateral):
            return (lateral,)

#-----------------------------------------------------------------------------------------------#
 
def facil(t,j):
    #facil: tabuleiro x peca -> tuplo de posicoes
    """
    facil(t, j) e uma funcao auxiliar da funcao obter_movimento_auto, recebe
    um tabuleiro e uma peca de um jogador. Devolve um tuplo em que o primeiro
    elemento corresponde a primeira posicao de entre todas as posicoes ocupadas 
    pelas pecas do jogador que tenha uma posicao adjacente livre e o segundo
    elemento corresponde a essa posicao adjacente livre.
    """    
    pos_jog = obter_posicoes_jogador(t,j)
    for pos in pos_jog:
        pos_adj = obter_posicoes_adjacentes(pos)
        for el in pos_adj:
            if (eh_posicao_livre(t,el)):
                return (pos,el)
    return (pos_jog[0],pos_jog[0])
         
def minimax(t,j,sq,prf):
    if obter_ganhador(t) in ['X', 'O'] or prf==0:
        if obter_ganhador(t)=='O':
            return (-1,sq)
        elif obter_ganhador(t)=='X':
            return (1,sq)
        return (0, sq)
    else:
        best_sq = []
        if j=='O':
            best_res=1
        elif j=='X':
            best_res=-1
        for pos in obter_posicoes_jogador(t,j):
            for pos_adj in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(t,pos_adj):
                    copia_tab = cria_copia_tabuleiro(t)
                    copia_tab = move_peca(copia_tab,pos,pos_adj)
                    if j=='O':
                        other_player='X'
                    elif j=='X':
                        other_player='O'
                    
                    result = minimax(copia_tab,other_player,prf-1,sq+[pos+pos_adj])
                    new_res = result[0]
                    new_sq = result[1]

                    if (new_res < best_res and j=='O') or ('best_sq' not in list(vars()))\
                       or (new_res > best_res and j=='X'):
                        best_res = new_res
                        best_sq = new_sq
        return (best_res, new_sq)

def minimax_convert(t):
    return (t[1][0][0:2],t[1][0][2:])

#-----------------------------------------------------------------------------------------------#

def obter_movimento_auto(t,j,dif):
    #obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
    """
    obter_movimento_auto(t,j,dif) e uma funcao auxiliar que recebe um tabuleiro,
    uma peca de um jogador e uma cadeia de carateres representando o nivel de 
    dificuldade do jogo e devolve um tuplo com uma ou duas posicoes que representam
    uma posicao ou um movimento escolhido automaticamente (dependendo se estamos
    na fase de colocao ou fase de movimento).
    """    
    #Fase de colocacao
    if len(obter_posicoes_livres(t))>3:  
        for i in range(5):
            if i==0: res = vitoria(t,j)
            if i==1: res = bloqueio(t,j)
            if i==2: res = centro(t)
            if i==3: res = canto_vazio(t)
            if i==4: res = lateral_vazio(t)
            
            if res!=None:
                return res
    #Fase de movimentacao
    else:
        if dif=='facil':
            return facil(t,j)
        elif dif=='normal':
            res = minimax(t,j,1,[])
            if res!=None:
                return minimax_convert(res)
            return facil(t,j)
        else:
            res = minimax(t,j,5,[])
            return minimax_convert(res)

#-----------------------------------------------------------------------------------------------#

def moinho_colocacao(t,j,pc,dif):
    #moinho_colocacao: tabuleiro x peca x peca x str -> {}
    """
    moinho_colocacao(t, j, pc, dif) e uma funcao auxiliar da funcao moinho e que
    realiza 6 rondas de colocacao (3 para o jogador e 3 para o computador), e
    a ordem de colocacao depende de qual a peca do jogador (se 'X' entao jogador 
    comeca primeiro, se 'O' entao computador comeca primeiro).
    """    
    game_round = 0
    def turno_jog(t,j,pc,dif):
    #turno_jog: tabuleiro x peca x peca x str -> {}
       
        jogada_j = obter_movimento_manual(t,j)[0]
        t = coloca_peca(t,j,jogada_j)
        print(tabuleiro_para_str(t)) 
        
    def turno_pc(t,j,pc,dif):
    #turno_pc: tabuleiro x peca x peca x str -> {}
       
        print('Turno do computador ({}):'.format(dif))
        jogada_pc = obter_movimento_auto(t,pc,dif)[0]
        t = coloca_peca(t,pc,jogada_pc)
        print(tabuleiro_para_str(t))
        
    while(game_round<3):
        if j=='O':
            turno_pc(t,j,pc,dif)
            turno_jog(t,j,pc,dif)
        else:
            turno_jog(t,j,pc,dif) 
            turno_pc(t,j,pc,dif)           
        game_round+=1    

def moinho_movimento(t,j,pc,dif):
    #moinho_movimento: tabuleiro x peca x peca x str -> {}
    """
    moinho_movimento(t, j, pc, dif) e uma funcao auxiliar da funcao moinho e que
    realiza 6 rondas de movimento (3 para o jogador e 3 para o computador), e
    a ordem de colocacao depende de qual a peca do jogador (se 'X' entao jogador 
    realiza o seu movimento primeiro, se 'O' entao o primeiro movimento sera
    realizado pelo computador).
    """      
    
    def turno_jog(t,j,pc,dif):
    #turno_jog: tabuleiro x peca x peca x str -> {} 
        """

        """       
        antes_j, depois_j = obter_movimento_manual(t,j)
        if not posicoes_iguais(antes_j, depois_j):
            t = move_peca(t,antes_j,depois_j)
        print(tabuleiro_para_str(t))        
        
    def turno_pc(t,j,pc,dif):
    #turno_pc: tabuleiro x peca x peca x str -> {}
        """

        """
        print('Turno do computador ({}):'.format(dif))
        antes_pc, depois_pc = obter_movimento_auto(t,pc,dif)
        t = move_peca(t,antes_pc,depois_pc)
        print(tabuleiro_para_str(t))         
    
    while(obter_ganhador(t)==' '):
        if j=='O':
            turno_pc(t,j,pc,dif)
            if obter_ganhador(t)!=' ':
                break            
            turno_jog(t,j,pc,dif)
        else:
            turno_jog(t,j,pc,dif) 
            if obter_ganhador(t)!=' ':
                break            
            turno_pc(t,j,pc,dif)                           

#-----------------------------------------------------------------------------------------------#

def moinho(j,dif):
    #moinho: str x str -> str
    """
    moinho(j, dif) e a funcao principal que permite jogar um jogo completo
    do jogo do moinho de um jogador contra o computador. A funcao recebe
    duas cadeias de carateres e devolve a representacao externa da peca
    ganhadora ('[X]' ou '[O]').
    """    
    if j in ['[X]','[O]'] and dif in ['facil','normal','dificil']:
        if j=='[X]':
            j,pc='X','O'
        else:
            pc,j='X','O'
        t = cria_tabuleiro()
        print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.'.format(dif))
        print(tabuleiro_para_str(t))
        moinho_colocacao(t,j,pc,dif)
        moinho_movimento(t,j,pc,dif)
        return '[{}]'.format(obter_ganhador(t))
    else:
        raise ValueError('moinho: argumentos invalidos')
    
#-----------------------------------------------------------------------------------------------#

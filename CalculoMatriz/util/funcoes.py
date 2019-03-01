import pygraphviz
import networkx as nx
from PIL import Image
'''
    Funcao usada para obter a media MICRO do TPR,
    uma vez que o pycm nao da essa informacao
'''

def montaGrafo(grupo):

    indices = {}
    subindices = {}
    counter = 0
    subcounter = 0
    for membro in grupo:
        indices[membro] = counter
        counter += 1
        for submembro in grupo[membro]:
            subindices[submembro] = subcounter
            subcounter += 1

    cores = None

    grafoDeCoAutoriaSemPesos = None
    grafoDeCoAutoriaSemPesosCMAPX = None
    grafoDeCoAutoriaComPesos = None
    grafoDeCoAutoriaComPesosCMAPX = None
    grafoDeCoAutoriaNormalizado = None
    grafoDeCoAutoriaNormalizadoCMAPX = None
    diretorioDeSaida = '../saida'

    # atribuicao de cores nos vertices
    corDoNoFG = '#FFFFFF'
    corDoNoBG = '#0A6EA4'

    grafoDeCoAutoriaSemPesos = criarGrafoDeCoAutoriaSemPesos(grupo,indices,subindices)
    grafoDeCoAutoriaSemPesos.draw(path=diretorioDeSaida + '/grafoDeColaboracoesSemPesos.png', format='png')
    grafoDeCoAutoriaSemPesos.draw(path=diretorioDeSaida + '/grafoDeColaboracoesSemPesos.dot', format='dot')
    grafoDeCoAutoriaSemPesosCMAPX = grafoDeCoAutoriaSemPesos.draw(format='cmapx')

    #grafoDeCoAutoriaComPesos = criarGrafoDeCoAutoriaComPesos(grupo,indices,subindices)
    #grafoDeCoAutoriaComPesos.draw(path=diretorioDeSaida + '/grafoDeColaboracoesComPesos.png', format='png')
    #grafoDeCoAutoriaComPesos.draw(path=diretorioDeSaida + '/grafoDeColaboracoesComPesos.dot', format='dot')
    #grafoDeCoAutoriaComPesosCMAPX = grafoDeCoAutoriaComPesos.draw(format='cmapx')

    # Criamos um thumbnail do grafo sem pesos
    im = Image.open(diretorioDeSaida + '/grafoDeColaboracoesSemPesos.png')
    im.thumbnail((400, 400))
    im.save(diretorioDeSaida + '/grafoDeColaboracoesSemPesos-t.png')

def calculaMediaMicroTPR(cm):
    total = 0;
    classes = cm.class_stat['TPR']
    for classe in classes:
        total += classes[classe]
    return (total/len(classes))

def lerArquivo(nome_arquivo):
    linhas = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.rstrip('\n')
            linhas.append([linha])
    return linhas

def atribuirCorLegal(self, indice):
    cores = [
        ['#FFFFFF', '#000099'],  # azul
        ['#FFFFFF', '#006600'],  # verde
        ['#FFFFFF', '#990000'],  # vermelho
        ['#FFFFFF', '#FF3300'],  # laranja
        ['#FFFFFF', '#009999'],  # esmeralda legal
        ['#000000', '#FF33CC'],  # pink
        ['#FFFFFF', '#333333'],  # cinza
        ['#000000', '#FFFF00'],  # amarelo
        ['#FFFFFF', '#0033FF'],  # azul eletric
        ['#FFFFFF', '#330000'],  # marrom
        ['#FFFFFF', '#330099'],  # roxo
        ['#000000', '#CC9999'],
        ['#000000', '#FF99CC'],
        ['#000000', '#FFCCFF'],
        ['#000000', '#999933'],
        ['#FFFFFF', '#339966'],
        ['#FFFFFF', '#660033'],
        ['#000000', '#00CC99'],
        ['#000000', '#99FFCC'],  # esmeralda
        ['#FFFFFF', '#330033'],  # roxo escuro
        ['#000000', '#FFFFFF']]

    if indice < len(self.cores):
        return cores[indice]
    else:
        return cores[-1]


def abreviarNome(nome):
    # No grafo de colaboracoes nomes cumpridos nao ajudam na visualizacao da co-autoria.
    # para tal, precisamos abreviar os nomes.
    # Ex.
    #     'Jesus Pascual Mena Chalco'         -> 'Jesus P. Mena Chalco'
    #     'Aaaaaa BBBBBB da CCCCCCC e DDDDDD' -> 'Aaaaaa B. da CCCCCCC e DDDDDD'
    partes = nome.split(' ')
    if len(partes) >= 4:
        indice = 2
        if len(partes[-2]) <= 3:
            indice = 3
        nomeAbreviado = partes[0]
        for i in range(1, len(partes) - indice):
            if len(partes[i]) >= 3:
                nomeAbreviado += " " + partes[i][0] + "."
            else:
                nomeAbreviado += " " + partes[i]
        for i in range(len(partes) - indice, len(partes)):
            nomeAbreviado += " " + partes[i]
    else:
        nomeAbreviado = nome
    return nomeAbreviado


def criarGrafoAutoresNetworkX() :
    G = nx.Graph()
    nx.draw(G)

def criarGrafoDeCoAutoriaSemPesos(grupo,indices,subindices):
    print "\n[CRIANDO GRAFOS DE COLABORACOES SEM PESOS]"
    grafo = pygraphviz.AGraph(directed=False, overlap="False", id="grafo1", name="grafo1")
    grafo.node_attr['shape'] = 'rectangle'
    grafo.node_attr['fontsize'] = '12'
    grafo.node_attr['style'] = 'filled'

    for nome in grupo:
        if nome == 'Komogortsev' or nome == 'Kasprowski' or nome == 'Rigas':
            cor = '#B30000'
        else :
            cor = '#0044CC'

        grafo.add_node(n=nome, height='0.3', fontcolor='#FFFFFF', color=cor)

        for submembro in grupo[nome]:
            if nome != submembro:
                if submembro == 'Komogortsev' or submembro == 'Kasprowski' or submembro == 'Rigas':
                    cor = '#B30000'
                else:
                    cor = '#0044CC'

                grafo.add_node(n=submembro, height='0.3', fontcolor='#FFFFFF', color=cor)
                grafo.add_edge(u=nome, v=submembro, key=nome, height='0.3', fontcolor='#FFFFFF', color=cor)

    grafo.layout('dot')  # circo dot neato
    return grafo

def criarGrafoDeCoAutoriaComPesos(grupo,indices,subindices):
    print "\n[CRIANDO GRAFOS DE COLABORACOES COM PESOS]"

    grafo = pygraphviz.AGraph(directed=False, overlap="False", id="grafo2", name="grafo2")
    grafo.node_attr['shape'] = 'rectangle'
    grafo.node_attr['fontsize'] = '12'
    grafo.node_attr['style'] = 'filled'
    nos_adicionados = {}
    # Inserimos os nos
    for nome in grupo:

        if nome not in nos_adicionados:
            nos_adicionados[nome] = 1
            grafo.add_node(indices[nome], label=nome, fontcolor='#000000', color='#FFFFFF', height="0.2")

        for submembro in grupo[nome]:
            if nome not in nos_adicionados:
                nos_adicionados[nome] = 1
                grafo.add_node(subindices[submembro], label=nome, fontcolor='#000000', color='#FFFFFF', height="0.2")

    # Inserimos as arestas
    for nome in grupo:
        for colaborador in grupo[nome]:
            grafo.add_edge(indices[nome], subindices[colaborador])

    grafo.layout('dot')  # circo dot neato
    return grafo
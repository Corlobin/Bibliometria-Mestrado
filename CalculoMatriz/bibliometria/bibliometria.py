from util.funcoes import *

'''filtragem = lerArquivo('../filtro')
nomes_filtragem=[]
for nome in filtragem:
    nome = nome[0].split(',')[0]
    nomes_filtragem.append(nome)
'''

linhas = lerArquivo('../dados_csv_autores')

nomes = {}
for autores in linhas:
    autores_splitted = autores[0].split(',')
    raiz = '';
    for autor in autores_splitted:
        autor = autor.replace('.', '')
        autor = autor.replace(',', '')
        splitted = autor.split(' ')
        if ( splitted[0] == ''):
            nome_inicial = splitted[1]
        else:
            nome_inicial = splitted[0]
        # Raiz da bibliometria
        if raiz == '':
            raiz = nome_inicial

        if raiz not in nomes:
            nomes[raiz] = []
        else:
            ## Retirando esse IF tera nomes repetidos na lista
            if nome_inicial not in nomes[raiz]:
                nomes[raiz] += [nome_inicial]

#for nome in nomes:
#    print(' Nome : \t%s  \tParceiros: %s' %(nome, nomes[nome]))


montaGrafo(grupo=nomes)
criarGrafoAutoresNetworkX()




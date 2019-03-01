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

for nome in nomes:
    print(' Nome : \t%s  \tParceiros: %s' %(nome, nomes[nome]))


montaGrafo(grupo=nomes)

#criarGrafoAutoresNetworkX(grupo=nomes)

print(' --- Trabalhando com a analise das instituicoes \r\n')
linhas = lerArquivo('../dados_csv_instituicoes')
count=1
for instituicao in linhas:
    instituicao_splitted = instituicao[0].split(';')
    print(' %d  - %s\r\n' %( count, instituicao_splitted))
    count+=1
''' Depois de feito isso, eu limpei manualmente cada instituicao 
    removendo informacoes de estado, cidade, departamentos. '''

# Ficou a seguinte lista, se a lista tiver mais de um elemento e porque houve contribuicao de mais de uma universidade do artigo
instituicoes = [['Univcreity of Washington', 'Texas State University'], ['Texas State University'], ['Fujitsu Laboratories'], \
['University of Kent'], ['University of Kent'], ['University of Kent'], ['University of Joensuu'],
['Texas State University'], ['University of Kent'], ['Siauliai University', 'Lund University', 'Lund University', 'University of Muenster', 'Texas State University', 'NWU Vaal'], \
['IT University of Copenhagen'], ['Silesian University of Technology'], ['Texas State University'], ['Texas State University'],
['Texas State University'], ['Texas State University'], ['Texas State University', 'Johns Hopkins University'], ['University of Tampere'], ['Silesian University of Technology'],
['Silesian University of Technology'], ['Silesian University of Technology', 'Silesian University of Technology'], ['Texas State University'], ['Silesian University of Technology'],
['Texas State University'], ['Silesian University of Technology'], ['Texas State University'], ['Silesian University of Technology', 'University of Patras'],
['Silesian University of Technology', 'Institute of Theoretical and Applied Informatics, Polish Academy of Science'], ['Texas State University', 'Texas State University', 'Texas A and M University'],
['Texas State University'], ['University of Eastern Finland'], ['Silesian University of Technology', 'Institute of Theoretical and Applied Informatics, Polish Academy of Science'],
['Texas State University'], ['Texas State University'], ['Texas State University'], ['Texas State University'], ['Texas State University'], ['Texas State University'], ['University of Patras'],
['Texas State University'], ['Texas State University'], ['Texas State University', 'University of Beira Interior'], ['Silesian University of Technology', 'Texas State University-San Marcos'],
['Silesian University of Technology'], ['IT University of Copenhagen', 'Rensselaer Polytechnic Institute'], ['Silesian University of Technology'], ['Texas State University'], ['Texas State University', 'Lawrence Berkeley National Laboratory'],
['Texas State University', 'University of Washington'], ['Texas State University'], ['University of Patras'], ['Texas State University'], ['Texas State University', 'University of Southampton'],
['Silesian University of Technology', 'University of Patras'], ['Texas State University'], ['Context Relevant', 'Western Washington University', 'New York Institute of Technology'],
['Versive', 'Western Washington University', 'New York Institute of Technology'], ['King Abdulazziz University'],
['University of Jeddah'], ['King Abdulaziz University'], ['IT University of Copenhagen'], ['Texas State University'],
['University of Tampere'], ['University of Tampere'], ['University of Tampere'], ['University of Tampere'], ['University of Tampere'], ['University of Tampere']]

montaGrafoInstituicoes(instituicoes)








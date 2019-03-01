#!/usr/bin/python
#  encoding: utf-8
#
#  scriptLattes
#  http://scriptlattes.sourceforge.net/
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import pygraphviz
from PIL import Image

class GrafoDeColaboracoes:
    grupo = None
    cores = None

    grafoDeCoAutoriaSemPesos = None
    grafoDeCoAutoriaSemPesosCMAPX = None
    grafoDeCoAutoriaComPesos = None
    grafoDeCoAutoriaComPesosCMAPX = None
    grafoDeCoAutoriaNormalizado = None
    grafoDeCoAutoriaNormalizadoCMAPX = None

    def __init__(self, grupo, diretorioDeSaida):
        self.grupo = grupo



    def criarGrafoDeCoAutoriaSemPesos(self):

        return grafo

    def criarGrafoDeCoAutoriaComPesos(self):

        return grafo





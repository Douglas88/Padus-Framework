import argparse
import sys
import os
from prettytable import PrettyTable
#bannar
os.system('''cowsay "\ Padus Framework /"''')


parser = argparse.ArgumentParser(usage='%(prog)s [options]')
parser.add_argument("-v", "--version", help="Output program version", action="store_true")
parser.add_argument("-t", "--target", help="Set target address",action='append',nargs = '*')
parser.add_argument("-p", "--port", help="Set target port",action='append',nargs = '*')
parser.add_argument("-as", "--autoscan", help="Start auto scan mode", action="store_true")
parser.add_argument("-ms", "--modulescan", help="Specify the module to scan",action='append',nargs = '*')
parser.add_argument("-o", "--output", help="Output scan report", action="store_true")
parser.add_argument("-ps", "--portscan", help="Only use port scanning for the target", action="store_true")
parser.add_argument("-cs", "--cmsscan", help="Determine the target CMS", action="store_true")
parser.add_argument("-px", "--proxy", help="Enable proxy", action="store_true")
parser.add_argument("-anon", "--anonymous", help="Scan anonymously with Tor", action="store_true")
parser.add_argument("-A", "--all", help="Export all supported modules", action="store_true")
parser.add_argument("-c", "--clean", help="Delete all temporary files", action="store_true")
args = parser.parse_args()

path = os.getcwd()
logs_dir = (path+'/logs')
core = (path+'/core')
vul_scan = (path+'/lib/vul_scan')
print("\n")
from lib.utils import statistics

if args.version:
	print("\033[1;34m[Version]\033[0m 1.0.1") #Blue
if args.target:
	ip = args.target[0]
	ip = ','.join(str(i) for i in ip)
	with open(logs_dir + '/url.log','w') as f:
  		f.write(ip)
if args.port:
	port = args.port[0]
	port = ','.join(str(i) for i in port)
	with open(logs_dir + '/port.log','w') as f:
  		f.write(port)

if args.autoscan:
	os.system("python3 %s/autoscan.py" %(core))

if args.modulescan:
	print("\033[1;36m[INFO]\033[0m The module scanner has started, you may need to fill in some information manually.")
	module = args.modulescan[0]
	module = ','.join(str(i) for i in module)
	print("[+]",module)
	os.system("python3 %s/%s/%s.py" %(vul_scan,module,module))
if args.clean:
	os.system("rm -rf %s/*" %(logs_dir))

if args.cmsscan:
	from lib.utils import cmsscan

if args.all:

    table = PrettyTable(['Serial Number','Module Name','Introduction','Automatic use'])
    table.add_row(['1','weblogic',"Oracle WebLogic Server",'Y'])
    table.add_row(['2','thinkcmf','Open source content management framework','N'])
    table.add_row(['3','drupal','Open source content management framework','N'])
    table.add_row(['4','imagemagick','Convert, Edit, or Compose Digital Images','N'])
    table.add_row(['5','mysql','Database Service','Y'])
    table.add_row(['6','scrapy','Open source web crawler framework','N'])
    table.add_row(['7','ecshop','Free and open source e-commerce platform','N'])
    table.add_row(['8','influxdb','Open source time series database','N'])
    table.add_row(['9','nexus','Nexus','Y'])
    table.add_row(['10','shiro','Apache Shiro','Y'])
    table.add_row(['11','elasticsearch','a trademark of Elasticsearch B.V.','N'])
    table.add_row(['12','jackson','Jackson','N'])
    table.add_row(['13','nginx','high-performance HTTP server and reverse proxy','Y'])
    table.add_row(['14','skywalking','Apache SkyWalking','Y'])
    table.add_row(['15','activemq','Apache ActiveMQ','Y'])
    table.add_row(['16','electron','An open source framework developed by GitHub','N'])
    table.add_row(['17','java','Java','N'])
    table.add_row(['18','node','Cross-platform JavaScript execution environment','Y'])
    table.add_row(['19','solr','Apache solr','Y'])
    table.add_row(['20','apereo-cas','Apereo-CAS','Y'])
    table.add_row(['21','fastjson','convert Java Objects into their JSON representation','Y'])
    table.add_row(['22','jboss','Web application based on SOA architecture','Y'])
    table.add_row(['23','ofbiz','The Apache OFBiz Project','Y'])
    table.add_row(['24','spark','Apache Spark','Y'])
    table.add_row(['25','appweb','Embedded Web Server','Y'])
    table.add_row(['26','ffmpeg','FFmpeg','Y'])
    table.add_row(['27','jenkins','Open source continuous integration tool','Y'])
    table.add_row(['28','openssh','OpenBSD sub-project','Y'])
    table.add_row(['29','spring','Spring Framework','Y'])
    table.add_row(['30','aria2','Download manager','Y'])
    table.add_row(['31','flask','Lightweight web application framework','Y'])
    table.add_row(['32','jira','Defect Tracking Management System','Y'])
    table.add_row(['33','openssl','Open source software library package','Y'])
    table.add_row(['34','struts2','Apache Struts 2','Y'])
    table.add_row(['35','flink','Apache Flink','Y'])
    table.add_row(['36','jmeter','Apache JMeter','Y'])
    table.add_row(['37','php','general-purpose scripting language','Y'])
    table.add_row(['38','supervisor','Supervisor','Y'])
    table.add_row(['39','bash',"GNU Project's shell",'Y'])
    table.add_row(['40','ghostscript','interpreter for the PostScript language and PDF files','Y'])
    table.add_row(['41','joomla','Open source content management framework','Y'])
    table.add_row(['42','phpmailer','code library to send (transport) emails','Y'])
    table.add_row(['43','git','open source distributed version control system','Y'])
    table.add_row(['44','jupyter','open-source web application','Y'])
    table.add_row(['45','phpmyadmin','MySQL database management tool','Y'])
    table.add_row(['46','thinkphp','Open source content management framework','Y'])
    table.add_row(['47','coldfusion','Adobe ColdFusion','Y'])
    table.add_row(['48','gitea','A painless self-hosted Git service','Y'])
    table.add_row(['49','kibana','Explore, Visualize, Discover Data | Elastic','Y'])
    table.add_row(['50','phpunit','PHP Testing Framework','Y'])
    table.add_row(['51','tikiwiki','Open source content management framework','Y'])
    table.add_row(['52','confluence','Remote-Friendly Team Workspace','Y'])
    table.add_row(['53','gitlab','A painless self-hosted Git service','Y'])
    table.add_row(['54','laravel',' PHP Framework For Web Artisans','Y'])
    table.add_row(['55','postgres','open source database','Y'])
    table.add_row(['56','tomcat','Apache Tomcat','Y'])
    table.add_row(['57','gitlist','An elegant and modern git repository viewer','Y'])
    table.add_row(['58','libssh','The SSH Library','Y'])
    table.add_row(['59','python','Python Programming Language','N'])
    table.add_row(['60','unomi','Apache Unomi','Y'])
    table.add_row(['61','glassfish','Open Source Java EE Reference Implementation','N'])
    table.add_row(['62','liferay-portal','open source portal framework','Y'])
    table.add_row(['63','rails','A web-application framework','Y'])
    table.add_row(['64','uwsgi','building hosting services','Y'])
    table.add_row(['65','couchdb','Apache CouchDB','Y'])
    table.add_row(['66','goahead','Embedded Web Servers','Y'])
    table.add_row(['67','log4j','Apache Log4j','Y'])
    table.add_row(['68','redis','Key-value pair storage database','Y'])
    table.add_row(['69','discuz','Open source content management framework','Y'])
    table.add_row(['70','gogs','A painless self-hosted Git service','Y'])
    table.add_row(['71','magento','Magento','Y'])
    table.add_row(['72','rsync',' fast and extraordinarily versatile file copying tool','N'])
    table.add_row(['73','webmin','web-based interface for system administration for Unix','Y'])
    table.add_row(['74','django','Web framework for perfectionists with deadlines','N'])
    table.add_row(['75','h2database',' free SQL database written in Java','Y'])
    table.add_row(['76','mini_httpd','small HTTP server','Y'])
    table.add_row(['77','ruby','Ruby Programming Language','Y'])
    table.add_row(['78','wordpress','Open source content management framework','Y'])
    table.add_row(['79','dns','Domain Name System','Y'])
    table.add_row(['80','hadoop','Apache Hadoop','Y'])
    table.add_row(['81','mojarra','Mojarra','Y'])
    table.add_row(['82','saltstack','Python-based','Y'])
    table.add_row(['83','xxl-job','A distributed task scheduling framework','Y'])
    table.add_row(['84','docker','Empowering App Development for Developers','N'])
    table.add_row(['85','httpd','Apache HTTP Server','Y'])
    table.add_row(['86','mongo-express','Web-based MongoDB admin interface','Y'])
    table.add_row(['87','samba','SMB/CIFS','Y'])
    table.add_row(['88','zabbix','Network monitoring and management system','Y'])


    print(table)







	
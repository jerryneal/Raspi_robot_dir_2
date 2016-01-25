import httplib
import smtplib
import urllib2
#import bs4



# configure script's parameters here

class Testor(object):

    def __init__(self):
        pass

    def connectionmade(self):
        thresholdRate = 1.30
        smtpServer = 'smtp.gmail.com:587'
        fromaddr = 'foo@bar.com'
        toaddrs = 'mck#####@live.com'
        # end of configuration
        url = '/en/financial_markets/csv/exchange_eng.csv'
        conn = httplib.HTTPConnection('www.bankofcanada.ca')
        conn.request('GET', url)
        response = conn.getresponse()
        data = response.read()
        print data
        start = data.index('USD')
        line = data[start:data.index('\n', start)] # get the relevant line
        #rate = line.split(',')[-1] # last field on the line
        rate = 1.10
        if float(rate) < thresholdRate:
             # send email
             msg = 'Subject: Bank of Canada exchange rate alert %s' % rate
             #msg = 'Subject: Bank of Canada exchange rate alert'
             server = smtplib.SMTP(smtpServer)
             server.login('chaprolls@gmail.com','delicious15')
             server.sendmail(fromaddr, toaddrs, msg)
             server.quit()
             conn.close()





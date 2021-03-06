import jsonlines
import os
from datetime import date, timedelta
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

def textHasData(line):
    return (line['text'] != "")

def getSetOfDates(fileName):
    dates = set()
    with jsonlines.open(fileName) as reader:
        for line in reader:
            dates.add(line['date'])

    listDates=list(dates)
    listDates.sort()
    return{'fileName':fileName,'dates':listDates}

def getRowCount(fileName):
    count = 0
    try:
        if os.path.isfile(fileName):
            with jsonlines.open(fileName) as reader:
                for line in reader:
                    count=count+1
    except:
        pass
    
    return count
   


'Get the Today adn Yesterday dates'
##Today = date.today().strftime("%Y-%m-%d")
##yesterday = date.today() - timedelta(1)
##Yesterday = yesterday.strftime("%Y-%m-%d")

today=date.today()
#today=date(2017,11,9)
Today = today.strftime("%Y-%m-%d")
yesterday = today - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
# if (len(sys.argv) == 1):
    # print '>>1>>'
    # today=date.today()
# elif (len(sys.argv) == 4):
    # print '>>2>>'
# else:
    # print '--------------------------------------'
    # print 'Usage Python DailyReport.py 2018 03 12'
    # print '--------------------------------------'
    
    # today=date(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))

    print 'Today is %s.%s.%s' % (sys.argv[1],sys.argv[2],sys.argv[3])

    headings='%-15s %-12s %7s'%('Source','Date','Records')
# recs=[{'Source':'Blitz','Date':Today,'Records':0},
    # {'Source':'24chasa','Date':Today,'Records':0},
    # {'Source':'Trud','Date':Today,'Records':0},
    # {'Source':'Duma','Date':Today,'Records':0},
    # {'Source':'Mediapool','Date':Today,'Records':0},
    # {'Source':'ClubZ','Date':Today,'Records':0},
    # {'Source':'Classa','Date':Today,'Records':0},
    # {'Source':'Epicenter','Date':Today,'Records':0},
    # {'Source':'Faktor','Date':Today,'Records':0},
    # {'Source':'Dnes','Date':Today,'Records':0},
    # {'Source':'StandartNews','Date':Today,'Records':0},
    # {'Source':'Actualno','Date':Yesterday,'Records':0},
    # {'Source':'BNews','Date':Yesterday,'Records':0},
    # {'Source':'Cross','Date':Yesterday,'Records':0},
    # {'Source':'Dnevnik','Date':Yesterday,'Records':0},
    # {'Source':'Focus','Date':Yesterday,'Records':0},
    # {'Source':'Monitor','Date':Yesterday,'Records':0},
    # {'Source':'News','Date':Yesterday,'Records':0},
    # {'Source':'Novinite','Date':Yesterday,'Records':0},
    # {'Source':'OffNews','Date':Yesterday,'Records':0},
    # {'Source':'PIK','Date':Yesterday,'Records':0},
    # {'Source':'BgOnAir','Date':Yesterday,'Records':0},
    # # {'Source':'SegaBG','Date':Yesterday,'Records':0}
     # ]

# line= '-'*36
# print 'Daily Summary Report'
# print 'Today: '+Today+'\n'+line
# print headings+'\n'+line
# for rec in recs:
    # path=rec['Source']+'/Reports/'+rec['Source']+'-'+rec['Date']+'.json'
    # rec['Records']= getRowCount(path)
    # print '%-15s %-12s %7s'%(rec['Source'],rec['Date'],rec['Records'])
# print line

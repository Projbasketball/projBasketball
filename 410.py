# -*- coding: utf-8 -*-
"""
Created on Sat May 03 23:21:32 2014

@author: aaron
"""
from xml.dom.minidom import parse, parseString
from urllib2 import Request, urlopen, URLError
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from flask import Flask, request, jsonify, render_template
from flask.views import MethodView
import time, json


#hardcode for testing
#playerID = "1f9d116b-7c1b-4d1a-bf02-59ba4b22092e"
#name = "Tim Duncan"
teamNum = 24

#stuff to keep it running
app = Flask(__name__, template_folder="")








#    wizards     = "583ec8d4-fb46-11e1-82cb-f4ce4684ea4c"
#    bobcats     = "583ec97e-fb46-11e1-82cb-f4ce4684ea4c"
#    hawks       = "583ecb8f-fb46-11e1-82cb-f4ce4684ea4c"
#    heat        = "583ecea6-fb46-11e1-82cb-f4ce4684ea4c"
#    magic       = "583ed157-fb46-11e1-82cb-f4ce4684ea4c"
#    knicks      = "583ec70e-fb46-11e1-82cb-f4ce4684ea4c"
#    sevensixers = "583ec87d-fb46-11e1-82cb-f4ce4684ea4c"
#    nets        = "583ec9d6-fb46-11e1-82cb-f4ce4684ea4c"
#    celtics     = "583eccfa-fb46-11e1-82cb-f4ce4684ea4c"
#    raptors     = "583ecda6-fb46-11e1-82cb-f4ce4684ea4c"
#    bulls       = "583ec5fd-fb46-11e1-82cb-f4ce4684ea4c"
#    cavaliers   = "583ec773-fb46-11e1-82cb-f4ce4684ea4c"
#    pacers      = "583ec7cd-fb46-11e1-82cb-f4ce4684ea4c"
#    pistons     = "583ec928-fb46-11e1-82cb-f4ce4684ea4c"
#    bucks       = "583ecefd-fb46-11e1-82cb-f4ce4684ea4c"
#    timberwolves= "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"
#    jazz        = "583ece50-fb46-11e1-82cb-f4ce4684ea4c"
#    thunder     = "583ecfff-fb46-11e1-82cb-f4ce4684ea4c"
#    trailblazers= "583ed056-fb46-11e1-82cb-f4ce4684ea4c"
#    nuggets     = "583ed102-fb46-11e1-82cb-f4ce4684ea4c"
#    grizzlies   = "583eca88-fb46-11e1-82cb-f4ce4684ea4c"
#    rockets     = "583ecb3a-fb46-11e1-82cb-f4ce4684ea4c"
#    pelicans    = "583ecc9a-fb46-11e1-82cb-f4ce4684ea4c"
#    spurs       = "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c"
#    mavericks   = "583ecf50-fb46-11e1-82cb-f4ce4684ea4c"
#    warriors    = "583ec825-fb46-11e1-82cb-f4ce4684ea4c"
#    lakers      = "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
#    clippers    = "583ecdfb-fb46-11e1-82cb-f4ce4684ea4c" 
#    suns        = "583ecfa8-fb46-11e1-82cb-f4ce4684ea4c"
#    kings       = "583ed0ac-fb46-11e1-82cb-f4ce4684ea4c"


def getTeam (teamNum):    


    if (teamNum == 1) : 
        return "583ec8d4-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 2) : 
        return "583ec97e-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 3) : 
        return "583ecb8f-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 4) : 
        return "583ecea6-fb46-11e1-82cb-f4ce4684ea4c"        
    elif (teamNum == 5) : 
        return "583ed157-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 6) : 
        return "583ec70e-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 7) : 
        return "583ec87d-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 8) : 
        return "583ec9d6-fb46-11e1-82cb-f4ce4684ea4c"    
    elif (teamNum == 9) : 
        return "583eccfa-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 10) : 
        return "583ecda6-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 11) : 
        return "583ec5fd-fb46-11e1-82cb-f4ce4684ea4c"  
    elif (teamNum == 12) : 
        return "583ec773-fb46-11e1-82cb-f4ce4684ea4c"    
    elif (teamNum == 13) : 
        return "583ec7cd-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 14) : 
        return "583ec928-fb46-11e1-82cb-f4ce4684ea4c"     
    elif (teamNum == 15) : 
        return "583ecefd-fb46-11e1-82cb-f4ce4684ea4c"        
    elif (teamNum == 16) : 
        return "583eca2f-fb46-11e1-82cb-f4ce4684ea4c"        
    elif (teamNum == 17) : 
        return "583ece50-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 18) : 
        return "583ecfff-fb46-11e1-82cb-f4ce4684ea4c"       
    elif (teamNum == 19) : 
        return "583ed056-fb46-11e1-82cb-f4ce4684ea4c"        
    elif (teamNum == 20) : 
        return "583ed102-fb46-11e1-82cb-f4ce4684ea4c" 
    elif (teamNum == 21) : 
        return "583eca88-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 22) : 
        return "583ecb3a-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 23) : 
        return "583ecc9a-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 24) : 
        return "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 25) : 
        return "583ecf50-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 26) : 
        return "583ec825-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 27) : 
        return "583ecae2-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 28) : 
        return "583ecdfb-fb46-11e1-82cb-f4ce4684ea4c"
    elif (teamNum == 29) : 
        return "583ecfa8-fb46-11e1-82cb-f4ce4684ea4c" 
    elif (teamNum == 30) : 
        return "583ed0ac-fb46-11e1-82cb-f4ce4684ea4c"
    
def roster(teamID):
    #http://api.sportsdatallc.org/nba-t3/teams/583ecd4f-fb46-11e1-82cb-f4ce4684ea4c/profile.xml?api_key=8uhnntmn4wst6z4vnraq3vpw
    request = Request("http://api.sportsdatallc.org/nba-t3/teams/" + teamID + "/profile.xml?api_key=8uhnntmn4wst6z4vnraq3vpw")
    try:
        myFile = open('roster.xml', 'w')
    
        response = urlopen(request)
        time.sleep(1)
        roster = response.read()
        myFile.write(roster)
        myFile.close()
        return roster
    except URLError, e:
        print 'Roster', e

def rosterSearch(roster):
    dom = parse("roster.xml") # parse an XML file by name
    #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:

    for i in range(0, 13):
        #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
        xmlTag = dom.getElementsByTagName('player')[i].toxml()
        #strip off the tag (<tag>data</tag>  --->   data):
        xmlData=xmlTag.replace('<player>','').replace('</player>','')
        #if full_name occurs, assign, break, else keep going
        if(xmlData.find(name) != -1):
            pID = xmlData
            start = xmlData.find(" id=")
            pID = pID[start+5:start+41]
            return pID
            
    print "Didn't find player"
    
def getStat(pID):

    #http://api.sportsdatallc.org/nba-t3/players/1f9d116b-7c1b-4d1a-bf02-59ba4b22092e/profile.xml?api_key=8uhnntmn4wst6z4vnraq3vpw
    request = Request("http://api.sportsdatallc.org/nba-t3/players/" + pID + "/profile.xml?api_key=8uhnntmn4wst6z4vnraq3vpw")
    
    try:
        myFile = open('player.xml', 'wb')

        response = urlopen(request)
        pStat = response.read()       
        myFile.write(pStat)
        myFile.close()
#        print pStat
        return pStat


    except URLError, e:
        print "Get Stat", e
        
def parseXML(pStat):
    #tree = ET.parse("player.xml")
    #root = tree.getroot()
    #root.findall(".")
    #root.findall("./sesasons/season id")
    #print root
    dom = parseString(pStat) # parse an XML file by name
    #retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
    xmlTag = dom.getElementsByTagName('statistics')[0].toxml()
    #strip off the tag (<tag>data</tag>  --->   data):
    xmlData=xmlTag.replace('<statistics>','').replace('</statistics>','')
    return xmlTag




#http://stackoverflow.com/questions/191536/converting-xml-to-json-using-python
#parsing xml to json after putting xml info in a data structure
#import xmltodict, json
#
#o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
#json.dumps(o) # '{"e": {"a": ["text", "text"]}}'





#teamID = getTeam(teamNum)
#pID = rosterSearch(roster(teamID))

#adds quotes
#pID = '"%s"' % pID.strip() 

#pStat = str(getStat(pID))
#readableStats = parseXML(pStat)

class TodoView(MethodView):
    def get(self):
        return render_template('/templates/main.html')
        


#post/get stuff
class TodoRetrieve(MethodView):
    def post(self):
        name = json.loads(request.data)
        print(name)
#        name = str(name)
#        name['search']
        return name




class TodoAdd(MethodView):
	def get(self):
         teamID = getTeam(teamNum)
         pID = rosterSearch(roster(teamID))
         pStat = str(getStat(pID))
         return jsonify({'statistics': parseXML(pStat)})

app.add_url_rule('/', view_func=TodoView.as_view('todo_view'))
#method that he is using
app.add_url_rule('/search', view_func = TodoRetrieve.as_view("todo_retrieve"), methods=['POST'])
app.add_url_rule('/response', view_func = TodoAdd.as_view("todo_add"), methods=['GET'])

if __name__ == "__main__":
    app.run(debug=True) #<-- use this for localhost

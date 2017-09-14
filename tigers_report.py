import requests
from bs4 import BeautifulSoup
import re

def main():
	message = createReportMessage()
	print(message)
    
def createReportMessage():
    teamNameList = []
    teamPointList = []

    url = 'https://m.hanshintigers.jp/game/score/'
    headers = {'User-Agent': 'YOUR-USER-AGENT'}
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')
    # now inning
    inning = soup.find(class_='inning').text

    # get team names
    for i in soup.find_all('img', src=re.compile("/images/logo/logo_")):
        teamNameList.append(i['src'])

    # get team points
    for i in soup.find_all(class_='number'):
        teamPointList.append(i.text)

    # set team names and points
    for i, team in enumerate(teamNameList):
        # TIGERS
        if team == '/images/logo/logo_t.png':
            tigers_name = "阪神"
            tigers_number = teamPointList[i]
        # CARP
        elif team == '/images/logo/logo_c.png':
            opponent_name = "広島"
            opponent_number = teamPointList[i]
        # GIANTS
        elif team == '/images/logo/logo_g.png':
            opponent_name = "巨人"
            opponent_number = teamPointList[i]
        # DRAGONS
        elif team == '/images/logo/logo_d.png':
            opponent_name = "中日"
            opponent_number = teamPointList[i]
        # SWAROWS
        elif team == '/images/logo/logo_s.png':
            opponent_name = "ヤクルト"
            opponent_number = teamPointList[i]
        # BAYSTARS
        elif team == '/images/logo/logo_db.png':
            opponent_name = "横浜"
            opponent_number = teamPointList[i]

    # generate message
    message = inning + '\n' + tigers_name + tigers_number + ' - ' + opponent_number + opponent_name
    return message

if __name__ == '__main__':
	main()

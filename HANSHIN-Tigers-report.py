import requests
from bs4 import BeautifulSoup
import re

def main():
	message = createReportMessage()
	print(message)
    
# 試合速報メッセージ作成
def createReportMessage():
    teamNameList = []
    teamPointList = []

    url = 'https://m.hanshintigers.jp/game/score/'
    headers = {'User-Agent': 'YOUR-USER-AGENT'}
    request = requests.get(url, headers=headers)
    # HTMLパーサ
    soup = BeautifulSoup(request.text, 'lxml')
    # 現在のイニング
    inning = soup.find(class_='inning').text

    # 両チームの名前取得
    for i in soup.find_all('img', src=re.compile("/images/logo/logo_")):
        teamNameList.append(i['src'])

    # 両チームの点数取得
    for i in soup.find_all(class_='number'):
        teamPointList.append(i.text)

    # 両チームの名前と点数をセット
    for i, team in enumerate(teamNameList):
        # 阪神の場合
        if team == '/images/logo/logo_t.png':
            tigers_name = "阪神"
            tigers_number = teamPointList[i]
        # 広島の場合
        elif team == '/images/logo/logo_c.png':
            opponent_name = "広島"
            opponent_number = teamPointList[i]
        # 巨人の場合
        elif team == '/images/logo/logo_g.png':
            opponent_name = "巨人"
            opponent_number = teamPointList[i]
        # 中日の場合
        elif team == '/images/logo/logo_d.png':
            opponent_name = "中日"
            opponent_number = teamPointList[i]
        # ヤクルトの場合
        elif team == '/images/logo/logo_s.png':
            opponent_name = "ヤクルト"
            opponent_number = teamPointList[i]
        # 横浜の場合
        elif team == '/images/logo/logo_db.png':
            opponent_name = "横浜"
            opponent_number = teamPointList[i]

    # メッセージ生成
    message = inning + '\n' + tigers_name + tigers_number + ' - ' + opponent_number + opponent_name
    return message

if __name__ == '__main__':
	main()

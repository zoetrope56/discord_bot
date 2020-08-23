import bs4
from urllib.request import urlopen, Request
import urllib

class Now():
    def __init__(self):
        self.weather = str()
    
    def check_param(self, message):
        self.weather = message.content.split()
        if len(self.weather) > 1:
            enc_location = urllib.parse.quote(self.weather[1]+'+날씨')
        else:
            # 만약 정보가 들어있는 리스트의 길이가 1보다 작으면? 강남의 날씨 반환
            enc_location = urllib.parse.quote('강남+날씨')

        try:
            url = 'https://search.naver.com/search.naver?ie=utf8&query='+enc_location 
            req = Request(url)
            page = urlopen(req)
            html = page.read()
            soup = bs4.BeautifulSoup(html, 'html5lib')

            response = '현재 ' + soup.find('span', class_='btn_select').find('em').text + '의 기온은 ' + \
                        soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + \
                        '도 입니다.\n' +soup.find('p', class_='cast_txt').text+'\n'
            return response
        except Exception as e:
            print(e)
            response = '죄송합니다. 관련 정보가 없습니다.\n감사합니다.\n'
            return response

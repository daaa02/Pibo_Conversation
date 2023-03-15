from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = {
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
}

json_file='/home/pi/Pibo_Conversation/data/dayoung-123-1e6969392f38.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
gc = gspread.authorize(credentials)
url = "https://docs.google.com/spreadsheets/d/1JPMgIQ7QdIDO6KdecXQAOQhSjGguXZOXufXkkpXorwQ/edit?usp=sharing"

today = datetime.now().strftime('%Y-%m-%d %H:%M')
user_name = "이름"

class google_spread_sheet():
    
    def make_sheet(self):
        ms = gc.create(f'{user_name}')    # file name
        worksheet = ms.get_worksheet(0)     # 첫 번째 시트
        worksheet.append_row(['활동일', '활동명', '의사소통', '사회성', '인지', '근육'])
        # worksheet.resize(50, 50)
        ms.share('dyk98498@gmail.com', perm_type='user', role='writer')     
    
    def write_sheet(self, today, activities, score):
        # # 새로 만든 시트에 쓰기
        # ws = gc.open(f'{user_name}')
        # worksheet = ws.get_worksheet(0)
        
        # 만들어졌던 시트에 쓰기
        os = gc.open_by_url(url)
        worksheet = os.get_worksheet(0)
        
        str_list = list(filter(None, worksheet.col_values(1)))
        next = len(str_list)+1
        worksheet.update(f'A{next}', today)
        worksheet.update(f'B{next}', activities)
        worksheet.append_row(score, table_range=f'C{next}')

    def save_sheet(self):
        ss = gc.open(f'{user_name}')
        worksheet = ss.get_worksheet(0)
        ss.share('dyk98498@gmail.com', perm_type='user', role='writer')
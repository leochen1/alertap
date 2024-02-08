
import datetime as t
import pytz
from datetime import datetime
import requests

taiwan_tz = pytz.timezone("Asia/Taipei") #時區


# 發送 Line Notify 通知
# https://developers.line.biz/en/docs/messaging-api/sticker-list/#sticker-definitions
def send_line_notify(notification_message, stickerPackageId, stickerId):
    line_notify_token = 'boHMgzAvRReM6BADCyM3eodXmqkgrkrwlRD2P4Utf0b'  # LB排程事項通知群
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {
        'message': notification_message,
        'stickerPackageId': stickerPackageId,
        'stickerId': stickerId
    }
    requests.post(line_notify_api, headers=headers, data=data)



def test():
    message = f"test"
    print(message)
    send_line_notify(message, '6359', '11069871')


# 通知就寢
def notice_sleep():
    message = f"小公主, 現在時間 : {t.datetime.now(taiwan_tz)}, 該睡覺了喔 !"
    print(message)
    send_line_notify(message, '6359', '11069871')
    

# 通知每月第一個星期三, 繳電話費
def notice_cellphone_tax():
    if datetime.today().weekday() == 2 and 1 <= datetime.today().day <= 7:
        message = f"小公主, 現在時間 : {t.datetime.now(taiwan_tz)}, 該繳電話費了喔 !"
        print(message)
        send_line_notify(message, '6359', '11069853')
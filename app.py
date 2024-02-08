import streamlit as st
import time, pytz, schedule
from datetime import datetime
import datetime as t
from notices import *
from streamlit_autorefresh import st_autorefresh
import requests

st_autorefresh(interval=1000)
st.title("事項排程通知 !!!")
taiwan_tz = pytz.timezone("Asia/Taipei") #時區
st.write(f":green[{t.datetime.now(taiwan_tz)}]")
st.divider()

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
    
def send_heartbeat():
    try:
        # 使用你的 Render 應用實際的 URL
        response = requests.get('https://li-ou-xiao-gong-zhu-pai-cheng-shi-xiang.onrender.com/')
        print(f"Heartbeat sent! Status Code: {response.status_code}, {t.datetime.now(taiwan_tz)}")
        st.write(f"Heartbeat sent! Status Code: {response.status_code}, {t.datetime.now(taiwan_tz)}")
        send_line_notify(f"Heartbeat 30 min sent! {t.datetime.now(taiwan_tz)}", '6359', '11069871')
    except Exception as e:
        print(f"Error sending heartbeat: {e}")


def test():
    message = f"整點測試"
    print(message)
    st.write(f"{message}, {t.datetime.now(taiwan_tz)}")
    send_line_notify(f"{message}, {t.datetime.now(taiwan_tz)}", '6359', '11069871')


# schedule.every().second.do(send_heartbeat)  # 每秒發送心跳
schedule.every().wednesday.at("00:00").do(notice_cellphone_tax) # 每月第一個星期三 通知繳電話費
schedule.every().day.at("23:00").do(notice_sleep)  # 每天 23:00 通知就寢

schedule.every().hour.at(":00").do(test) # 每小時整點測試
schedule.every().hour.at(":30").do(send_heartbeat)

while True:
    schedule.run_pending()
    time.sleep(1)





import streamlit as st
import time, pytz, schedule
from datetime import datetime
import datetime as t
from notices import *
from streamlit_autorefresh import st_autorefresh
import requests

st_autorefresh(interval=5000)
st.title("事項排程通知 !!!")
taiwan_tz = pytz.timezone("Asia/Taipei") #時區
st.write(f":green[{t.datetime.now(taiwan_tz)}]")
st.divider()


def send_heartbeat():
    try:
        # 使用你的 Render 應用實際的 URL
        response = requests.get('https://li-ou-xiao-gong-zhu-pai-cheng-shi-xiang.onrender.com/')
        print(f"Heartbeat sent! Status Code: {response.status_code}")
        st.write(f"Heartbeat sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending heartbeat: {e}")

schedule.every().second.do(send_heartbeat)  # 每秒發送心跳
schedule.every().wednesday.at("00:00").do(notice_cellphone_tax) # 每月第一個星期三 通知繳電話費
schedule.every().day.at("23:00").do(notice_sleep)  # 每天 23:00 通知就寢
schedule.every().day.at("23:55").do(test)  # 每天 23:00 通知就寢
schedule.every().day.at("23:56").do(test)  # 每天 23:00 通知就寢

while True:
    schedule.run_pending()
    time.sleep(1)





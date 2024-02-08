import streamlit as st
import time, pytz, schedule
from datetime import datetime
import datetime as t
from notices import *


st.title("事項排程通知 !!!")
taiwan_tz = pytz.timezone("Asia/Taipei") #時區
st.write(f":green[{t.datetime.now(taiwan_tz)}]")
st.divider()




schedule.every().wednesday.at("00:00").do(notice_cellphone_tax) # 每月第一個星期三 通知繳電話費
schedule.every().day.at("23:00").do(notice_sleep)  # 每天 23:00 通知就寢



while True:
    schedule.run_pending()
    time.sleep(1)





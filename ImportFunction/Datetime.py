from datetime import datetime, timedelta, timezone

class DatetimeGet():
    def GetNowDT():
        taipei_timezone = timezone(timedelta(hours=8)) #獲得台北時區
        current_time = datetime.now(taipei_timezone) #將當前時間轉換成台北時區
        formatted_date_time = current_time.strftime("%Y-%m-%d %H:%M:%S") #格式化日期的字串
        return formatted_date_time
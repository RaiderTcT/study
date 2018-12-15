from datetime import datetime, timedelta, timezone
import time
import re


def to_timestamp(dt_str, tz_str):
    pa = re.compile(r'^UTC(\+|-)(\d{1,2}):00$')
    tz = pa.match(tz_str).group(2)
    cal = pa.match(tz_str).group(1)
    tz = int(cal+tz)
    time_zone = timezone(timedelta(hours=tz))
    time0 = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S').replace(tzinfo=time_zone)
    return time0.timestamp()


if __name__ == "__main__":

    # clock 以浮点数计算的秒数返回当前的CPU时间
    clock0 = time.clock()

    # now: 2018-08-29 09:51:49.523958
    now = datetime.now()
    print('now:', now)

    # Wed Aug 29 09:51:49 2018
    # 将输入秒 转为时间 从1970年开始
    # 无参数，则为当前时间
    ctime = time.ctime()
    print('ctime:', ctime)

    clock = time.clock()
    print('clock:', time.clock() - clock0)

    # 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    time_now = time.time()
    print('time:', time_now)

    dt = datetime(2018, 8, 17, 12, 0)
    print('dt:', dt)
    # 转换为timestamp 秒 与时区无关
    print('dt.timetamp:', dt.timestamp())

    # 秒转为datetime
    t = 1534475443.0
    print('UTC+8:', datetime.fromtimestamp(t))
    # 格林威治标准时间 UTC+0:00
    print('UTC+0:', datetime.utcfromtimestamp(t))

    # 时间转字符串
    str_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print('date to str:', str_date)

    cdate = datetime.strptime('2018-8-17 12:00:00', '%Y-%m-%d %H:%M:%S')
    print('str to date:', cdate)

    print('8 hours later:', now + timedelta(hours=10))

    # weeks days hours minutes...
    print('1 week beforel', now - timedelta(weeks=1))

    tz_utc_8 = timezone(timedelta(hours=8))
    dt = now.replace(tzinfo=tz_utc_8)
    print('UTC-8 time:', dt)

    # 时区转换
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    print('utc now:', utc_now)
    bj_time = utc_now.astimezone(timezone(timedelta(hours=8)))
    tokyo_time = utc_now.astimezone(timezone(timedelta(hours=9)))
    print('Beijing :', bj_time)
    print('Tokyo :', tokyo_time)
    t1 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    print(t1)

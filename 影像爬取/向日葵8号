import sys
import json
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
from dateutil import tz
import psycopg2
import time
import random

conf = {
    'last_refresh_url': 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json',  # latest photo
    'img_url_pattern': 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/%id/550/%s_%i_%i.png',    # scale, time, row, col
    'scale': 2,     # 1, 2, 4, 8, 16, 20.  Width and height are both 550*scale
}

'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/2d/550/2018/09/19/065000_0_0.png'
'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/770/coastline/00ff00_0_0.png'

headers = ['Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
           "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           ]


# Convert time
def utf2local(utc):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = utc.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone)


def download(args):
    scale = args['scale']
    png = Image.new('RGB', (550*scale, 550*scale))
    for row in range(scale):
        for col in range(scale):
            print('Downloading %i of %i ...' % (row*scale + col + 1, scale*scale))
            strtime = args['time'].strftime("%Y/%m/%d/%H%M%S")

            url = conf['img_url_pattern'] % (args['scale'], strtime, row, col)
            try:
                r = requests.get(url, headers={'User-Agent': random.choice(headers)}, timeout=100)
                tile = Image.open(BytesIO(r.content))
                png.paste(tile, (550 * row, 550 * col, 550 * (row + 1), 550 * (col + 1)))
            except requests.exceptions.Timeout:
                print("请求超时")
            except requests.exceptions.ConnectionError:
                print("连接超时")
    if 'fout' in args:
        fpath = args['fout']
    else:
        fpath = "%s.png" % utf2local(args['time']).strftime("/%Y/%m/%d/%H%M%S").replace('/', '')
        # path = "%s.png" % utf2local(args['time']).strftime("%Y/%m/%d/%H%M%S").replace('/', '')
    url = fpath
    dttime = utf2local(args['time']).strftime("%Y-%m-%d %H:%M:%S")
    print(dttime)
    # postgres数据库操作
    conn = psycopg2.connect(host='47.95.10.198', user='postgres', password='qwe123', database='zxdsj')
    con = conn.cursor()
    sql1 = "select * from qg_server where dttime='{}'".format(dttime)
    con.execute(sql1)
    conn.commit()
    rows = con.fetchall()
    if len(rows) == 0:
        path = "%s.png" % utf2local(args['time']).strftime("%Y/%m/%d/%H%M%S").replace('/', '')
        sql = "insert into qg_server(url,dttime) values(%s,%s)"  # url图片路径  dttime 抓取时间
        params = (url, dttime)
        con.execute(sql, params)
        conn.commit()
        png.save(path, "PNG")
    else:
        print("时间数据已存在")

    conn.close()


def get_last_time():
    try:
        r = requests.get(conf['last_refresh_url'], headers={'User-Agent': random.choice(headers)})
        resp = json.loads(r.text)
        last_refresh_time = datetime.strptime(resp['date'], '%Y-%m-%d %H:%M:%S')
        return last_refresh_time
    except requests.exceptions.ConnectionError:
        print("请求图片最新时间异常")



def get_last_image(fout=None, scale=2):
    # print('output[%s] scale[%i]' % (fout, scale))
    last_refresh_time = get_last_time()
    args = {'time': last_refresh_time}
    args['scale'] = scale
    if fout is not None:
        args['fout'] = fout
    download(args)


if __name__ == '__main__':
    while True:
        if len(sys.argv) == 1:
            get_last_image()
        elif len(sys.argv) == 2:
            get_last_image(fout=sys.argv[1])
        elif len(sys.argv) == 3:
            get_last_image(fout=sys.argv[1], scale=int(sys.argv[2]))
        time.sleep(600)

'''爬取向日葵8号网站数据存放linux上，十分钟新增一条数据和删除第一条数据，删除文件夹下指定图片'''
